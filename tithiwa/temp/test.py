from tithiwa import *

tithiwabot = Tithiwa()
# tithiwabot.generate_session("00")
tithiwabot.open_session()

contacts_or_groups = ["Navpreet Devpuri"]
group_name = "test2"
time_to_send = "15:45:00"

# tithiwabot.open_chat_to("919592140593")
# tithiwabot._open_group_members_list("PROGRAMMING")
# tithiwabot.open_chat_to_number_using_url("919592140593")  # wa.me/919592140593
# tithiwabot.send_message_to("919592140593", "Hello, from Tithiwa")

# print(tithiwabot.get_mobile_number_of(contacts_or_groups[0]))

# tithiwabot.send_message_to_multiple_chats([contact for contact in contacts_or_groups], "hello")

# tithiwabot.send_message_at_time_to([contact for contact in contacts_or_groups],
#                                    "hi, from tithiwa at 9:36PM",
#                                    time_to_send)

# tithiwabot.create_group(group_name, [contact for contact in contacts_or_groups])

# print(tithiwabot.scrape_members_from_group(group_name))  # ["contact1", "contact2", "contact2"]
# tithiwabot.remove_members_from_group("test2", ["Navpreet Devpuri"])
# print()
tithiwabot.make_group_admins(group_name, [contact for contact in contacts_or_groups])
#
# tithiwabot.remove_members_from_group(group_name, [contact for contact in contacts_or_groups])
#
tithiwabot.send_message_with_mention_all_to_group(group_name, "Hello All")
#
tithiwabot.exit_from_group(group_name)
#
tithiwabot.exit_from_all_groups()
#
tithiwabot.exit_from_groups([group_name])
