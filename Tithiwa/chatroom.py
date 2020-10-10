from selenium import webdriver
from time import sleep
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import *


class Chatroom:
    def __init__(self, browser=None):
        self.browser = open_browser_if_not_opened(browser)
        open_whatsapp_if_not_opened(self.browser)

    def open_chat_by_number(self, number, browser=None, wait=True):
        if browser == None:
            browser = self.browser
        browser.get("https://web.whatsapp.com/send?phone=" + number)
        if wait:
            try:
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, '_3FRCZ'))
                )
            finally:
                return browser
        else:
            return browser

    def send_message_to_number(self, number, message, browser=None):
        if browser == None:
            browser = self.browser
        browser = self.open_chat_by_number(number, browser=browser)
        print(f'Sending message "{message}" to number "{number}"...')
        inputbox = browser.find_element_by_css_selector("#main footer ._3FRCZ")
        inputbox.send_keys(message + Keys.ENTER)
        return browser
