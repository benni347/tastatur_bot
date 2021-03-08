from tkinter import messagebox

import base
#import time

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def fourN(url):
  driver = base.login(url = url)
  wait = WebDriverWait(driver, 3)
  action = webdriver.common.action_chains.ActionChains(driver)

  exercise_repeated = None
  try:
    zeilenwiederholung_btn = wait.until(EC.presence_of_element_located(
      (By.ID, "test")
    ))
    exercise_repeated = False
    ts_xpath_id = "repeatLines_value_"
  except TimeoutException:
    zeilenwiederholung_btn = wait.until(EC.presence_of_element_located(
      (By.ID, "toggle-repeat-exercise")
    ))
    exercise_repeated = True
    ts_xpath_id = "sliding-range-repeat-exercise"
  zeilenwiederholung_btn.click()

  # Find all "ts-sliding-range" elements where id contains ts_xpath_id
  for tsr in driver.find_elements_by_xpath('//ts-sliding-range[contains(@id, "' + ts_xpath_id + '")]'):
    # Scroll to element
    driver.execute_script("arguments[0].scrollIntoView(false)", tsr)
    # Set value to 2
    driver.execute_script("arguments[0].setAttribute('value', '2')", tsr)

    # Move slider to x=80 or x=35, y=5 and click
    if exercise_repeated:
      action.move_to_element_with_offset(tsr, 35, 5)
    else:
      action.move_to_element_with_offset(tsr, 80, 5)
    action.click()
    action.perform()

  # Starte Übung
  driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

  delay = 3 # seconds
  try:
    WebDriverWait(driver, delay).until(
      EC.presence_of_element_located((By.ID, 'finish-editor')))
  except TimeoutException:
    print("Loading took too much time!")

  while driver.current_url == "%s/editor" % (url):
    line = driver.find_element_by_xpath("//div[@id='line']/input")
    editor_source_texts=driver.find_elements_by_xpath(
      "//div[@class='editor-source-text']/ts-line-display/ts-word-display")
    for editor_source_text in editor_source_texts:
        spans = editor_source_text.find_elements_by_xpath("./span")
        checked_for_pressed_key = False
        for span in spans:
            if "space" in span.get_attribute("class"):
                line.send_keys(" ")
                checked_for_pressed_key = True

        if not checked_for_pressed_key:
            line.send_keys(editor_source_text.text)
        base.time.sleep(.1 + (base.rnd.random() * base.wait_period))
    line.send_keys(Keys.ENTER)

def four3():
  url = "%s%s-%s" % (base.exercises_base_url, 4, 3)
  
  fourN(url)

def four4():
  url = "%s%s-%s" % (base.exercises_base_url, 4, 4)
  
  fourN(url)



















# def four3():
#   url = "%s%s-%s" % (base.exercises_base_url, 4, 3)
  
#   driver = base.login(url = url)
#   wait = WebDriverWait(driver, 3)
#   action = webdriver.common.action_chains.ActionChains(driver)

#   exercise_repeated = None
#   try:
#     zeilenwiederholung_btn = wait.until(EC.presence_of_element_located(
#       (By.ID, "test")
#     ))
#     exercise_repeated = False
#     ts_xpath_id = "repeatLines_value_"
#   except TimeoutException:
#     zeilenwiederholung_btn = wait.until(EC.presence_of_element_located(
#       (By.ID, "toggle-repeat-exercise")
#     ))
#     exercise_repeated = True
#     ts_xpath_id = "sliding-range-repeat-exercise"
#   zeilenwiederholung_btn.click()

#   # Find all "ts-sliding-range" elements where id contains ts_xpath_id
#   for tsr in driver.find_elements_by_xpath('//ts-sliding-range[contains(@id, "' + ts_xpath_id + '")]'):
#     # Scroll to element
#     driver.execute_script("arguments[0].scrollIntoView(false)", tsr)
#     # Set value to 2
#     driver.execute_script("arguments[0].setAttribute('value', '2')", tsr)

#     # Move slider to x=80 or x=35, y=5 and click
#     if exercise_repeated:
#       action.move_to_element_with_offset(tsr, 35, 5)
#     else:
#       action.move_to_element_with_offset(tsr, 80, 5)
#     action.click()
#     action.perform()

#   # Starte Übung
#   driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

#   delay = 3 # seconds
#   try:
#     WebDriverWait(driver, delay).until(
#       EC.presence_of_element_located((By.ID, 'finish-editor')))
#   except TimeoutException:
#     print("Loading took too much time!")

#   while driver.current_url == "%s/editor" % (url):
#     line = driver.find_element_by_xpath("//div[@id='line']/input")
#     editor_source_texts=driver.find_elements_by_xpath(
#       "//div[@class='editor-source-text']/ts-line-display/ts-word-display")
#     for editor_source_text in editor_source_texts:
#         spans = editor_source_text.find_elements_by_xpath("./span")
#         checked_for_pressed_key = False
#         for span in spans:
#             if "space" in span.get_attribute("class"):
#                 line.send_keys(" ")
#                 checked_for_pressed_key = True

#         if not checked_for_pressed_key:
#             line.send_keys(editor_source_text.text)
#         base.time.sleep(.1 + (base.rnd.random() * base.wait_period))
#     line.send_keys(Keys.ENTER)

# def four4():
#   url = "%s%s-%s" % (base.exercises_base_url, 4, 4)

#   driver = base.login(url = url)
#   wait = WebDriverWait(driver, 3)
#   action = webdriver.common.action_chains.ActionChains(driver)

#   exercise_repeated = None
#   try:
#     zeilenwiederholung_btn = wait.until(EC.presence_of_element_located(
#       (By.ID, "test")
#     ))
#     exercise_repeated = False
#     ts_xpath_id = "repeatLines_value_"
#   except TimeoutException:
#     zeilenwiederholung_btn = wait.until(EC.presence_of_element_located(
#       (By.ID, "toggle-repeat-exercise")
#     ))
#     exercise_repeated = True
#     ts_xpath_id = "sliding-range-repeat-exercise"
#   zeilenwiederholung_btn.click()

#   # Find all "ts-sliding-range" elements where id contains ts_xpath_id
#   for tsr in driver.find_elements_by_xpath('//ts-sliding-range[contains(@id, "' + ts_xpath_id + '")]'):
#     # Scroll to element
#     driver.execute_script("arguments[0].scrollIntoView(false)", tsr)
#     # Set value to 2
#     driver.execute_script("arguments[0].setAttribute('value', '2')", tsr)

#     # Move slider to x=80 or x=35, y=5 and click
#     if exercise_repeated:
#       action.move_to_element_with_offset(tsr, 35, 5)
#     else:
#       action.move_to_element_with_offset(tsr, 80, 5)
#     action.click()
#     action.perform()

#   # Starte Übung
#   driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
  
#   delay = 3 # seconds
#   try:
#     WebDriverWait(driver, delay).until(
#       EC.presence_of_element_located((By.ID, 'finish-editor')))
#   except TimeoutException:
#     print("Loading took too much time!")

#   while driver.current_url == "%s/editor" % (url):
#     line = driver.find_element_by_xpath("//div[@id='line']/input")
#     editor_source_texts = driver.find_elements_by_xpath(
#       "//div[@class='editor-source-text']/ts-line-display/ts-word-display")
#     for editor_source_text in editor_source_texts:
#       spans = editor_source_text.find_elements_by_xpath("./span")
#       checked_for_pressed_key = False
#       for span in spans:
#         if "space" in span.get_attribute("class"):
#           line.send_keys(" ")
#           checked_for_pressed_key = True

#       if not checked_for_pressed_key:
#         line.send_keys(editor_source_text.text)
#       base.time.sleep(.1 + (base.rnd.random() * base.wait_period))
#     line.send_keys(Keys.ENTER)









# def four4():
#     url = "%s%s-%s" % (base.exercises_base_url, 4, 4)

#     driver = base.login(url = url)
#     wait = WebDriverWait(driver, 10)
#     action = webdriver.common.action_chains.ActionChains(driver)

#     try:
#       zeilenwiederholung_btn = wait.until(EC.presence_of_element_located(
#         (By.ID, "test")
#       ))
#     except TimeoutException:
#       zeilenwiederholung_btn = wait.until(EC.presence_of_element_located(
#         (By.ID, "toggle-repeat-exercise")
#       ))
#     zeilenwiederholung_btn.click()

#     # Find all "ts-sliding-range" elements where id contains "repeatLines_value_"
#     for tsr in driver.find_elements_by_xpath('//ts-sliding-range[contains(@id, "repeatLines_value_")]'):
#       # Scroll to element
#       driver.execute_script("arguments[0].scrollIntoView(false)", tsr)
#       # Set value to 2
#       driver.execute_script("arguments[0].setAttribute('value', '2')", tsr)

#       # Move slider to x=80, y=0 and click
#       action.move_to_element_with_offset(tsr, 80, 5)
#       action.click()
#       action.perform()

#     # Starte Übung
#     driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
    
#     delay = 3 # seconds
#     try:
#       WebDriverWait(driver, delay).until(
#         EC.presence_of_element_located((By.ID, 'finish-editor')))
#     except TimeoutException:
#       print("Loading took too much time!")

#     while driver.current_url == "%s/editor" % (url):
#       line = driver.find_element_by_xpath("//div[@id='line']/input")
#       editor_source_texts = driver.find_elements_by_xpath(
#         "//div[@class='editor-source-text']/ts-line-display/ts-word-display")
#       for editor_source_text in editor_source_texts:
#         spans = editor_source_text.find_elements_by_xpath("./span")
#         checked_for_pressed_key = False
#         for span in spans:
#           if "space" in span.get_attribute("class"):
#             line.send_keys(" ")
#             checked_for_pressed_key = True

#         if not checked_for_pressed_key:
#           line.send_keys(editor_source_text.text)
#         base.time.sleep(.1 + (base.rnd.random() * base.wait_period))
#       line.send_keys(Keys.ENTER)


def four5():

    driver = prepare()
 
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-5')

    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Zeilenwiederholung aktivieren')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    action = webdriver.common.action_chains.ActionChains(driver)

    for n in range(4):
        repeatLines_value_0 = driver.find_element_by_xpath("//ts-sliding-range[@id='repeatLines_value_%s']/input[1]" % n)
        driver.execute_script("arguments[0].setAttribute('value', '2')", repeatLines_value_0)
        action.move_to_element_with_offset(repeatLines_value_0, 80, 5)
        action.click()
        action.perform()

    repeatLines_value_3 = driver.find_element_by_xpath("//ts-sliding-range[@id='repeatLines_value_3']/input[1]")
    driver.execute_script("arguments[0].setAttribute('value', '2')", repeatLines_value_3)
    action.move_to_element_with_offset(repeatLines_value_3, 80, 5)
    action.click()
    action.perform()

    # Starte Übung
    repeatLines_value_3.send_keys(Keys.SPACE)

    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'finish-editor')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-5/editor":
        line = driver.find_element_by_xpath("//div[@id='line']/input")
        editor_source_texts=driver.find_elements_by_xpath("//div[@class='editor-source-text']/ts-line-display/ts-word-display")
        for editor_source_text in editor_source_texts:
            spans = editor_source_text.find_elements_by_xpath("./span")
            checked_for_pressed_key = False
            for span in spans:
                if "space" in span.get_attribute("class"):
                    # line.send_keys(Keys.SPACE)
                    line.send_keys(" ")
                    checked_for_pressed_key = True

            if not checked_for_pressed_key:
                line.send_keys(editor_source_text.text)
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)

def four6():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-6')

    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Zeilenwiederholung aktivieren')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    action = webdriver.common.action_chains.ActionChains(driver)

    for n in range(2):
        repeatLines_value_0 = driver.find_element_by_xpath("//ts-sliding-range[@id='repeatLines_value_%s']/input[1]" % n)
        driver.execute_script("arguments[0].setAttribute('value', '2')", repeatLines_value_0)
        action.move_to_element_with_offset(repeatLines_value_0, 80, 5)
        action.click()
        action.perform()

    repeatLines_value_3 = driver.find_element_by_xpath("//ts-sliding-range[@id='repeatLines_value_1']/input[1]")
    driver.execute_script("arguments[0].setAttribute('value', '2')", repeatLines_value_3)
    action.move_to_element_with_offset(repeatLines_value_3, 80, 5)
    action.click()
    action.perform()

    # Starte Übung
    repeatLines_value_3.send_keys(Keys.SPACE)

    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'finish-editor')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-6/editor":
        line = driver.find_element_by_xpath("//div[@id='line']/input")
        editor_source_texts=driver.find_elements_by_xpath("//div[@class='editor-source-text']/ts-line-display/ts-word-display")
        for editor_source_text in editor_source_texts:
            spans = editor_source_text.find_elements_by_xpath("./span")
            checked_for_pressed_key = False
            for span in spans:
                if "space" in span.get_attribute("class"):
                    # line.send_keys(Keys.SPACE)
                    line.send_keys(" ")
                    checked_for_pressed_key = True

            if not checked_for_pressed_key:
                line.send_keys(editor_source_text.text)
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)

def four7():

    driver = prepare()

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-7')
    
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Zeilenwiederholung aktivieren')]/..")

    action = webdriver.common.action_chains.ActionChains(driver)

    repeatLines_value_3 = driver.find_element_by_xpath("//ts-sliding-range[@id='repeatLines_value_3']/input[1]")
    
    # Starte Übung
    repeatLines_value_3.send_keys(Keys.SPACE)

    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'finish-editor')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-7/editor":
        line = driver.find_element_by_xpath("//div[@id='line']/input")
        editor_source_texts=driver.find_elements_by_xpath("//div[@class='editor-source-text']/ts-line-display/ts-word-display")
        for editor_source_text in editor_source_texts:
            spans = editor_source_text.find_elements_by_xpath("./span")
            checked_for_pressed_key = False
            for span in spans:
                if "space" in span.get_attribute("class"):
                    # line.send_keys(Keys.SPACE)
                    line.send_keys(" ")
                    checked_for_pressed_key = True

            if not checked_for_pressed_key:
                line.send_keys(editor_source_text.text)
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)

def run(uebung):
  if uebung == 3: four3()
  elif uebung == 4: four4()
  elif uebung == 5: four5()
  elif uebung == 6: four6()
  elif uebung == 7: four7()
