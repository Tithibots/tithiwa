__all__ = ["Contact"]

from chatroom import Chatroom
from constants import SELECTORS
from constants import STRINGS
from waobject import WaObject

class Contact(Chatroom, WaObject):

    def __init__(self, browser=None):
        super().__init__(browser)


