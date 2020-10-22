from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import datetime
import time, sys
# from datetime import time

chrome_browser = webdriver.Chrome(executable_path='G:\Trial_proj\chromedriver')
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(10)          # Waiting for user to scan the QR code

def new_chat(user):
    chat = chrome_browser.find_element_by_xpath('//div[@class="_2FVVk cBxw-"]')
    chat.click()

    chat = chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    chat.send_keys(user)

    time.sleep(1)       #waiting for Whatsapp to search the contact

    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user))
        user.click()
    except NoSuchElementException:
        print("This contact '{}' was not found".format(user))
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()

def send_messages_at_time(dict_users_name, schd_time):

    h, m = map(int, schd_time.split(':'))

    res = datetime.time(hour=h, minute=m)

    while True:
        now = datetime.datetime.now()
        n = "%0.2d:%0.2d:%0.2d" % (now.hour, now.minute, now.second)
        # print(n, res)
        if str(res) == str(n):

            for i in dict_users_name:

                try:
                    user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(i))        #   can replace these lines from (46-57) with the function to send messages
                    user.click()
                except NoSuchElementException:
                    new_chat(i)


                message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
                message_box.send_keys('Hey, there!!')

                message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
                message_box.click()

            print('Message Sent')
            break

send_messages_at_time(['Contact_1', 'Contact_2'], 'HH:MM')
