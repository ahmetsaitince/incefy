from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

def browserCreator():
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #browser = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=chrome_options)
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    return browser

browser = browserCreator()

browser.get('https://malatyapazaripalanci.com.tr')

