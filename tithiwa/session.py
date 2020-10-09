from selenium import webdriver
from time import sleep
import sys
import os

from util import *


def generate_session(sessionfilename=None,
                     sessiondir=os.path.join(
                         __file__[:__file__.rfind("tithiwa")], "tithiwa", "sessions"),
                     browser=None, shouldclosebrowser=False, shouldshowfilelocation=True):
    browser = open_browser_if_not_opened(browser)
    os.makedirs(sessiondir, exist_ok=True)
    if sessionfilename == None:
        sessionfilename = create_valid_session_file_name(sessiondir)
    open_whatsapp_if_not_opened(browser)
    print("Waiting for QR code scan...")
    while "WAToken1" not in browser.execute_script(
            "return window.localStorage;"):
        continue
    session = browser.execute_script("return window.localStorage;")
    sessionfilelocation = os.path.realpath(os.path.join(sessiondir, sessionfilename))
    with open(sessionfilelocation, 'w',
              encoding='utf-8') as sessionfile:
        sessionfile.write(str(session))
    print('Your session file is saved to: ' +
          sessionfilelocation)
    if shouldshowfilelocation:
        show_file_location(sessiondir)
    if not shouldclosebrowser:
        return browser
    browser.quit()


def open_session(sessionfilename=None,
                 sessiondir=os.path.join(
                     __file__[:__file__.rfind("tithiwa")],
                     "tithiwa", "sessions"),
                 browser=None,
                 wait=True
                 ):
    if sessionfilename == None:
        sessionfilename = get_last_created_session_file(sessiondir)
    else:
        sessionfilename = validate_session_file(sessionfilename, sessiondir)
    session = None
    with open(sessionfilename, "r", encoding="utf-8") as sessionfile:
        try:
            session = eval(sessionfile.read())
        except:
            raise IOError('"' + sessionfilename + '" is invalid file.')
    browser = open_browser_if_not_opened(browser)
    open_whatsapp_if_not_opened(browser)
    print("Injecting session...")
    browser.execute_script(
        """
    var keys = Object.keys(arguments[0]);
    var values = Object.values(arguments[0]);
    for(i=0;i<keys.length;++i) window.localStorage.setItem(keys[i], values[i]);
    """,
        session,
    )
    browser.refresh()
    return browser

# browser = generate_session("03")
# browser.quit()
# open_session("03")
# input("PRESS ENTER")