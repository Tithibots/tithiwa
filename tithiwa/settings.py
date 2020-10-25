from constants import *


class Settings():
    def open_settings(self):
        print('Opening settings', end="... ")
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS.MENU_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS.SETTINGS).click()
