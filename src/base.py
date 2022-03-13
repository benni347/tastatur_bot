# Misc imports
import json
import time
import random as rnd

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Global variables
EXERCISE_BASE_URL = "https://tastaturschreiben.verlagskv.ch/#/exercises/e/"
USERNAME = 'n/a'
PASSWORD = 'n/a'
WAIT_PERIOD = -1
DO_ALL_EXERCISES = -1

def write_to_file(log_data, file_name, open_option="w"):
    file = open(file_name, open_option)
    print(json.dumps(json.loads(log_data), indent=7))
    file.write(json.dumps(json.loads(log_data), indent=7))
    file.write("\n")
    file.close()

def load_settings():
    '''Load settings from settings.json file'''
    global USERNAME, PASSWORD, WAIT_PERIOD, DO_ALL_EXERCISES

    try:
        cfg = json.load(open('settings.json'))

    except FileNotFoundError:
        USERNAME = ''
        PASSWORD = ''
        WAIT_PERIOD = 0
        #DO_ALL_EXERCISES = 0

    else:
        USERNAME = cfg['username']
        PASSWORD = cfg['password']
        WAIT_PERIOD = cfg['wait_period']
        #DO_ALL_EXERCISES = cfg['do_all_exercises']

#def store_settings(username, password, wait_period, do_all_exercises):
def store_settings(username, password, wait_period):
    '''Store settings in settings.json file'''
    # write_to_file('{"username":"%s", "password":"%s", "wait_period":%s, "do_all_exercises":%s}' % (
    # username, password, wait_period, do_all_exercises
    write_to_file('{"username":"%s", "password":"%s", "wait_period":%s}' % (
    username, password, wait_period
  ), "settings.json")

def login(browser = "firefox", url = None):
    '''Login to site and optionally go to an URL.'''
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    # other browsers …
    driver.implicitly_wait(5) # seconds

    # Load login page
    driver.get('https://tastaturschreiben.verlagskv.ch/#/login')
    wait = WebDriverWait(driver, 10)

    # Find username and password fields and enter data
    username_tx = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    username_tx.clear()
    username_tx.send_keys(USERNAME)

    password_tx = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_tx.clear()
    password_tx.send_keys(PASSWORD)

    # Click on login button
    login_btn = driver.find_elements_by_class_name("login-button")
    login_btn[0].click()

    # Waiting for link to KONTO to be present - page has been loaded
    WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable(
          (By.LINK_TEXT, 'KONTO')
      )
    )

# Has a URL been given? If so, load it.
    if url is not None:
        driver.get(url)

    return driver
