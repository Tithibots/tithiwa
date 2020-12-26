from .constants import *
from .waobject import WaObject


class Settings(WaObject):

    def set_theme(self, theme: str, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Setting "{theme}" theme', end="...")
        self._open_settings()
        self._wait_for_an_element_to_be_clickable(SELECTORS.SETTINGS__THEME).click()
        self._wait_for_an_element_to_be_clickable((By.CSS_SELECTOR, f'[value="{theme}"]')).click()
        self._wait_for_presence_of_an_element(SELECTORS.OVERLAY)
        self._wait_for_an_element_to_be_clickable(SELECTORS.SETTINGS__OK_BUTTON).click()
        self._press_back_button()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def setting_notifications(self, is_sounds=True, is_desktop_alerts=True, is_show_previews=True,
                              is_turn_off_desktop_notifications=False,
                              turn_off_desktop_notifications_for=INTEGERS.TURN_OFF_NOTIFICATIONS_FOR_ALWAYS,
                              _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Setting notifications', end="...")
        self._open_settings()
        self._wait_for_an_element_to_be_clickable(SELECTORS.SETTINGS__NOTIFICATIONS).click()
        options = self._wait_for_presence_of_all_elements(SELECTORS.SETTINGS__NOTIFICATIONS_OPTIONS)
        self._setting_notifications_select(is_sounds, options[0])
        self._setting_notifications_select(is_desktop_alerts, options[1])
        if is_desktop_alerts and is_show_previews:
            self._setting_notifications_select(is_show_previews, options[2])
        self._setting_notifications_select(is_turn_off_desktop_notifications, options[3])
        self._wait_for_presence_of_an_element(SELECTORS.OVERLAY)
        if is_turn_off_desktop_notifications:
            options = self._wait_for_presence_of_all_elements(SELECTORS.SETTINGS__NOTIFICATIONS_TURN_OFF_OPTIONS)
            options[turn_off_desktop_notifications_for].click()
            self._wait_for_an_element_to_be_clickable(SELECTORS.OVERLAY_OK).click()
        else:
            self._wait_for_an_element_to_be_clickable(SELECTORS.OVERLAY_OK).click()
        self._press_back_button()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def block(self, namesornumbers, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Setting notifications', end="...")
        self._open_settings()
        self._wait_for_an_element_to_be_clickable(SELECTORS.SETTINGS__BLOCKED).click()

        self._press_back_button()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def _setting_notifications_select(self, istrue, element):
        if istrue:
            if element.get_attribute('aria-checked') == 'false':
                element.click()
        else:
            if element.get_attribute('aria-checked') == 'true':
                element.click()

    def _open_settings(self):
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS__MENU_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS__SETTINGS).click()
