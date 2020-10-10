from tithiwa import Tithiwa

tithiwabot = Tithiwa()
tithiwabot.session.open_session("03")
memberlist = tithiwabot.group.scrape_members_from_group("PROGRAMMING")
print(memberlist)


