import time
import random as rnd

import json

import webbrowser

import tkinter as tk
from tkinter import *
from tkinter import ttk

import keyboard

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

wait_period = 0

try:
    cfg = json.load(open('login.json'))
except FileNotFoundError:
    username = ''
    password = ''
else:
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)
    delay = 3 # seconds


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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
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
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)


def seven5():

    driver = prepare()
 
    time.sleep(3)
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
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)

def seven6():

    driver = prepare()
 
    time.sleep(3)
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
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)

    

def seven7():

    driver = prepare()
 
    time.sleep(3)
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
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)

    

def seven8():

    driver = prepare()
 
    time.sleep(3)
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
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)

def eight0():

    driver = prepare()
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-0')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-0/editor":
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


def eight1():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-1')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-1/editor":
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
    delay = 3 # seconds


def eight2():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-2')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-2/editor":
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


def eight3():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-3')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-3/editor":
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


def eight4():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-4')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-4/editor":
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
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)


def eight5():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-5')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-5/editor":
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

def eight6():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-6')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-6/editor":
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

    

def eight7():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-7')

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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-7/editor":
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

    

def eight8():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-8')

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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/8-8/editor":
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

def nine0():

    driver = prepare()
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-0')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-0/editor":
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


def nine1():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-1')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-1/editor":
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
    delay = 3 # seconds


def nine2():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-2')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-2/editor":
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


def nine3():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-3')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-3/editor":
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


def nine4():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-4')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-4/editor":
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
            time.sleep(.1 + (rnd.random() * wait_period))
        line.send_keys(Keys.ENTER)


def nine5():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-5')
    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-5/editor":
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

def nine6():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-6')


    
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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-6/editor":
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

    

def nine7():

    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-7')

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


    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-7/editor":
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

def nine8():
    driver = prepare()
 
    time.sleep(3)
    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-8')

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

    while driver.current_url == "https://tastaturschreiben.verlagskv.ch/#/exercises/e/9-8/editor":
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

def writeToFile(logData, fileName, openOption="w"):
    file = open(fileName, openOption)
    file.write(json.dumps(json.loads(logData), indent=4)) 
    file.write("\n")
    file.close()  

def storeLoginData(val1, val2):
    writeToFile('{"username":"' + val1 + '", "password":"' + val2 + '"}', "login.json")

def recordWaitPeriod(waitPeriod):
    global wait_period
    wait_period = float(waitPeriod)

def drawWindow():
    window = Tk()

    window.title("Exercises")
    window.geometry('950x500')

    tab_parent = ttk.Notebook(window)
    
    tab_list = [
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent),
      ttk.Frame(tab_parent)
    ]

    tab_list_settings = [
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
      BtnHelp.grid(row=5, column=8, padx=15, pady=15)
      title = title+1
      
    titleSettings = "Settings"
    for tab in tab_list_settings:
      tab_parent.add(tab, text="Settings")
      
    mail = tk.Label(tab_list_settings[0], text="E-Mail")
    password = tk.Label(tab_list_settings[0], text="Password")
    entry_1 = tk.Entry(tab_list_settings[0])
    entry_2 = tk.Entry(tab_list_settings[0])
    submit = tk.Button(tab_list_settings[0], text="Enter", command=lambda: storeLoginData(entry_1.get(), entry_2.get()))
    time_scale = tk.Scale(tab_list_settings[0], from_=0.1, to=1.0, resolution=0.01, length=600, orient=HORIZONTAL, command=recordWaitPeriod)

    # === WIDGETS FOR TAB ONE
    btn_dict = {
      4: [  # === WIDGETS FOR TAB ONE
        tk.Button(tab_list[0], text="4-3", command=four3),
        tk.Button(tab_list[0], text="4-4", command=four4),
        tk.Button(tab_list[0], text="4-5", command=four5),
        tk.Button(tab_list[0], text="4-6", command=four6),
        tk.Button(tab_list[0], text="4-7", command=four7)
      ],
      5: [  # === WIDGETS FOR TAB TWO
        tk.Button(tab_list[1], text="5-0", command=five0),
        tk.Button(tab_list[1], text="5-1", command=five1),
        tk.Button(tab_list[1], text="5-2", command=five2),
        tk.Button(tab_list[1], text="5-3", command=five3),
        tk.Button(tab_list[1], text="5-4", command=five4),
        tk.Button(tab_list[1], text="5-5", command=five5),
        tk.Button(tab_list[1], text="5-6", command=five6),
        tk.Button(tab_list[1], text="5-7", command=five7)
      ],
      6: [  # === WIDGETS FOR TAB THREE
        tk.Button(tab_list[2], text="6-0", command=six0),
        tk.Button(tab_list[2], text="6-1", command=six1),
        tk.Button(tab_list[2], text="6-2", command=six2),
        tk.Button(tab_list[2], text="6-3", command=six3),
        tk.Button(tab_list[2], text="6-4", command=six4),
        tk.Button(tab_list[2], text="6-5", command=six5),
        tk.Button(tab_list[2], text="6-6", command=six6),
        tk.Button(tab_list[2], text="6-7", command=six7)
      ],
      7: [  # === WIDGETS FOR TAB FOUR
        tk.Button(tab_list[3], text="7-0", command=seven0),
        tk.Button(tab_list[3], text="7-1", command=seven1),
        tk.Button(tab_list[3], text="7-2", command=seven2),
        tk.Button(tab_list[3], text="7-3", command=seven3),
        tk.Button(tab_list[3], text="7-4", command=seven4),
        tk.Button(tab_list[3], text="7-5", command=seven5),
        tk.Button(tab_list[3], text="7-6", command=seven6),
        tk.Button(tab_list[3], text="7-7", command=seven7),
        tk.Button(tab_list[3], text="7-8", command=seven8)
      ],
      8: [  # === WIDGETS FOR TAB FIVE
        tk.Button(tab_list[4], text="8-0", command=eight0),
        tk.Button(tab_list[4], text="8-1", command=eight1),
        tk.Button(tab_list[4], text="8-2", command=eight2),
        tk.Button(tab_list[4], text="8-3", command=eight3),
        tk.Button(tab_list[4], text="8-4", command=eight4),
        tk.Button(tab_list[4], text="8-5", command=eight5),
        tk.Button(tab_list[4], text="8-6", command=eight6),
        tk.Button(tab_list[4], text="8-7", command=eight7),
        tk.Button(tab_list[4], text="8-8", command=eight8)
      ],
      9: [  # === WIDGETS FOR TAB SIX
        tk.Button(tab_list[5], text="9-0", command=nine0),
        tk.Button(tab_list[5], text="9-1", command=nine1),
        tk.Button(tab_list[5], text="9-2", command=nine2),
        tk.Button(tab_list[5], text="9-3", command=nine3),
        tk.Button(tab_list[5], text="9-4", command=nine4),
        tk.Button(tab_list[5], text="9-5", command=nine5),
        tk.Button(tab_list[5], text="9-6", command=nine6),
        tk.Button(tab_list[5], text="9-7", command=nine7),
        tk.Button(tab_list[5], text="9-8", command=nine8)
      ],
      titleSettings: [  # === WIDGETS FOR SETTINGS
        mail,
        password,
        entry_1,
        entry_2,
        submit,
        time_scale
      ]
    }

    # === ADD WIDGETS TO GRID ON TABS
    row = 0
    col = -1
    for exc in btn_dict:
      for btn in btn_dict[exc]:
        if (row%8) == 0:
          col = col + 1
        row = (row%8) + 1
        btn.grid(row=row, column=col, padx=15, pady=15)
      row=0
    mail.grid(row=0, column=0)
    password.grid(row=1, column=0)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    submit.grid(row=1)
    time_scale.grid(row=3, column=0)

    tab_parent.pack(expand=1, fill='both')

    window.mainloop()
