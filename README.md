# tithiwa - WhatsApp-bot

Automate WhatsApp with selenium in python.

## Installation
`
pip install tithiwa
`

## Automations

#### 1. Session
   1. Generate or Open session file for Web-WhatsApp i.e No need to scan QR code everytimes.
Usage

```python
from tithiwa import session

session.generate_session("filename")

browser = session.open_session("filename")

input("Press Enter to exit.")
browser.quit()
```

#### 2. Chatroom 
   1. Open chat and Send messages.
```python
from selenium import webdriver
from tithiwa import chatroom

browser = webdriver.Chrome()

chatroom.open_chat_by_number("919592140593", browser=browser)

chatroom.send_message_to_number("919592140593", "Hello, from Tithiwa", browser=browser)

input("Press Enter to exit.")
browser.quit()
```
####3. Group
   1. Create Groups
   2. Scape list of group members 
   3. Make some particular group members as group admins
```python
from selenium import webdriver
from tithiwa import group

browser = webdriver.Chrome()

group.create_group("GroupName", ["contact1", "contact2", "contact2"], browser=browser)

membersList = group.scrape_members_from_group("GroupName", browser=browser)
print(membersList) # ["contact1", "contact2", "contact2"]

group.make_group_admins("GroupName", ["contact1", "contact2"], browser=browser)

input("Press Enter to exit.")
browser.quit()
```

## Contribution

Clone this repo 
```buildoutcfg
git clone https://github.com/Maskgirl/tithiwa.git
```
Install for development
```buildoutcfg
cd tithiwa
pip install -e .
```
