import chatroom
import session
import group

class Session:

    @staticmethod
    def generate_session(sessionfilename=None, sessiondir=None, browser=None, shouldclosebrowser=False,
                         shouldshowfilelocation=True):
        tempbot = session.Session(sessiondir, browser)
        tempbot.generate_session(sessionfilename, shouldclosebrowser, shouldshowfilelocation)

    @staticmethod
    def open_session(sessionfilename=None, sessiondir=None, browser=None, wait=True):
        tempbot = session.Session(sessiondir, browser)
        tempbot.open_session(sessionfilename, wait)


class Chatroom:

    @staticmethod
    def open_chat_by_number(number, browser=None, wait=True):
        tempbot = chatroom.Chatroom(browser)
        tempbot.open_chat_by_number(number, wait)

    @staticmethod
    def send_message_to_number(number, message, browser=None):
        tempbot = chatroom.Chatroom(browser)
        tempbot.open_chat_by_number(number, message)


class Group:

    @staticmethod
    def create_group(groupname, contacts, browser=None):
        tempbot = group.Group(browser)
        tempbot.create_group(groupname, contacts)

    @staticmethod
    def scrape_members_from_group(groupname, browser=None):
        tempbot = group.Group(browser)
        return tempbot.scrape_members_from_group(groupname)

    @staticmethod
    def make_group_admins(groupname, members, browser=None):
        tempbot = group.Group(browser)
        tempbot.make_group_admins(groupname, members)

