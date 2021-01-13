from tithiwa import *

tithiwabot = Tithiwa()
# tithiwabot.generate_session("00")

tithiwabot.open_session()
tithiwabot.join_group('https://chat.whatsapp.com/IxPJXSkqrwK0MGNAk8cZg7')
print()

session = tithiwabot.browser.execute_script("return window.localStorage;")
