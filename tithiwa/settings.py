from constants import *


class Settings():
    def open_settings(self):
        print('Opening settings', end="... ")
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS.MENU_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS.SETTINGS).click()

    def choose_theme(self, theme: str):
        self.open_settings()
        self._wait_for_an_element_to_be_clickable(
            SELECTORS.SETTINGS.THEME).click()
        self._wait_for_an_element_to_be_clickable(f'[value="{theme}"]').click()
        print(f'Applying {theme} theme', end="... ")
        self._wait_for_an_element_to_be_clickable(
            SELECTORS.SETTINGS.OK_BUTTON).click()
        self.close_settings()

    def close_settings(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.BACK_MAIN).click()
