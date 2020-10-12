from selenium import webdriver
import flextithiwa
browser = webdriver.Chrome()

flextithiwa.Session.generate_session(browser=browser)
flextithiwa.Session.open_session(browser=browser)
memberlist = flextithiwa.Group.scrape_members_from_group("PROGRAMMING", browser=browser)
print(memberlist)
flextithiwa.Group.create_group("Group made by flextithiwa", ["Navpreet Devpuri"], browser)
flextithiwa.Chatroom.send_message_to_number("919592140593", "Yess, from tithiwa", browser)

browser.close()
# import os
# print(os.path.exists('F:\\projects\\tithiwa\\tithiwa\\sessions\\00.wa'))