__all__ = ["session"]

from util import *


class Session:

    def __init__(self, browser, sessiondir=None):
        self.sessiondir = sessiondir
        if sessiondir == None:
            self.sessiondir = os.path.join(
                __file__[:__file__.rfind("tithiwa")], "tithiwa", "sessions")
        self.browser = open_browser_if_not_opened(browser)
        open_whatsapp_if_not_opened(browser)

    def generate_session(self, sessionfilename=None,
                         browser=None, shouldclosebrowser=False, shouldshowfilelocation=True):
        if browser == None:
            browser = self.browser
        os.makedirs(sessiondir, exist_ok=True)
        if sessionfilename == None:
            sessionfilename = create_valid_session_file_name(sessiondir)
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

    def open_session(self, sessionfilename=None,
                     sessiondir=os.path.join(
                         __file__[:__file__.rfind("tithiwa")],
                         "tithiwa", "sessions"),
                     browser=None,
                     wait=True
                     ):
        if browser == None:
            browser = self.browser
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

    def _create_valid_session_file_name(self, sessiondir):
        n = len(os.listdir(sessiondir))
        sessionfilename = "%02d" % n + ".wa"
        while os.path.exists(sessionfilename):
            n += 1
            sessionfilename = "%02d" % n + ".wa"
        if sessionfilename[-3:] != ".wa":
            sessionfilename += ".wa"

        return sessionfilename

# browser = generate_session("03")
# browser.quit()
# open_session("03")
# input("PRESS ENTER")
