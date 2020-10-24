<img src="./logo/tithiwa.png" alt="logo" width="233"/>

# tithiwa - Web WhatsApp bot

Automate Web WhatsApp with selenium.
# Check Headless tithiwa [challenge](https://github.com/Tithibots/tithiwa/issues/64)

Full explained Videos on that project are coming soon. Stay tune with our youtube channel [Noobie Techs](https://www.youtube.com/c/NoobieTechsTithi_mukherjee/)

Table of contents
  * [Contribution and creativity points](#contribution)
  * [Automation ideas](#automation-ideas)
  * [Installation](#installation)
  
## Contribution and creativity points
Selenium automation creativity points 
1. **Debugging** [Example](https://github.com/Tithibots/tithiwa/issues/50#issuecomment-710778130)<br> We can create breakpoints to pause execution at any time then we can try to run some python code in the console to find a way to do something. That helps to develop efficiently.  
2. **CTRL + Left mouse click** [Example](https://github.com/Tithibots/tithiwa/issues/50#issuecomment-710779007)<br> We can see the definitions or references or usages of any function or variable in our IDE like PyCharm. That helps to understand the existing code base efficiently.
3. **Inspect elements and console** [Example](https://github.com/Tithibots/tithiwa/issues/50#issuecomment-710781167)<br> In chrome, we can inspect HTML elements and run javascript code inside console. That helps up to find better selectors and automations steps efficiently.

NOTE: By pressing UP key we can see the history about what codes we had run during Python debugging and inside Chrome's console.<br> 
NOTE: If you are running javascript code inside selenium chromedriver's console then it will **NOT** keep history.<br>
Good luck :)
  
## Automation ideas

- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/23): Clear chats of all groups  
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/24): Clear chats of all contacts 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/25): Clear all chats both groups and contacts 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/26): Auto-reply given messages to some given messages 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/27): Scrap chat as text 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/28): Track online status of given number 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/29): Send given message to given contacts at some given time i.e schedule messages 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/53): Join group by invite link
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/39): Change Web WhatsApp's settings 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/42): Scape all contacts and send message containing URL to their own chatroom 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/54): Get currently opened Web WhatsApp's mobile number 
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/55): Open chat to the same number as currently opened Web WhatsApp's number
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/56): Join multiple groups by invite links
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/61): Delete chats of all exited groups
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/62): Delete chats of all contacts
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/60): Get number from contact name
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/66): Get number of views to my status
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/67): Get number of name
- [ ] [Todo](https://github.com/Tithibots/tithiwa/issues/68): Get number of about

```python
from tithiwa import Tithiwa

# Create bot 
tithiwabot = Tithiwa()

## Generate sessions and open sessions ✔ 
tithiwabot.generate_session("filename")
tithiwabot.open_session("filename")

## Open chatroom and send message ✔ 
tithiwabot.open_chat_to("919592140593")
tithiwabot.open_chat_to_number_using_url("919592140593") # wa.me/919592140593
tithiwabot.send_message_to("919592140593", "Hello, from Tithiwa")

## Send a message to multiple chats
tithiwabot.send_message_to_multiple_chats("hello", ["contact1", "contact2", "Group1"])

## Send a message to multiple chats at given time 
tithiwabot.send_message_at_time_to(["contact1", "contact2", "Group1"],
                                   "hi, from tithiwa at 9:36PM",
                                   "21:36:00")

## Create new WhatsApp group ✔ 
tithiwabot.create_group("GroupName", ["contact1", "contact2", "contact2"])

## Scrape members list from group ✔ 
membersList = tithiwabot.scrape_members_from_group("GroupName")
print(membersList) # ["contact1", "contact2", "contact2"]

## Make given contacts as group admins of given group ✔ 
tithiwabot.make_group_admins("GroupName", ["contact1", "contact2"])

## Remove given contacts from given group ✔ 
tithiwabot.remove_members_from_group("GroupName", ["contact1", "contact2"])

## Send a message to a group with mentioning all group members ✔ 
tithiwabot.send_message_with_mention_all_to_group("GroupName", "Hello All")

## Exit from group ✔
tithiwabot.exit_from_group("GroupName1")

## Exit from all groups ✔
tithiwabot.exit_from_all_groups()

## Exit from given groups ✔
tithiwabot.exit_from_groups(["GroupName1", "GroupName2"])
```

## Installation 
NOTE - pip contains older version i.e clone repo to use

`
pip install tithiwa
`
