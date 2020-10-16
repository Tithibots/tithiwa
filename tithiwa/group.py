__all__ = ["Group"]

from time import sleep
from constants import SELECTORS
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from util import *
from waobject import WaObject


class Group(WaObject):
    def __init__(self, browser=None):
        super().__init__(browser)

    def create_group(self, groupname, contacts):
        print(f'Creating group "{groupname}" with contacts {contacts}', end="... ")
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS.MENU_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS.NEW_GROUP).click()
        inputbox = self._wait_for_an_presence_of_element(SELECTORS.CREATE_NEW_GROUP.TYPE_CONTACTS_INPUT_BOX)
        inputbox.click()
        for name in contacts:
            inputbox.send_keys(name)
            self._wait_for_an_presence_of_element(SELECTORS.CREATE_NEW_GROUP.RESULT_CONTACT)
            inputbox.send_keys(Keys.TAB + Keys.ENTER)
        self._wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP.OK_CONTACTS_TYPE).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP.TYPE_GROUP_NAME).send_keys(groupname)
        self._wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP.OK_GROUP_NAME_TYPE).click()
        self._wait_for_an_presence_of_element(SELECTORS.CREATE_NEW_GROUP.ENCRYPTED_LOCK_SIGN)
        print('✔ Done')

    def scrape_members_from_group(self, groupname):
        print(f'Scrapping group members from group "{groupname}"', end="... ")
        members = []
        self._open_group_members_list(groupname)
        preactive = None
        curractive = self.browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            if curractive == preactive:
                break
            members.append(
                curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.CONTACTS_SEARCH_NAME).get_attribute(
                    'innerText'))
            preactive = curractive
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.CLOSE_CONTACTS_SEARCH).click()
        print('✔ Done')
        return members

    def make_group_admins(self, groupname, members):
        print(f'Making members {str(members)} to be group admins of group "{groupname}"', end="... ")
        self._open_group_members_list(groupname)
        preactive = None
        curractive = self.browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            if curractive == preactive:
                break
            name = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.CONTACTS_SEARCH_NAME).get_attribute(
                'innerText')
            if name in members:
                try:
                    curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.ADMIN_ICON)
                except:
                    curractive.click()
                    self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.MAKE_ADMIN).click()
            preactive = curractive
        self._wait_for_presence_of_an_element_in_other_element(SELECTORS.GROUPS.ADMIN_ICON, curractive)
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.CLOSE_CONTACTS_SEARCH).click()
        print('✔ Done')

    def remove_members_from_group(self, groupname, members):
        print(f'Removing these members {str(members)} from the group "{groupname}"', end="... ")
        self._open_group_members_list(groupname)
        preactive = None
        curractive = self.browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            if curractive == preactive:
                break
            name = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.CONTACTS_SEARCH_NAME).get_attribute(
                'innerText')
            if name in members:
                curractive.click()
                self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.REMOVE).click()
            preactive = curractive
        self._wait_for_an_element_to_deattached(curractive)
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.CLOSE_CONTACTS_SEARCH).click()
        print('✔ Done')

    def send_message_with_mention_all_to_group(self, groupname, message):
        members_in_group = self.scrape_members_from_group(groupname=groupname)
        print(f'Sending message "{message}" to group "{groupname}" with mentioning all members...', end="... ")
        message_with_members_mention = ""
        for member in members_in_group:
            # Need below condition to avoid mentioning ourself, as scrape_members_from_group gives "You" also a member
            if member == "You":
                continue
            message_with_members_mention += f"@{member}" + Keys.ENTER
        message_with_members_mention += message
        inputbox = self._wait_for_an_element_to_be_clickable(SELECTORS.MESSAGE_INPUT_BOX)
        inputbox.send_keys(message_with_members_mention + Keys.ENTER)
        print('✔ Done')

    def exit_from_groups(self, groups):
        for group in groups:
            print(f'Exiting from group "{group}"', end="... ")
            if self._find_group_and_open_chat(group):
                self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.NAME).click()
                self._exit_from_group()
            else:
                print(f'\u2718 Failed. Group not found.')
            self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR_BACK_ARROW).click()

    def _open_group_members_list(self, groupname):
        inputbox = self._wait_for_an_presence_of_element(SELECTORS.MAIN_SEARCH_BAR)
        inputbox.send_keys(groupname)
        self._wait_for_an_presence_of_element(SELECTORS.MAIN_SEARCH_BAR_DONE)
        inputbox.send_keys(Keys.TAB)
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.NAME).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.MEMBERS_SEARCH_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.SEARCH_CONTACTS_INPUT_BOX).click()

    def _find_group_and_open_chat(self, groupname):
        isfound = False
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR_SEARCH_ICON).click()
        self.browser.switch_to.active_element.send_keys(groupname)
        self._wait_for_an_presence_of_element(SELECTORS.MAIN_SEARCH_BAR_DONE)
        preactive = None
        curractive = self.browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            if curractive == preactive:
                break
            name = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.CONTACTS_SEARCH_NAME).get_attribute(
                'innerText')
            if name == groupname:
                isfound = True
                break
            preactive = curractive
        self._wait_for_group_to_open(groupname)
        return isfound

    def _wait_for_group_to_open(self, groupname):
        while True:
            nameofgroup = self._wait_for_an_presence_of_element(SELECTORS.GROUPS.NAME).get_attribute(
                'innerText')
            if nameofgroup == groupname:
                break

    def _exit_from_group(self):
        no_longer_a_participant = self._wait_for_an_presence_of_element(SELECTORS.GROUPS.NO_LONGER_A_PARTICIPANT)
        if no_longer_a_participant is not None:
            print(f'\u2718 Failed. You are not the member of the group.')
            self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.CLOSE_GROUP_INFO).click()
        else:
            self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.EXIT_FROM_GROUP).click()
            self._wait_for_an_presence_of_element(SELECTORS.GROUPS.EXIT_DIALOG_BOX)
            self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.EXIT_BUTTON_EXIT_DIALOG_BOX).click()
            self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.CLOSE_GROUP_INFO).click()
            print('✔ Done')

# create_group('yeh', ["Navpreet Devpuri"])

# print(scrape_members_from_group("PROGRAMMING"))
#
# make_group_admins("test1", ["Navpreet Devpuri", "TiDdi"])


# EXTRA
# element = WebDriverWait(browser, 10).until(
#     lambda browser: browser.find_element((By.CSS_SELECTOR, '._210SC') or browser.find_element((By.CSS_SELECTOR, '._210SC'))[0]))
