__all__ = ["Tithiwa"]

from chatroom import Chatroom
from session import Session
from group import Group
from util import *


class Tithiwa:
    def __init__(self, browser=None):
        self.browser = open_browser_if_not_opened(browser)
        open_whatsapp_if_not_opened(self.browser)
        self.session = Session(self.browser)
        self.chatroom = Chatroom(self.browser)
        self.group = Group(self.browser)

    def quit(self):
        self.browser.quit()
    # def __del__(self):
    #     self.browser.quit()