from constants import *
from waobject import WaObject

class Settings(WaObject):

    def choose_theme(self, theme: str, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Applying {theme} theme', end="...")
        self._open_settings()
        self._wait_for_an_element_to_be_clickable(SELECTORS.SETTINGS__THEME).click()
        self._wait_for_an_element_to_be_clickable((By.CSS_SELECTOR, f'[value="{theme}"]')).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.SETTINGS__OK_BUTTON).click()
        self._close_settings()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def _open_settings(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS__MENU_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS__SETTINGS).click()

    def _close_settings(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.BACK_BUTTON).click()
