__all__ = ["Tithiwa"]

from session import Session
from settings import Settings
from group import Group
from contact import Contact

class Tithiwa(Session, Settings, Group, Contact):
    def __init__(self, browser=None):
        super().__init__(browser)

    # def __del__(self):
    #     self.browser.quit()