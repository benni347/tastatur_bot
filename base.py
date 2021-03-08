# Misc imports
import time
import random as rnd
import json
import webbrowser

# Selenium imports
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Global variables
exercises_base_url = "https://tastaturschreiben.verlagskv.ch/#/exercises/e/"
username = 'n/a'
password = 'n/a'
wait_period = -1

def writeToFile(logData, fileName, openOption="w"):
    file = open(fileName, openOption)
    file.write(json.dumps(json.loads(logData), indent=7)) 
    file.write("\n")
    file.close()  

def loadSettings():
  '''Load settings from settings.json file'''
  global username, password, wait_period

  try:
    cfg = json.load(open('settings.json'))
  except FileNotFoundError:
    username = ''
    password = ''
    wait_period = 0
  else:
    username = cfg['username']
    password = cfg['password']
    wait_period = cfg['wait_period']

def storeSettings(username, password, wait_period):
  '''Store settings in settings.json file'''
  writeToFile('{"username":"%s", "password":"%s", "wait_period":%s}' % (
    username, password, wait_period
  ), "settings.json")

def login(browser = "firefox", url = None):
  '''Login to site and optionally go to an URL.'''
  if browser == "firefox":
    # fxprofile = FirefoxProfile()
    # fxprofile.set_preference("layout.css.devPixelsPerPx", "0.49")
    # driver = webdriver.Firefox(firefox_profile=fxprofile)
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
  username_tx.send_keys(username)

  password_tx = wait.until(EC.presence_of_element_located((By.ID, 'password')))
  password_tx.clear()
  password_tx.send_keys(password)
  
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
