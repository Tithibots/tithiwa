__all__ = ["Group"]

from selenium import webdriver
from time import sleep
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from util import *
from constants import SELECTORS
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

    def _open_group_members_list(self, groupname):
        inputbox = self._wait_for_an_presence_of_element(SELECTORS.MAIN_SEARCH_BAR)
        inputbox.send_keys(groupname)
        self._wait_for_an_presence_of_element(SELECTORS.MAIN_SEARCH_BAR_DONE)
        inputbox.send_keys(Keys.TAB)
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.NAME).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.MEMBERS_SEARCH_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.SEARCH_CONTACTS_INPUT_BOX).click()

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
# create_group('yeh', ["Navpreet Devpuri"])

# print(scrape_members_from_group("PROGRAMMING"))
#
# make_group_admins("test1", ["Navpreet Devpuri", "TiDdi"])


# EXTRA
# element = WebDriverWait(browser, 10).until(
#     lambda browser: browser.find_element((By.CSS_SELECTOR, '._210SC') or browser.find_element((By.CSS_SELECTOR, '._210SC'))[0]))
