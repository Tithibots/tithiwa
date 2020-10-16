__all__ = ["WaObject"]

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

    def _handle_new_browser_init(self, browser):
        self.intitbrowser = self.browser
        if browser != None:
            self.browser = browser

    def _handle_new_browser_del(self):
        self.browser = self.intitbrowser

    def quit(self):
        self.browser.quit()

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

    def _wait_for_an_element_to_deattached(self, element):
        while True:
            try:
                element.find_element()
            except:
                break
            finally:
                pass
