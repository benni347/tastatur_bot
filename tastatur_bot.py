from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random as rnd

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
    # wait = WebDriverWait(driver, 10)

    # driver.implicitly_wait(10) # seconds
    print("vor aufruf url\n")
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-3')
    print("NACH aufruf url\n")
    driver.implicitly_wait(10) # seconds

    # zeilenwiederholung_btn = driver.find_element_by_id("ts-sliding-toggle-3")
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'repeatExercise')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    # repeatLines_value_0 = driver.find_element_by_id("repeatLines_value_0")

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
    # wait = WebDriverWait(driver, 10)

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-4')

    # zeilenwiederholung_btn = driver.find_element_by_id("ts-sliding-toggle-3")
    
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Zeilenwiederholung aktivieren')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    # repeatLines_value_0 = driver.find_element_by_id("repeatLines_value_0")

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
    # wait = WebDriverWait(driver, 10)

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-5')

    # zeilenwiederholung_btn = driver.find_element_by_id("ts-sliding-toggle-3")
    
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Zeilenwiederholung aktivieren')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    # repeatLines_value_0 = driver.find_element_by_id("repeatLines_value_0")

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
    # wait = WebDriverWait(driver, 10)

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-6')

    # zeilenwiederholung_btn = driver.find_element_by_id("ts-sliding-toggle-3")
    
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Zeilenwiederholung aktivieren')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    # repeatLines_value_0 = driver.find_element_by_id("repeatLines_value_0")

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
    # wait = WebDriverWait(driver, 10)

    driver.implicitly_wait(4) # seconds
    driver.get('https://tastaturschreiben.verlagskv.ch/#/exercises/e/4-7')

    # zeilenwiederholung_btn = driver.find_element_by_id("ts-sliding-toggle-3")
    
    zeilenwiederholung_label = driver.find_element_by_xpath("//label[contains(text(), 'Zeilenwiederholung aktivieren')]/..")
    zeilenwiederholung_btn = zeilenwiederholung_label.find_element_by_xpath("./ts-sliding-toggle/input[1]")
    zeilenwiederholung_btn.click()

    # repeatLines_value_0 = driver.find_element_by_id("repeatLines_value_0")

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

def drawWindow():
    window = Tk()

    window.title("Übungen")
    window.geometry('650x500')

    tab_parent = ttk.Notebook(window)

    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)

    tab_parent.add(tab1, text="4")
    tab_parent.add(tab2, text="5")

    # === WIDGETS FOR TAB ONE
    btnFour3 = tk.Button(tab1, text="4-3", command=four3)
    btnFour4 = tk.Button(tab1, text="4-4", command=four4)
    btnFour5 = tk.Button(tab1, text="4-5", command=four5)
    btnFour6 = tk.Button(tab1, text="4-6", command=four6)
    btnFour7 = tk.Button(tab1, text="4-7", command=four7)

    imgLabelTabOne = tk.Label(tab1)

    buttonForward = tk.Button(tab1, text="Forward")
    buttonBack = tk.Button(tab1, text="Back")

    # === ADD WIDGETS TO GRID ON TAB ONE
    btnFour3.grid(row=0, column=0, padx=15, pady=15)
    btnFour4.grid(row=1, column=0, padx=15, pady=15)
    btnFour5.grid(row=2, column=0, padx=15, pady=15)
    btnFour6.grid(row=3, column=0, padx=15, pady=15)
    btnFour7.grid(row=4, column=0, padx=15, pady=15)

    tab_parent.pack(expand=1, fill='both')

    window.mainloop()

drawWindow()
