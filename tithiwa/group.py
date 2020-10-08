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


def wait_for_an_element(selector, browser):
    element = None
    try:
        element = WebDriverWait(browser, 34).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
    except:
        pass
    finally:
        return element

def wait_for_an_element_in_other_element(selector, element):
    while True:
        try:
            relement = element.find_element(By.CSS_SELECTOR, selector)
        except:
            pass
        finally:
            return relement


def create_group(groupname, contacts, browser=None):
    shouldreturnbrowser = False
    if browser == None:
        shouldreturnbrowser = True
    browser = open_session()
    wait_for_an_element('[data-testid=menu]', browser).click()
    wait_for_an_element('[title="New group"]', browser).click()
    inputbox = wait_for_an_element('._17ePo', browser)
    inputbox.click()
    for name in contacts:
        inputbox.send_keys(name)
        wait_for_an_element('._210SC', browser)
        inputbox.send_keys(Keys.TAB + Keys.ENTER)
    wait_for_an_element('[data-testid="arrow-forward"]', browser).click()
    wait_for_an_element('._3FRCZ', browser).send_keys(groupname)
    wait_for_an_element('._3y5oW', browser).click()
    wait_for_an_element('._2VO5X', browser)
    if shouldreturnbrowser:
        return browser


def scrape_members_from_group(groupname, browser=None):
    members = []
    browser = open_session()
    inputbox = wait_for_an_element('._3FRCZ', browser)
    inputbox.send_keys(groupname)
    wait_for_an_element('._210SC', browser)
    inputbox.send_keys(Keys.TAB)
    wait_for_an_element('.DP7CM', browser).click()
    wait_for_an_element('._3lS1C', browser).click()
    wait_for_an_element('._3FRCZ', browser).click()
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
    inputbox = wait_for_an_element('._3FRCZ', browser)
    inputbox.send_keys(groupname)
    wait_for_an_element('._210SC', browser)
    inputbox.send_keys(Keys.TAB)
    wait_for_an_element('.DP7CM', browser).click()
    wait_for_an_element('._3lS1C', browser).click()
    wait_for_an_element('._3FRCZ', browser).click()
    preactive = None
    curractive = browser.switch_to.active_element
    while True:
        curractive.send_keys(Keys.ARROW_DOWN)
        curractive = browser.switch_to.active_element
        if curractive == preactive:
            break
        name = curractive.find_element(By.CSS_SELECTOR, "._3ko75").get_attribute('innerText')
        if name in members:
            try:
                curractive.find_element(By.CSS_SELECTOR, ".LwCwJ")
            except:
                curractive.click()
                wait_for_an_element('.Ut_N0', browser).click()
        preactive = curractive
    wait_for_an_element_in_other_element(".LwCwJ", curractive)


# create_group("yeh", ["Navpreet Devpuri"])

# print(scrape_members_from_group("PROGRAMMING"))

# make_group_admins("test1", ["Navpreet Devpuri", "TiDdi"])


# EXTRA
# element = WebDriverWait(browser, 10).until(
            #     lambda browser: browser.find_element((By.CSS_SELECTOR, '._210SC') or browser.find_element((By.CSS_SELECTOR, '._210SC'))[0]))