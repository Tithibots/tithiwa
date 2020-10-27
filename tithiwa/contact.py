__all__ = ["Contact"]

from chatroom import Chatroom
from constants import SELECTORS
from constants import STRINGS
from waobject import WaObject

class Contact(Chatroom, WaObject):

    def __init__(self, browser=None):
        super().__init__(browser)

    def get_number_from_contact_name(self, name):
        self.open_chat_by_number(name)
        self._open_chat_info()
        element1 = self.browser.find_element(SELECTORS.CHATROOM__INFO__NUMBER)
        number = element1.text
        self._close_chat_info()
        return number
