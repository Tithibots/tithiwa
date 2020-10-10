from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
import os
import platform
import subprocess

def open_browser_if_not_opened(browser):
    if browser == None:
        browser = webdriver.Chrome()
    return browser


def show_file_location(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

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
    relement = None
    while True:
        try:
            relement = element.find_element(By.CSS_SELECTOR, selector)
        except:
            pass
        finally:
            return relement


def open_whatsapp_if_not_opened(browser):
    if browser.current_url.find("web.whatsapp") == -1:
        browser.get("https://web.whatsapp.com/")





def get_last_created_session_file(sessiondir):
    if not os.path.exists(sessiondir):
        raise IOError('No session file is exists. Generate session file by using generate_session().')
    files = os.listdir(sessiondir)
    paths = [os.path.join(sessiondir, basename) for basename in files]
    sessionfilename = max(paths, key=os.path.getctime)
    print(sessionfilename)
    if not os.path.exists(sessionfilename):
        raise IOError('No session file is exists. Generate session file by using generate_session().')
    return sessionfilename


def validate_session_file(sessionfilename, sessiondir):
    if sessionfilename[-3:] != ".wa":
        sessionfilename += ".wa"
    possible_paths = [
        os.path.join(sessiondir, sessionfilename), sessionfilename
    ]
    possibleSessionfilePath = None
    for path in possible_paths:
        if os.path.exists(path):
            possibleSessionfilePath = path
    if possibleSessionfilePath == None:
        raise IOError('Session file "' + sessionfilename + '" is not exist. Generate that session file by using generate_session(\''+sessionfilename+'\')')
    return possibleSessionfilePath

def open_group_members_list(groupname, browser):
    inputbox = wait_for_an_element('._3FRCZ', browser)
    inputbox.send_keys(groupname)
    wait_for_an_element('._325lp', browser)
    inputbox.send_keys(Keys.TAB)
    wait_for_an_element('.DP7CM', browser).click()
    wait_for_an_element('._3lS1C', browser).click()
    wait_for_an_element('._3FRCZ', browser).click()

# show_file_location("sessions")
# open_whatsapp_if_not_opened()
