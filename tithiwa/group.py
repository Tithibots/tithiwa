from selenium import webdriver
from time import sleep
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from session import open_session

__all__ = ["create_group", "scrape_members_from_group", "make_group_admins"]


def create_group(groupname, contacts, browser=None):
    shouldreturnbrowser = False
    if browser == None:
        shouldreturnbrowser = True
    # data-testid="menu"
    browser = open_session()
    sleep(2)
    browser.find_element_by_css_selector('[data-testid=menu]').click()
    sleep(2)
    browser.find_element_by_css_selector('[title="New group"]').click()
    sleep(8)
    inputbox = browser.find_element(By.CLASS_NAME, "_17ePo")
    for name in contacts:
        inputbox.send_keys(name)
        sleep(5)
        inputbox.send_keys(Keys.TAB + Keys.ENTER)
    sleep(1)
    browser.find_element_by_css_selector('[data-testid="arrow-forward"]').click()
    sleep(1)
    browser.find_element(By.CLASS_NAME, "_3FRCZ").send_keys(groupname)
    sleep(1)
    browser.find_element(By.CLASS_NAME, "_3y5oW").click()
    sleep(3)
    if shouldreturnbrowser:
        return browser


def scrape_members_from_group(groupname, browser=None):
    members = []
    browser = open_session()
    inputbox = browser.find_element(By.CLASS_NAME, "_3FRCZ")
    inputbox.send_keys(groupname)
    sleep(5)
    inputbox.send_keys(Keys.TAB)
    sleep(3)
    browser.find_element(By.CSS_SELECTOR, ".DP7CM").click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, "._3lS1C").click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, "._3FRCZ").click()
    sleep(1)
    preactive = None
    curractive = browser.switch_to.active_element
    while True:
        curractive.send_keys(Keys.ARROW_DOWN)
        curractive = browser.switch_to.active_element
        if curractive == preactive:
            break
        members.append(curractive.find_element(By.CSS_SELECTOR, "._3ko75").get_attribute('innerText'))
        preactive = curractive

    return members


def make_group_admins(groupname, members, browser=None):
    browser = open_session()
    inputbox = browser.find_element(By.CLASS_NAME, "_3FRCZ")
    inputbox.send_keys(groupname)
    sleep(5)
    inputbox.send_keys(Keys.TAB)
    sleep(3)
    browser.find_element(By.CSS_SELECTOR, ".DP7CM").click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, "._3lS1C").click()
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, "._3FRCZ").click()
    sleep(1)
    preactive = None
    curractive = browser.switch_to.active_element
    while True:
        curractive.send_keys(Keys.ARROW_DOWN)
        sleep(1)
        curractive = browser.switch_to.active_element
        if curractive == preactive:
            break
        name = curractive.find_element(By.CSS_SELECTOR, "._3ko75").get_attribute('innerText')
        if name in members:
            try:
                curractive.find_element(By.CSS_SELECTOR, ".LwCwJ")
            except:
                curractive.click()
                sleep(1)
                browser.find_element(By.CSS_SELECTOR, ".Ut_N0").click()
                sleep(1)
        preactive = curractive
    sleep(3)

# make_group_admins("yess", ["Navpreet Devpuri", "TiDdi"])
