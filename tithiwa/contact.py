__all__ = ["Contact"]

from chatroom import Chatroom
from constants import SELECTORS
from constants import STRINGS
from waobject import WaObject

class Contact(Chatroom, WaObject):

    def __init__(self, browser=None):
        super().__init__(browser)

    def get_mobile_number_of(self, nameornumber):
        # print(f'Getting mobile number of "{nameornumber}"...', end="... ")
        self.open_chat_to(nameornumber)
        self._open_chat_info()
        number = self._wait_for_mobile_number_to_appear()
        # print(f'{STRINGS.CHECK_CHAR} Done')
        return number

    def _wait_for_mobile_number_to_appear(self):
        number = ''
        while number == '':
            number = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__INFO_NUMBER).text
            continue
        return number

