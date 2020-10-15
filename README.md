# tithiwa - Web WhatsApp bot

Automate Web WhatsApp with selenium.

Full explained Videos on that project are coming soon. Stay tune with my youtube channel [Noobie techs](https://www.youtube.com/c/NoobieTechsTithi_mukherjee/)

- [tithiwa - Web WhatsApp bot](#tithiwa---web-whatsapp-bot)
  * [Automation ideas](#automation-ideas)
  * [Installation](#installation)
  * [Automation](#automation)
      - [1. Session](#1-session)
      - [2. Chatroom](#2-chatroom)
      - [3. Group](#3-group)
  * [Contribution](#contribution)

## Automation ideas
- [x] [Done](https://github.com/Tithibots/tithiwa/blob/main/tithiwa/session.py#L16-L63) Generate sessions and open sessions ✔ 
- [x] [Done](https://github.com/Tithibots/tithiwa/blob/main/tithiwa/chatroom.py#L21-L33) Open chatroom and send message ✔ 
- [x] [Done](https://github.com/Tithibots/tithiwa/blob/main/tithiwa/group.py#L19-L33) Create new WhatsApp group ✔ 
- [x] [Done](https://github.com/Tithibots/tithiwa/blob/main/tithiwa/group.py#L35-L52) Scrape members list from group ✔ 
- [x] [Done](https://github.com/Tithibots/tithiwa/blob/main/tithiwa/group.py#L54-L75) Make given contacts as group admins of given group ✔ 
- [x] [Done](https://github.com/Tithibots/tithiwa/blob/main/tithiwa/group.py#L77-L95) Remove given contacts from given group ✔ 
- [x] [Done](https://github.com/Tithibots/tithiwa/blob/main/tithiwa/group.py#L97-L109) Send a message to a group with mentioning all group members ✔ 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/23) Clear chats of all groups  
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/24) Clear chats of all contacts 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/25) Clear all chats both groups and contacts 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/26) Auto-reply given messages to some given messages 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/27) Scrap chat as text 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/28) Track online status of given number 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/29) Send given message to given contacts at some given time i.e schedule messages 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/35) Exit from all groups 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/43) Exit from given groups 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/39) Change Web WhatsApp's settings 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/42) Scape all contacts and send message containing URL to their own chatroom 

## Installation
`
pip install tithiwa
`

## Automation

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

## 4. Remove given contacts from given group 
tithiwabot.group.remove_members_from_group("GroupName", ["contact1", "contact2"])

## 5. Send a message to a group with mentioning all group members
tithiwabot.send_message_with_mention_all_to_group("GroupName", "Hello All")
```

## Contribution
Setup package for development
```buildoutcfg
git clone https://github.com/Maskgirl/tithiwa.git
cd tithiwa
pip install -e .
```
