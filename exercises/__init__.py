from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random as rnd

import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser

import json

cfg = json.load(open('tastatur_bot.json'))

username = cfg['username']
password = cfg['password']

def prepare():
    
    driver = webdriver.Firefox()
    driver.get('https://tastaturschreiben.verlagskv.ch/#/login')
    driver.implicitly_wait(10) # seconds

    username_tx = driver.find_element_by_id("username")
    password_tx = driver.find_element_by_id("password")

    username_tx.clear()
    username_tx.send_keys(username)
    
    password_tx.clear()
    password_tx.send_keys(password)
    
    login_btn = driver.find_elements_by_class_name("login-button")
    login_btn[0].click()

    return driver

def four3():
    
    driver = prepare()
 

    # driver.implicitly_wait(10) # seconds
    print("vor aufruf url\n")
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-3')
    print("NACH aufruf url\n")
    driver.implicitly_wait(10) # seconds

    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'repeatExercise')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    action = webdriver.common.action_chains.ActionChains(driver)

    repeatLines_value_3 = driver.find_element_by_xpath("//ts-sliding-range[@id='sliding-range-repeat-exercise']/input[1]")
    driver.execute_script("arguments[0].setAttribute('value', '2')", repeatLines_value_3)
    action.move_to_element_with_offset(repeatLines_value_3, 35, 5)
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

    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-3/editor":
        line = driver.find_element_by_xpath("//div[@id='line']/input")
        editor_source_texts=driver.find_elements_by_xpath("//div[@class='editor-source-text']/ts-line-display/ts-word-display")
        for editor_source_text in editor_source_texts:
            spans = editor_source_text.find_elements_by_xpath("./span")
            checked_for_pressed_key = False
            for span in spans:
                print("span:")
                print(span)
                if "space" in span.get_attribute("class"):
                    # line.send_keys(Keys.SPACE)
                    line.send_keys(" ")
                    checked_for_pressed_key = True
                    print("space found")

            if not checked_for_pressed_key:
                print(editor_source_text.text)
                print("class:\n\r" + editor_source_text.get_attribute("class") + "\n\r****************\n\r")
                line.send_keys(editor_source_text.text)
            time.sleep(.4)
        line.send_keys(Keys.ENTER)

def four4():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-4')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-4/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

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
            time.sleep(.35 + (rnd.random() * 0.25))
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
            time.sleep(.35 + (rnd.random() * 0.25))
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def five0():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-0')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-0/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def five1():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-1')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-1/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def five2():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-2')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-2/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def five3():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-3')
    
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Übungswiederholung')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    action = webdriver.common.action_chains.ActionChains(driver)

    repeatLines_value_3 = driver.find_element_by_xpath("//ts-sliding-range[@id='sliding-range-repeat-exercise']/input[1]")
    driver.execute_script("arguments[0].setAttribute('value', '2')", repeatLines_value_3)
    action.move_to_element_with_offset(repeatLines_value_3, 32, 5)
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-3/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def five4():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-4')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-4/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def five5():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-5')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-5/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def five6():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-6')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-6/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def five7():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-7')

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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-7/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def six0():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-0')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-0/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def six1():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-1')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-1/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def six2():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-2')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-2/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def six3():

    driver = prepare()

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/5-3')
    
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Übungswiederholung')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    action = webdriver.common.action_chains.ActionChains(driver)

    repeatLines_value_3 = driver.find_element_by_xpath("//ts-sliding-range[@id='sliding-range-repeat-exercise']/input[1]")
    driver.execute_script("arguments[0].setAttribute('value', '2')", repeatLines_value_3)
    action.move_to_element_with_offset(repeatLines_value_3, 32, 5)
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-3/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def six4():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-4')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-4/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def six5():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-5')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-5/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def six6():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-6')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-6/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def six7():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-7')

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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/6-7/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven0():

    driver = prepare()

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-0')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-0/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven1():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-1')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-1/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven2():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-2')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-2/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven3():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-3')
    
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Übungswiederholung')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    action = webdriver.common.action_chains.ActionChains(driver)

    repeatLines_value_3 = driver.find_element_by_xpath("//ts-sliding-range[@id='sliding-range-repeat-exercise']/input[1]")
    driver.execute_script("arguments[0].setAttribute('value', '2')", repeatLines_value_3)
    action.move_to_element_with_offset(repeatLines_value_3, 32, 5)
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-3/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven4():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-4')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-4/editor":
        line = driver.find_element_by_xpath("//div[@id='line']/input")
        editor_source_texts=driver.find_elements_by_xpath("//div[@class='editor-source-text']/ts-line-display/ts-word-display")
        for editor_source_text in editor_source_texts:
            spans = editor_source_text.find_elements_by_xpath("./span")
            checked_for_pressed_key = False
            for span in spans:
                if "space" in span.get_attribute("class"):
                    line.send_keys(" ")
                    checked_for_pressed_key = True

            if not checked_for_pressed_key:
                line.send_keys(editor_source_text.text)
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven5():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-5')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-5/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven6():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-6')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-6/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven7():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-7')

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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-7/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def seven8():

    driver = prepare()
 

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-8')

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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/7-8/editor":
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
            time.sleep(.35 + (rnd.random() * 0.25))
        line.send_keys(Keys.ENTER)

def drawWindow():
    window = Tk()

    window.title("Übungen")
    window.geometry('650x500')

    tab_parent = ttk.Notebook(window)
    
    tab_list = [
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent)
    ]
    
    new = 1
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    def openweb():
     webbrowser.open(url,new=new)
    
    title = 4
    for tab in tab_list:
      tab_parent.add(tab, text="{0}".format(title))
      BtnHelp = tk.Button(tab, text = "Help", command=openweb)
      BtnHelp.grid(row=5, column=6, padx=15, pady=15)
      title = title+1

    # === WIDGETS FOR TAB ONE
    btnFour3 = tk.Button(tab_list[0], text="4-3", command=four3)
    btnFour4 = tk.Button(tab_list[0], text="4-4", command=four4)
    btnFour5 = tk.Button(tab_list[0], text="4-5", command=four5)
    btnFour6 = tk.Button(tab_list[0], text="4-6", command=four6)
    btnFour7 = tk.Button(tab_list[0], text="4-7", command=four7)

    # === WIDGETS FOR TAB TWO
    btnFive0 = tk.Button(tab_list[1], text="5-0", command=five0)
    btnFive1 = tk.Button(tab_list[1], text="5-1", command=five1)
    btnFive2 = tk.Button(tab_list[1], text="5-2", command=five2)
    btnFive3 = tk.Button(tab_list[1], text="5-3", command=five3)
    btnFive4 = tk.Button(tab_list[1], text="5-4", command=five4)
    btnFive5 = tk.Button(tab_list[1], text="5-5", command=five5)
    btnFive6 = tk.Button(tab_list[1], text="5-6", command=five6)
    btnFive7 = tk.Button(tab_list[1], text="5-7", command=five7)

    # === WIDGETS FOR TAB THREE
    btnSix0 = tk.Button(tab_list[2], text="6-0", command=six0)
    btnSix1 = tk.Button(tab_list[2], text="6-1", command=six1)
    btnSix2 = tk.Button(tab_list[2], text="6-2", command=six2)
    btnSix3 = tk.Button(tab_list[2], text="6-3", command=six3)
    btnSix4 = tk.Button(tab_list[2], text="6-4", command=six4)
    btnSix5 = tk.Button(tab_list[2], text="6-5", command=six5)
    btnSix6 = tk.Button(tab_list[2], text="6-6", command=six6)
    btnSix7 = tk.Button(tab_list[2], text="6-7", command=six7)

    # === WIDGETS FOR TAB FOUR
    btnSeven0 = tk.Button(tab_list[3], text="7-0", command=seven0)
    btnSeven1 = tk.Button(tab_list[3], text="7-1", command=seven1)
    btnSeven2 = tk.Button(tab_list[3], text="7-2", command=seven2)
    btnSeven3 = tk.Button(tab_list[3], text="7-3", command=seven3)
    btnSeven4 = tk.Button(tab_list[3], text="7-4", command=seven4)
    btnSeven5 = tk.Button(tab_list[3], text="7-5", command=seven5)
    btnSeven6 = tk.Button(tab_list[3], text="7-6", command=seven6)
    btnSeven7 = tk.Button(tab_list[3], text="7-7", command=seven7)
    btnSeven8 = tk.Button(tab_list[3], text="7-8", command=seven8)

    imgLabelTabOne = tk.Label(tab_list[0])

    buttonForward = tk.Button(tab_list[0], text="Forward")
    buttonBack = tk.Button(tab_list[0], text="Back")

    # === ADD WIDGETS TO GRID ON TAB ONE
    btnFour3.grid(row=0, column=0, padx=15, pady=15)
    btnFour4.grid(row=1, column=0, padx=15, pady=15)
    btnFour5.grid(row=2, column=0, padx=15, pady=15)
    btnFour6.grid(row=3, column=0, padx=15, pady=15)
    btnFour7.grid(row=4, column=0, padx=15, pady=15)
    
    # === ADD WIDGETS TO GRID ON TAB TWO
    btnFive0.grid(row=0, column=0, padx=15, pady=15)
    btnFive1.grid(row=1, column=0, padx=15, pady=15)
    btnFive2.grid(row=2, column=0, padx=15, pady=15)
    btnFive3.grid(row=3, column=0, padx=15, pady=15)
    btnFive4.grid(row=4, column=0, padx=15, pady=15)
    btnFive5.grid(row=5, column=0, padx=15, pady=15)
    btnFive6.grid(row=6, column=0, padx=15, pady=15)
    btnFive7.grid(row=7, column=0, padx=15, pady=15)
    
    # === ADD WIDGETS TO GRID ON TAB THREE
    btnSix0.grid(row=0, column=0, padx=15, pady=15)
    btnSix1.grid(row=1, column=0, padx=15, pady=15)
    btnSix2.grid(row=2, column=0, padx=15, pady=15)
    btnSix3.grid(row=3, column=0, padx=15, pady=15)
    btnSix4.grid(row=4, column=0, padx=15, pady=15)
    btnSix5.grid(row=5, column=0, padx=15, pady=15)
    btnSix6.grid(row=6, column=0, padx=15, pady=15)
    btnSix7.grid(row=7, column=0, padx=15, pady=15)
    
    # === ADD WIDGETS TO GRID ON TAB FOUR
    btnSeven0.grid(row=0, column=0, padx=15, pady=15)
    btnSeven1.grid(row=1, column=0, padx=15, pady=15)
    btnSeven2.grid(row=2, column=0, padx=15, pady=15)
    btnSeven3.grid(row=3, column=0, padx=15, pady=15)
    btnSeven4.grid(row=4, column=0, padx=15, pady=15)
    btnSeven5.grid(row=5, column=0, padx=15, pady=15)
    btnSeven6.grid(row=6, column=0, padx=15, pady=15)
    btnSeven7.grid(row=7, column=0, padx=15, pady=15)
    btnSeven8.grid(row=0, column=2, padx=15, pady=15)

    tab_parent.pack(expand=1, fill='both')

    window.mainloop()
