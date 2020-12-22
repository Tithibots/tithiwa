__all__ = ["Contact"]

from .chatroom import Chatroom
from .constants import *
from .waobject import WaObject

class Contact(Chatroom, WaObject):

    def __init__(self, browser=None):
        super().__init__(browser)

    def get_mobile_number_of(self, nameornumber, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Getting mobile number of "{nameornumber}"...')
        self.open_chat_to(nameornumber, _shouldoutput=(True, False))
        self._open_chat_info()
        number = self._wait_for_mobile_number_to_appear()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')
        return number

    def _wait_for_mobile_number_to_appear(self):
        number = ''
        while number == '':
            number = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__INFO_NUMBER).text
            continue
        return number

    def delete_chats_of_all_contacts(self, _shouldoutput=(True, True)):
        self._wait_for_presence_of_an_element(SELECTORS.CONTACTS__NAME_IN_CHATS)
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
        preactive = None
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        curractive = self.browser.switch_to.active_element
        prechatname = None
        while curractive != preactive:
            chatnameelement = None
            try:
                chatnameelement = curractive.find_element(By.CSS_SELECTOR, SELECTORS.CONTACTS__NAME_IN_CHATS)
            except:
                pass
            if chatnameelement != None:
                chatname = chatnameelement.get_attribute('innerText')
                self._wait_for_an_element_to_deattached(prechatname)
                self._wait_for_chat_to_open(chatname)
            preactive = curractive
            prechatname = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__NAME)
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
        # wait for options element to be available then click
        self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__OPTIONS)
        self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM__OPTIONS).click()
        # wait for delete element to be available then click
        self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__INFO_DELETE_CHAT)
        self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM__INFO_DELETE_CHAT).click()
        # wait for pop up to delete chat to be available then click
        self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__DELETE_CHAT)
        self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM__DELETE_CHAT).click()
        self._close_info()
        