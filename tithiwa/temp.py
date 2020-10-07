# from session import *
from selenium import webdriver
# session_generator(shouldclosebrowser=True, sessionfilename="00.wa")
# browser = webdriver.Chrome()
# sessionGenerator(shouldCloseBrowser=True, sessionFileName="00.wa")
# browser = webdriver.Chrome()
# browser.quit()
# input("Enter to continue")
# sessionOpener(browser)
# from messages import *
# from session import *
import os
# browser = session_generator()
# session_opener(browser=browser)

# browser = session_opener()

# open_chat_by_number("919592140593", browser=browser)
#
# send_message_to_number("919592140593", "yess", browser=browser)
# input("Enter")

# from tithiwa import session
#
# session.session_generator()

import tithiwa
tithiwa.session.session_opener()
tithiwa.session.session_generator()
tithiwa.messages.send_message_to_number()
tithiwa.messages.open_chat_by_number()



