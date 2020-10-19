__all__ = ["Contact"]

from chatroom import Chatroom
from constants import SELECTORS
from constants import STRINGS

class Contact(Chatroom):

    def __init__(self, browser=None):
        super().__init__(browser)

    def open_chat_by_name_or_number(self, number):
        print(f'Opening chatroom to "{number}"', end="... ")
        self._search_and_open_chat_by_name(number)
        print(f'{STRINGS.CHECK_CHAR} Done')

    def open_chat_by_number_using_url(self, number):
        print(f'Opening chatroom to "{number}"', end="... ")
        self.browser.get("https://web.whatsapp.com/send?phone=" + number)
        self._wait_for_presence_of_an_element(SELECTORS.MAIN_SEARCH_BAR)
        print(f'{STRINGS.CHECK_CHAR} Done')

    def send_message_to_number(self, number, message):
        print(f'Sending message "{message}" to number "{number}"...', end="... ")
        self.open_chat_by_name_or_number(number)
        self._send_message(message)
        print(f'{STRINGS.CHECK_CHAR} Done')
