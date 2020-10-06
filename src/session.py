from selenium import webdriver
from time import sleep
import sys
import os


def sessionGenerator(browser=None, sessionDir=os.path.join(__file__[:__file__.rfind("WhatsApp-bot")], "WhatsApp-bot", "sessions"), sessionFileName="", shouldCloseBrowser=False):
    shouldReturnBrowser = False
    if browser == None:
        shouldReturnBrowser = True
        browser = webdriver.Chrome()
    os.makedirs(sessionDir, exist_ok=True)
    if sessionFileName == "":
        n = len(os.listdir(sessionDir))
        sessionFileName = "%02d" % (n) + ".wa"
        while os.path.exists(sessionFileName):
            n += 1
            sessionFileName = "%02d" % (n) + ".wa"
    if sessionFileName[-3:] != ".wa":
        sessionFileName += ".wa"
    browser.get("https://web.whatsapp.com/")
    print("Waiting for QR code scan...")
    while "WAToken1" not in browser.execute_script("return window.localStorage;"):
        continue
    sleep(5)
    session = browser.execute_script("return window.localStorage;")
    with open(os.path.join(sessionDir, sessionFileName), "w", encoding="utf-8") as sessionFile:
        sessionFile.write(str(session))
    print("Your session file is saved to: " +
          os.path.join("sessions", sessionFileName))
    if shouldReturnBrowser and not shouldCloseBrowser:
        return browser
    browser.close()


def sessionOpener(browser=None, sessionDir=os.path.join(__file__[:__file__.rfind("WhatsApp-bot")], "WhatsApp-bot", "sessions"), sessionFileName="00.wa"):
    print(browser, "yesss")
    shouldReturnBrowser = False
    if sessionFileName[-3:] != ".wa":
        sessionFileName += ".wa"
    session = None
    possible_paths = [os.path.join(
        sessionDir, sessionFileName), sessionFileName]
    possibleSessionFilePath = ""
    for path in possible_paths:
        if os.path.exists(path):
            possibleSessionFilePath = path
    if possibleSessionFilePath == "":
        raise IOError('"' + sessionFileName + '" is not exist.')
    with open(possibleSessionFilePath, "r", encoding="utf-8") as sessionFile:
        try:
            session = eval(sessionFile.read())
        except:
            raise IOError('"' + possibleSessionFilePath + '" is invalid file.')
    if browser == None:
        shouldReturnBrowser = True
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
    if shouldReturnBrowser:
        return browser
