# tithiwa - Web WhatsApp bot

Automate Web WhatsApp with selenium.

Full explained Videos on that project are coming soon. <br>
Stay tune with my youtube channel [Noobie techs](https://www.youtube.com/c/NoobieTechsTithi_mukherjee/)

## Installation
`
pip install tithiwa
`

## Automations

#### 1. Session

```python
from tithiwa import session

### No need to scan QR code every time.

## 1.  Generate session file
session.generate_session("filename")

## 2. Open session file
browser = session.open_session("filename")

input("Press Enter to exit.")
browser.quit()
```

#### 2. Chatroom 
```python
from selenium import webdriver
from tithiwa import chatroom

browser = webdriver.Chrome()

## 1. Open chat
chatroom.open_chat_by_number("919592140593", browser=browser)

## 2. Send message
chatroom.send_message_to_number("919592140593", "Hello, from Tithiwa", browser=browser)

input("Press Enter to exit.")
browser.quit()
```
#### 3. Group
```python
from selenium import webdriver
from tithiwa import group

browser = webdriver.Chrome()

## 1. Create Groups
group.create_group("GroupName", ["contact1", "contact2", "contact2"], browser=browser)


## 2. Scrape list of group members 
membersList = group.scrape_members_from_group("GroupName", browser=browser)
print(membersList) # ["contact1", "contact2", "contact2"]

## 3. Make some particular group members as group admins
group.make_group_admins("GroupName", ["contact1", "contact2"], browser=browser)

input("Press Enter to exit.")
browser.quit()
```

## Contribution
Setup package for development
```buildoutcfg
git clone https://github.com/Maskgirl/tithiwa.git
cd tithiwa
pip install -e .
```
