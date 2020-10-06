from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from tkinter import *
from tkinter import ttk

from lib.session import *

# browser = sessionGenerator()
# input("Enter to continue")
# sessionOpener(browser)

driver = None
name = None
filepath = None


def open_wa():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')


def find_nm():
    global name
    name = input('Enter the name of user or group : ')


def path():
    global filepath
    filepath = input('Enter your filepath (images/video): ')


def work():
    input('Enter anything after scanning QR code')


def proceed():
    global driver, name, filepath
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()

    image_box = driver.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)

    sleep(3)

    send_button = driver.find_element_by_xpath(
        '//span[@data-icon="send-light"]')
    send_button.click()


window = Tk()
window.title("Tithi's WathsApp-bot")
l1 = Label(window, text="write_wa_to_open_whatsapp", width=15)
l1.grid(row=0, column=0)
l1 = Label(window, text="write_name_to_search_the_name", width=15)
l1.grid(row=1, column=0)
l1 = Label(window, text="give_the_path_of_the_image_to_send", width=30)
l1.grid(row=2, column=0)
l1 = Label(window, text="enter_anythng_to_work", width=30)
l1.grid(row=3, column=0)
l1 = Label(window, text="enter_anythng_to_proceed", width=30)
l1.grid(row=4, column=0)

write_wa_to_open_whatsapp = StringVar()
e1 = Entry(window, textvariable=write_wa_to_open_whatsapp,)
e1.grid(row=0, column=1)
write_name_to_search_the_name = StringVar()
e2 = Entry(window, textvariable=write_name_to_search_the_name,)
e2.grid(row=1, column=1)
give_the_path_of_the_image_to_send = StringVar()
e3 = Entry(window, textvariable=give_the_path_of_the_image_to_send,)
e3.grid(row=2, column=1)
enter_anythng_to_work = StringVar()
e3 = Entry(window, textvariable=enter_anythng_to_work,)
e3.grid(row=3, column=1)
enter_anythng_to_proceed = StringVar()
e3 = Entry(window, textvariable=enter_anythng_to_proceed,)
e3.grid(row=4, column=1)

b1 = Button(window, text="enter1", width=15)
b1.grid(row=0, column=2)
b1.config(command=open_wa)
b2 = Button(window, text="enter2", width=15)
b2.grid(row=1, column=2)
b2.config(command=find_nm)
b3 = ttk.Button(window, text="enter3", width=15)
b3.grid(row=2, column=2)
b3.config(command=path)
b4 = ttk.Button(window, text="enter4", width=15)
b4.grid(row=3, column=2)
b4.config(command=work)
b5 = ttk.Button(window, text="enter5", width=15)
b5.grid(row=4, column=2)
b5.config(command=proceed)


window.mainloop()
