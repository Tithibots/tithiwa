from tithiwa import *

tithiwabot = Tithiwa()
tithiwabot.open_session()
print("'" + tithiwabot.get_my_name() + "', '" + tithiwabot.get_my_about() + "'")
tithiwabot.quit()

browser = webdriver.Chrome()'
#doing something else with browser
tithiwabot = Tithiwa(browser)
tithiwabot.open_session()
print("'" + tithiwabot.get_my_name() + "', '" + tithiwabot.get_my_about() + "'")
tithiwabot.quit()
