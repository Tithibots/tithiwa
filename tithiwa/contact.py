__all__ = ["Contact"]

from chatroom import Chatroom
from constants import *
from waobject import WaObject

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

