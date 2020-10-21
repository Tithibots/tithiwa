__all__ = ["Chatroom"]

from constants import *
from waobject import WaObject
from selenium.webdriver.common.keys import Keys


class Chatroom(WaObject):
    def __init__(self, browser=None):
        super().__init__(browser)

    def open_chat_by_name_or_number(self, nameornumber):
        print(f'Opening chatroom to "{nameornumber}"', end="... ")
        self._search_and_open_chat_by_name(nameornumber)
        print(f'{STRINGS.CHECK_CHAR} Done')

    def open_chat_by_number_using_url(self, number):
        print(f'Opening chatroom to "{number}"', end="... ")
        self.browser.get("https://web.whatsapp.com/send?phone=" + number)
        self._wait_for_presence_of_an_element(SELECTORS.MAIN_SEARCH_BAR)
        print(f'{STRINGS.CHECK_CHAR} Done')

    def send_message_to_name_or_number(self, nameornumber, message):
        print(f'Sending message "{message}" to number "{nameornumber}"...', end="... ")
        self.open_chat_by_name_or_number(nameornumber)
        self._send_message(message)
        print(f'{STRINGS.CHECK_CHAR} Done')

    def send_a_message_to_multiple_chats(self, names, message):
        for name in names:
            self.send_message_to_name_or_number(name, message)

    def _open_chat_info(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM__NAME).click()

    def _close_chat_info(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM__CLOSE_INFO).click()

    def _send_message(self, message):
        self._wait_for_an_element_to_be_clickable(SELECTORS.MESSAGE_INPUT_BOX).send_keys(message + Keys.ENTER)
