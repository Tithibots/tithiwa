# tithiwa - Web WhatsApp bot

Automate Web WhatsApp with selenium.

Full explained Videos on that project are coming soon. Stay tune with my youtube channel [Noobie techs](https://www.youtube.com/c/NoobieTechsTithi_mukherjee/)

Table of contents
  * [Automation ideas](#automation-ideas)
  * [Installation](#installation)
  * [Contribution and creativity points](#contribution)
## Automation ideas
Create bot 
```python
from tithiwa import Tithiwa
tithiwabot = Tithiwa()
```
- [x] Done - `generate_session()`: Generate sessions and open sessions ✔ 
```python
tithiwabot.generate_session("filename")
tithiwabot.open_session("filename")
```
- [x] Done - `open_session()`: Open chatroom and send message ✔ 
```python
tithiwabot.open_chat_by_number("919592140593")
tithiwabot.send_message_to_number("919592140593", "Hello, from Tithiwa")
```
- [x] Done - `create_group()`: Create new WhatsApp group ✔ 
```python
tithiwabot.create_group("GroupName", ["contact1", "contact2", "contact2"])
```
- [x] Done - `scrape_members_from_group()`: Scrape members list from group ✔ 
```python
membersList = tithiwabot.scrape_members_from_group("GroupName")
print(membersList) # ["contact1", "contact2", "contact2"]
```
- [x] Done - `make_group_admins()`: Make given contacts as group admins of given group ✔ 
```python
tithiwabot.make_group_admins("GroupName", ["contact1", "contact2"])
```
- [x] Done - `remove_members_from_group()`: Remove given contacts from given group ✔ 
```python
tithiwabot.remove_members_from_group("GroupName", ["contact1", "contact2"])
```
- [x] Done - `send_message_with_mention_all_to_group()`: Send a message to a group with mentioning all group members ✔ 
```python
tithiwabot.send_message_with_mention_all_to_group("GroupName", "Hello All")
```
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/23): Clear chats of all groups  
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/24): Clear chats of all contacts 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/25): Clear all chats both groups and contacts 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/26): Auto-reply given messages to some given messages 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/27): Scrap chat as text 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/28): Track online status of given number 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/29): Send given message to given contacts at some given time i.e schedule messages 
- [x] Done - `exit_from_group()`: Exit from group ✔
```python
tithiwabot.exit_from_group("GroupName1")
```
- [x] Done - `exit_from_all_groups()`: Exit from all groups ✔
```python
tithiwabot.exit_from_all_groups()
```
- [x] Done - `exit_from_groups()`: Exit from given groups ✔
```python
tithiwabot.exit_from_groups(["GroupName1", "GroupName2"])
```
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/39): Change Web WhatsApp's settings 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/42): Scape all contacts and send message containing URL to their own chatroom 

## Installation 
NOTE - pip contains older version i.e clone repo to use

`
pip install tithiwa
`
## Contribution and creativity points
Selenium automation creativity points 
1. **Debugging** <br> We can create breakpoints to pause execution at any time then we can try to run some python code in the console to find a way to do something. That helps to develop efficiently. 
2. **CTRL + Left mouse click** <br> We can see the definitions or references or usages of any function or variable in our IDE like PyCharm. That helps to understand the existing code base efficiently.
3. **Inspect elements and console** <br> In chrome, we can inspect HTML elements and run javascript code inside console. That helps up to find better selectors and automations steps efficiently.

NOTE: By pressing UP key we can see the history about what codes we had run during Python debugging and inside Chrome's console.<br> 
NOTE: If you are running javascript code inside selenium's chromedriver then it will **NOT** keep history.<br>
Good luck :)
