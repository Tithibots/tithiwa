__all__ = ["WaObject"]

from selenium import webdriver
from constants import SELECTORS
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaObject:
    def __init__(self, browser=None):
        self.browser = browser
        self.browser = self._open_browser_if_not_opened()
        self._open_whatsapp_if_not_opened()
        # self._wait_for_web_whatsapp_to_load()

    def quit(self):
        self.browser.quit()

    def _close_info(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.CLOSE_INFO).click()

    def _open_browser_if_not_opened(self):
        if self.browser == None:
            self.browser = webdriver.Chrome()
        return self.browser

    def _open_whatsapp_if_not_opened(self):
        if self.browser.current_url.find("web.whatsapp") == -1:
            self.browser.get("https://web.whatsapp.com/")

    def _wait_for_web_whatsapp_to_load(self):
        self._wait_for_presence_of_an_element(SELECTORS.TURN_ON_DESKTOP_NOTIFICATIONS)

    def _wait_for_presence_of_an_element(self, selector):
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
                element.is_displayed()
            except:
                break
            finally:
                pass

    def _race_for_presence_of_two_elements(self, selector1, selector2):
        selector1orselector2 = selector1 + ", " + selector2
        winnerelement = self._wait_for_presence_of_an_element(selector1orselector2)
        element1 = None
        try:
            element1 = self.browser.find_element(By.CSS_SELECTOR, selector1)
        except:
            pass
        element2 = None
        try:
            element2 = self.browser.find_element(By.CSS_SELECTOR, selector2)
        except:
            pass
        if winnerelement == element1:
            return winnerelement, 0
        elif winnerelement == element2:
            return winnerelement, 1
        else:
            return None, -1

    def _search_and_open_chat_by_name(self, name):
        isfound = False
        self._search_and_wait_for_complete(name)
        preactive = None
        curractive = self.browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            if curractive == preactive:
                break
            name = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS__CONTACTS_SEARCH_NAME).get_attribute(
                'innerText')
            if name == name:
                isfound = True
                break
            preactive = curractive
        self._wait_for_chat_to_open(name)
        return isfound

    def _search_and_open_chat_by_number(self, number):
        self._search_and_wait_for_complete(number)
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        self.browser.switch_to.active_element.click()

    def _wait_for_chat_to_open(self, name):
        nameofchat = ''
        while True:
            try:
                nameofchat = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__NAME).get_attribute(
                    'innerText')
            except:
                pass
            if nameofchat == name:
                break

    def _search_and_wait_for_complete(self, nameornumber):
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR_SEARCH_ICON).click()
        self.browser.switch_to.active_element.send_keys(nameornumber)
        self._wait_for_presence_of_an_element(SELECTORS.MAIN_SEARCH_BAR_DONE)
