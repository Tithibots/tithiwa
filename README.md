# tithiwa - Web WhatsApp bot

Automate Web WhatsApp with selenium.

Full explained Videos on that project are coming soon. Stay tune with my youtube channel [Noobie techs](https://www.youtube.com/c/NoobieTechsTithi_mukherjee/)

## Installation
`
pip install tithiwa
`

## Automations

Create bot 
```pythom
from tithiwa import Tithiwa

tithiwabot = Tithiwa()
```


#### 1. Session

```python
### No need to scan QR code every time.

## 1.  Generate session file
tithiwabot.session.generate_session("filename")

## 2. Open session file
tithiwabot.session.open_session("filename")

input("Press Enter to exit.")
```

#### 2. Chatroom 
```python
## 1. Open chat
tithiwabot.chatroom.open_chat_by_number("919592140593")

## 2. Send message
tithiwabot.chatroom.send_message_to_number("919592140593", "Hello, from Tithiwa")
```
#### 3. Group
```python

## 1. Create Groups
tithiwabot.group.create_group("GroupName", ["contact1", "contact2", "contact2"])


## 2. Scrape list of group members 
membersList = tithiwabot.group.scrape_members_from_group("GroupName")
print(membersList) # ["contact1", "contact2", "contact2"]

## 3. Make some particular group members as group admins
tithiwabot.group.make_group_admins("GroupName", ["contact1", "contact2"])
```

## Contribution
Setup package for development
```buildoutcfg
git clone https://github.com/Maskgirl/tithiwa.git
cd tithiwa
pip install -e .
```
