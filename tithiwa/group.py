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


class Group:
    def __init__(self, browser=None):
        self.browser = open_browser_if_not_opened(browser)
        open_whatsapp_if_not_opened(self.browser)

    def create_group(self, groupname, contacts, browser=None):
        print(f'Creating group "{groupname}" with contacts {contacts}', end="... ")
        shouldreturnbrowser = False
        if browser == None:
            shouldreturnbrowser = True
            browser = self.browser
        wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS.MENU_ICON, browser).click()
        wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS.NEW_GROUP, browser).click()
        inputbox = wait_for_an_element(SELECTORS.CREATE_NEW_GROUP.TYPE_CONTACTS_INPUT_BOX, browser)
        inputbox.click()
        for name in contacts:
            inputbox.send_keys(name)
            wait_for_an_element(SELECTORS.CREATE_NEW_GROUP.RESULT_CONTACT, browser)
            inputbox.send_keys(Keys.TAB + Keys.ENTER)
        wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP.OK_CONTACTS_TYPE, browser).click()
        wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP.TYPE_GROUP_NAME, browser).send_keys(groupname)
        wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP.OK_GROUP_NAME_TYPE, browser).click()
        wait_for_an_element(SELECTORS.CREATE_NEW_GROUP.ENCRYPTED_LOCK_SIGN, browser)
        print('✔ Done')
        if shouldreturnbrowser:
            return browser

    def scrape_members_from_group(self, groupname, browser=None):
        print(f'Scrapping group members from group "{groupname}"', end="... ")
        members = []
        if browser == None:
            browser = self.browser
        open_group_members_list(groupname, browser)
        preactive = None
        curractive = browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = browser.switch_to.active_element
            if curractive == preactive:
                break
            members.append(
                curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.CONTACTS_SEARCH_NAME).get_attribute(
                    'innerText'))
            preactive = curractive
        wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.CLOSE_CONTACTS_SEARCH, browser).click()
        print('✔ Done')
        return members

    def make_group_admins(self, groupname, members, browser=None):
        print(f'Making members {str(members)} to be group admins of group "{groupname}"', end="... ")
        if browser == None:
            browser = self.browser
        open_group_members_list(groupname, browser)
        preactive = None
        curractive = browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = browser.switch_to.active_element
            if curractive == preactive:
                break
            name = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.CONTACTS_SEARCH_NAME).get_attribute(
                'innerText')
            if name in members:
                try:
                    curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.ADMIN_ICON)
                except:
                    curractive.click()
                    wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.MAKE_ADMIN, browser).click()
            preactive = curractive
        wait_for_an_element_in_other_element(SELECTORS.GROUPS.ADMIN_ICON, curractive)
        wait_for_an_element_to_be_clickable(SELECTORS.GROUPS.CLOSE_CONTACTS_SEARCH, browser).click()
        print('✔ Done')

# create_group('yeh', ["Navpreet Devpuri"])

# print(scrape_members_from_group("PROGRAMMING"))
#
# make_group_admins("test1", ["Navpreet Devpuri", "TiDdi"])


# EXTRA
# element = WebDriverWait(browser, 10).until(
#     lambda browser: browser.find_element((By.CSS_SELECTOR, '._210SC') or browser.find_element((By.CSS_SELECTOR, '._210SC'))[0]))
