from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
import os
import platform
import subprocess


class WaObject:
    def __init__(self, browser=None):
        self.browser = browser
        self.browser = self._open_browser_if_not_opened()
        self._open_whatsapp_if_not_opened()

    # def _handle_new_browser(self, browser):
    #     self.shouldreturnbrowser = False
    #     if browser == None:
    #         self.shouldreturnbrowser = True
    #         return self.browser
    #     else:
    #         return browser
    #
    # def _return_browser_if_new(self, browser):
    #     if self.shouldreturnbrowser:
    #         return browser


    def _open_browser_if_not_opened(self):
        if self.browser == None:
            self.browser = webdriver.Chrome()
        return self.browser

    def _open_whatsapp_if_not_opened(self):
        if self.browser.current_url.find("web.whatsapp") == -1:
            self.browser.get("https://web.whatsapp.com/")

    def _wait_for_an_presence_of_element(self, selector):
        element = None
        try:
            element = WebDriverWait(self.browser, 34).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
        except:
            pass
        finally:
            return element

    def _wait_for_presence_of_an_element_in_other_element(self, selector, element):
        relement = None
        while True:
            try:
                relement = element.find_element(By.CSS_SELECTOR, selector)
            except:
                pass
            finally:
                return relement

    def _wait_for_an_element_to_be_clickable(self, selector):
        element = None
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )
        except:
            pass
        finally:
            return element
