from tkinter import messagebox

import ../src/base

# Selenium imports
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def exerciseN(le, uebung):

  url = "%s%s-%s" % (base.EXERCISE_BASE_URL, le, uebung)

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
        base.time.sleep(.1 + (base.rnd.random() * base.WAIT_PERIOD))
    line.send_keys(Keys.ENTER)

def run(le, uebung):
  exerciseN(le, uebung)
