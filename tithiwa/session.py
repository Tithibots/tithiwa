from selenium import webdriver
from time import sleep
import sys
import os


def session_generator(sessionfilename="",
                      sessiondir=os.path.join(
                          __file__[:__file__.rfind("tithiwa")], "tithiwa", "sessions"),
                      browser=None, shouldclosebrowser=False):
    shouldreturnbrowser = False
    if browser == None:
        shouldreturnbrowser = True
        browser = webdriver.Chrome()
    os.makedirs(sessiondir, exist_ok=True)
    if sessionfilename == "":
        n = len(os.listdir(sessiondir))
        sessionfilename = "%02d" % (n) + ".wa"
        while os.path.exists(sessionfilename):
            n += 1
            sessionfilename = "%02d" % (n) + ".wa"
    if sessionfilename[-3:] != ".wa":
        sessionfilename += ".wa"
    browser.get("https://web.whatsapp.com/")
    print("Waiting for QR code scan...")
    while "WAToken1" not in browser.execute_script(
            "return window.localStorage;"):
        continue
    sleep(5)
    session = browser.execute_script("return window.localStorage;")
    with open(os.path.join(sessiondir, sessionfilename), "w",
              encoding="utf-8") as sessionfile:
        sessionfile.write(str(session))
    print("Your session file is saved to: " +
          os.path.join("sessions", sessionfilename))
    if shouldreturnbrowser and not shouldclosebrowser:
        return browser
    browser.quit()


def session_opener(sessionfilename="00.wa",
                   sessiondir=os.path.join(
                       __file__[:__file__.rfind("tithiwa")],
                       "tithiwa", "sessions"),
                   browser=None
                   ):
    if sessionfilename[-3:] != ".wa":
        sessionfilename += ".wa"
    session = None
    possible_paths = [
        os.path.join(sessiondir, sessionfilename), sessionfilename
    ]
    possibleSessionfilePath = ""
    for path in possible_paths:
        if os.path.exists(path):
            possibleSessionfilePath = path
    if possibleSessionfilePath == "":
        raise IOError('"' + sessionfilename + '" is not exist.')
    with open(possibleSessionfilePath, "r", encoding="utf-8") as sessionfile:
        try:
            session = eval(sessionfile.read())
        except:
            raise IOError('"' + possibleSessionfilePath + '" is invalid file.')
    if browser == None:
        browser = webdriver.Chrome()
    browser.get("https://web.whatsapp.com/")
    sleep(1)
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
