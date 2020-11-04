from tithiwa import *

tithiwabot = Tithiwa()
tithiwabot.open_session()
print("'" + tithiwabot.get_my_name() + "', '" + tithiwabot.get_my_about() + "'")
tithiwabot.quit()

browser = 3
#doing something else with browser
tithiwabot = Tithiwa(browser)
tithiwabot.browser = webdriver.Chrome()
tithiwabot.open_session()
print("'" + tithiwabot.get_my_name() + "', '" + tithiwabot.get_my_about() + "'")
tithiwabot.quit()
