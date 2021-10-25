__all__ = ["Tithiwa"]

from .session import Session
from .settings import Settings
from .group import Group
from .contact import Contact
from time import sleep
from .constants import *
from selenium.webdriver.common.keys import Keys

class Tithiwa(Session, Settings, Group, Contact):
    def __init__(self, browser=None):
        super().__init__(browser)

    def clear_all_chats(self):
        self._wait_for_presence_of_an_element(SELECTORS.GROUPS__NAME_IN_CHATS)
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
        preactive = None
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        curractive = self.browser.switch_to.active_element
        pregroupname = None
        while curractive != preactive:
            sleep(0.5)
            self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[3]/div/div[2]/div/div/span").click()
            for i in range(3):
                self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
            self.browser.switch_to.active_element.send_keys(Keys.ENTER)
            self._wait_for_presence_of_an_element(SELECTORS.OVERLAY)
            self._wait_for_an_element_to_be_clickable(SELECTORS.OVERLAY_OK).click()      
            
            preactive = curractive
            pregroupname = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__NAME)
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element


    # def __del__(self):
    #     self.browser.quit()
