__all__ = ["Contact"]

from chatroom import Chatroom
from constants import SELECTORS


class Contact(Chatroom):

    def __init__(self, browser=None):
        super().__init__(browser)

    def open_chat_by_number(self, number):
        print(f'Opening chatroom to "{number}"', end="... ")
        self._search_and_open_chat_by_name(number)
        print('✔ Done')

    def open_chat_by_number_using_url(self, number, wait=True):
        print(f'Opening chatroom to "{number}"', end="... ")
        self.browser.get("https://web.whatsapp.com/send?phone=" + number)
        if wait:
            self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
        print('✔ Done')

    def open_chat_by_name(self, name):
        print(f'Opening chatroom to "{name}"', end="... ")
        self._search_and_open_chat_by_name(name)
        print('✔ Done')

    def send_message_to_number(self, number, message):
        print(f'Sending message "{message}" to number "{number}"...', end="... ")
        self.open_chat_by_number(number)
        self._send_message(message)
        print('✔ Done')
