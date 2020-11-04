from tithiwa import *

tithiwabot = Tithiwa()
tithiwabot.open_session()
print("'" + tithiwabot.get_my_name() + "', '" + tithiwabot.get_my_about() + "'")
tithiwabot.quit()

browser = webdriver.Chrome()
tithiwabot = Tithiwa(browser)
tithiwabot.open_session()
print("'" + tithiwabot.get_my_name() + "', '" + tithiwabot.get_my_about() + "'")
tithiwabot.quit()
