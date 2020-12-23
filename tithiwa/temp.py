from tithiwa import *

tithiwabot = Tithiwa()
# tithiwabot.generate_session("00")

tithiwabot.open_session()
print()

session = tithiwabot.browser.execute_script("return window.localStorage;")
