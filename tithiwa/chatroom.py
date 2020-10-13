__all__ = ["Chatroom"]

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
from constants import SELECTORS
from waobject import WaObject


class Chatroom(WaObject):
    def __init__(self, browser=None):
        super().__init__(browser)

    def open_chat_by_number(self, number, wait=True):
        print(f'Opening chatroom to "{number}"', end="... ")
        self.browser.get("https://web.whatsapp.com/send?phone=" + number)
        if wait:
            self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
        print('✔ Done')

    def send_message_to_number(self, number, message):
        self.open_chat_by_number(number)
        print(f'Sending message "{message}" to number "{number}"...', end="... ")
        inputbox = self._wait_for_an_element_to_be_clickable(SELECTORS.MESSAGE_INPUT_BOX)
        inputbox.send_keys(message + Keys.ENTER)
        print('✔ Done')
