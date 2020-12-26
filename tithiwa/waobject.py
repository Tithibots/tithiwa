__all__ = ["WaObject"]

from time import sleep

from selenium import webdriver
from .constants import *
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

    def quit(self, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Quiting tithiwa', end="...")
        self.browser.quit()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

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
            element = WebDriverWait(self.browser, INTEGERS.DEFAULT_WAIT).until(
                EC.presence_of_element_located(selector)
            )
        except:
            pass
        finally:
            return element

    def _wait_for_presence_of_all_elements(self, selector):
        elements = None
        try:
            elements = WebDriverWait(self.browser, INTEGERS.DEFAULT_WAIT).until(
                EC.presence_of_all_elements_located(selector)
            )
        except:
            pass
        finally:
            return elements

    def _wait_for_presence_of_an_element_in_other_element(self, selector, element):
        relement = None
        while True:
            try:
                relement = element.find_element(*selector)
            except:
                continue
            return relement

    def _wait_for_presence_of_an_element_in_active_element(self, selector):
        relement = None
        while True:
            try:
                curractive = self.browser.switch_to.active_element
                relement = curractive.find_element(*selector)
                sleep(0.5)
            except:
                continue
            return relement

    def _wait_for_an_element_to_be_clickable(self, selector):
        element = None
        try:
            element = WebDriverWait(self.browser, INTEGERS.DEFAULT_WAIT).until(
                EC.element_to_be_clickable(selector)
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
            element1 = self.browser.find_element(*selector1)
        except:
            pass
        element2 = None
        try:
            element2 = self.browser.find_element(*selector2)
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
            curr_name = curractive.find_element(*SELECTORS.MAIN_SEARCH_BAR__RESULT_NAMES).get_attribute('innerText')
            if curr_name == name:
                isfound = True
                break
            preactive = curractive
        self._wait_for_chat_to_open(name)
        self._wait_for_presence_of_an_element(SELECTORS.MAIN_SEARCH_BAR__BACK_ARROW).click()
        return isfound

    def _search_and_open_chat_by_number(self, number):
        self._search_and_wait_for_complete(number)
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        self.browser.switch_to.active_element.click()
        self._wait_for_presence_of_an_element(SELECTORS.MAIN_SEARCH_BAR__BACK_ARROW).click()

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
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR__SEARCH_ICON).click()
        self.browser.switch_to.active_element.send_keys(nameornumber)
        self._wait_for_presence_of_an_element(SELECTORS.MAIN_SEARCH_BAR__DONE)

    def _press_back_button(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.BACK_BUTTON).click()

    def _wait_until_innerText_is_empty_of_an_element(self, element):
        text = element.get_attribute('innerText')
        while text == '':
            text = element.get_attribute('innerText')
        return text

    def _open_about(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS__MENU_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS__PROFILE).click()

    def _wait_for_attribute_change(self, selector, attribute, previous_value=None):
        class _wait_for_attribute_change_class(object):
            def __init__(self):
                self.pre_value = previous_value

            def __call__(self, driver):
                try:
                    element_attribute = EC._find_element(driver, selector).get_attribute(attribute)
                    if self.pre_value is None:
                        self.pre_value = element_attribute
                    return element_attribute != self.pre_value
                except:
                    return False

        WebDriverWait(self.browser, INTEGERS.DEFAULT_WAIT).until(_wait_for_attribute_change_class())

    def get_my_about(self):
        self._open_about()
        about = self._wait_until_innerText_is_empty_of_an_element(
            self._wait_for_presence_of_all_elements(SELECTORS.NAME_AND_ABOUT)[1])
        self._press_back_button()
        return about

    def get_my_name(self):
        self._open_about()
        name = self._wait_until_innerText_is_empty_of_an_element(
            self._wait_for_presence_of_all_elements(SELECTORS.NAME_AND_ABOUT)[0])
        self._press_back_button()
        return name
