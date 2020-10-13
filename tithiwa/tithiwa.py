__all__ = ["Tithiwa"]

from chatroom import Chatroom
from session import Session
from group import Group
from waobject import WaObject


class Tithiwa(WaObject):
    def __init__(self, browser=None):
        super().__init__(browser)
        self.session = Session(browser=self.browser)
        self.chatroom = Chatroom(browser=self.browser)
        self.group = Group(browser=self.browser)


    # def __del__(self):
    #     self.browser.quit()