__all__ = ["Group"]

from .constants import *
from .chatroom import Chatroom
from .waobject import WaObject
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Group(Chatroom, WaObject):
    def __init__(self, browser=None):
        super().__init__(browser)

    def create_group(self, groupname, contacts, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Creating group "{groupname}" with contacts {contacts}', end="... ")
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS__MENU_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_MENU_OPTIONS__NEW_GROUP).click()
        inputbox = self._wait_for_presence_of_an_element(SELECTORS.CREATE_NEW_GROUP__TYPE_CONTACTS_INPUT_BOX)
        inputbox.click()
        for name in contacts:
            # pre_style = self._wait_for_presence_of_an_element(SELECTORS.CREATE_NEW_GROUP__RESULT_BOX).get_attribute(
            #     "style")
            inputbox.send_keys(name)
            # self._wait_for_attribute_change(SELECTORS.CREATE_NEW_GROUP__RESULT_BOX, "style", pre_style)
            inputbox.send_keys(Keys.TAB + Keys.ENTER)
        self._wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP__OK_CONTACTS_TYPE).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP__TYPE_GROUP_NAME).send_keys(groupname)
        self._wait_for_an_element_to_be_clickable(SELECTORS.CREATE_NEW_GROUP__OK_GROUP_NAME_TYPE).click()
        self._wait_for_chat_to_open(groupname)
        self._close_info()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def scrape_members_from_group(self, groupname, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Scrapping group members from group "{groupname}"', end="... ")
        members = []
        self._open_group_members_list(groupname)
        preactive = None
        curractive = self.browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            if curractive == preactive:
                break
            members.append(
                curractive.find_element(*SELECTORS.GROUPS__CONTACTS_SEARCH_NAME).get_attribute(
                    'innerText'))
            preactive = curractive
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__CLOSE_CONTACTS_SEARCH).click()
        self._close_chat_info()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')
        return members

    def make_group_admins(self, groupname, members, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Making members {str(members)} to be group admins of group "{groupname}"', end="... ")
        self._open_group_members_list(groupname)
        preactive = None
        curractive = self.browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            if curractive == preactive:
                break
            name = curractive.find_element(*SELECTORS.GROUPS__CONTACTS_SEARCH_NAME).get_attribute(
                'innerText')
            if name in members:
                if curractive.get_attribute("innerText").find("\nGroup admin") == -1:
                    curractive.click()
                    self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__MAKE_ADMIN).click()
            preactive = curractive
        # self._wait_for_presence_of_an_element_in_other_element(SELECTORS.GROUPS__ADMIN_ICON, curractive)
        self._close_info()
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__CLOSE_CONTACTS_SEARCH).click()
        self._close_chat_info()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def remove_members_from_group(self, groupname, members, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Removing these members {str(members)} from the group "{groupname}"', end="... ")
        self._open_group_members_list(groupname)
        preactive = None
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        curractive = self.browser.switch_to.active_element
        while curractive != preactive:
            print(curractive == preactive)
            name = curractive.find_element(*SELECTORS.GROUPS__CONTACTS_SEARCH_NAME).get_attribute(
                'innerText')
            if name in members:
                curractive.click()
                self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__REMOVE).click()
                self._close_info()
            preactive = curractive
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
        # self._wait_for_an_element_to_deattached(curractive)
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__CLOSE_CONTACTS_SEARCH).click()
        self._close_chat_info()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def remove_group_admins(self, groupname, members, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Removing members {str(members)} from being admins of group "{groupname}"', end="... ")
        self._open_group_members_list(groupname)
        preactive = None
        curractive = self.browser.switch_to.active_element
        while True:
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            if curractive == preactive:
                break
            name = curractive.find_element(*SELECTORS.GROUPS__CONTACTS_SEARCH_NAME).get_attribute(
                'innerText')
            if name in members:
                if curractive.get_attribute("innerText").find("\nGroup admin") != -1:
                    curractive.click()
                    self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__REMOVE_ADMIN).click()
            preactive = curractive
        # self._wait_for_presence_of_an_element_in_other_element(SELECTORS.GROUPS__ADMIN_ICON, curractive)
        self._close_info()
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__CLOSE_CONTACTS_SEARCH).click()
        self._close_chat_info()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def send_message_with_mention_all_to_group(self, groupname, message, _shouldoutput=(True, True)):
        members_in_group = self.scrape_members_from_group(groupname=groupname)
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Sending message "{message}" to group "{groupname}" with mentioning all members...', end="... ")
        message_with_members_mention = ""
        for member in members_in_group:
            # Need below condition to avoid mentioning ourself, as scrape_members_from_group gives "You" also a member
            if member == "You":
                continue
            message_with_members_mention += f"@{member}" + Keys.ENTER
        message_with_members_mention += message
        inputbox = self._wait_for_an_element_to_be_clickable(SELECTORS.MESSAGE_INPUT_BOX)
        inputbox.send_keys(message_with_members_mention + Keys.ENTER)
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def exit_from_group(self, groupname, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Exiting from group "{groupname}"', end="... ")
        if self._search_and_open_chat_by_name(groupname):
            self._exit_from_group(_shouldoutput[1])
        else:
            if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
                print(f'{STRINGS.CROSS_CHAR} Failed. Group not found.')
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR__BACK_ARROW).click()

    def exit_from_all_groups(self, _shouldoutput=(True, True)):
        self._wait_for_presence_of_an_element(SELECTORS.GROUPS__NAME_IN_CHATS)
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
        preactive = None
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        curractive = self.browser.switch_to.active_element
        pregroupname = None
        while curractive != preactive:
            groupnameelement = None
            try:
                groupnameelement = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS__NAME_IN_CHATS)
            except:
                pass
            if groupnameelement != None:
                groupname = groupnameelement.get_attribute('innerText')
                self._wait_for_an_element_to_deattached(pregroupname)
                self._wait_for_group_to_open_then_exit(groupname, _shouldoutput)
            preactive = curractive
            pregroupname = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__NAME)
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element

    def clear_chat_from_all_groups(self, _shouldoutput=(True, True)):
        self._wait_for_presence_of_an_element(SELECTORS.GROUPS__NAME_IN_CHATS)
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
        preactive = None
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        curractive = self.browser.switch_to.active_element
        pregroupname = None
        while curractive != preactive:
            groupnameelement = None
            try:
                groupnameelement = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS__NAME_IN_CHATS)
            except:
                pass
            if groupnameelement != None:
                groupname = groupnameelement.get_attribute('innerText')
                self._wait_for_an_element_to_deattached(pregroupname)
                self._wait_for_chat_to_open(groupname)
                self._clear_chat()

            preactive = curractive
            pregroupname = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__NAME)
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element

    def exit_from_groups(self, groupnames, includesamename=True, _shouldoutput=(True, True)):
        exitedgroups = []
        self._wait_for_presence_of_an_element(SELECTORS.GROUPS__NAME_IN_CHATS)
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
        preactive = None
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        curractive = self.browser.switch_to.active_element
        pregroupname = None
        while curractive != preactive:
            groupnameelement = None
            try:
                groupnameelement = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS__NAME_IN_CHATS)
            except:
                pass
            if groupnameelement != None:
                groupname = groupnameelement.get_attribute('innerText')
                if groupname in groupnames:
                    self._wait_for_an_element_to_deattached(pregroupname)
                    self._wait_for_group_to_open_then_exit(groupname, _shouldoutput)
                    exitedgroups.append(groupname)
                    if not includesamename:
                        groupnames.remove(groupname)
            preactive = curractive
            pregroupname = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__NAME)
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} You exited groups: {exitedgroups}.')

    def _open_group_members_list(self, groupname):
        self._search_and_open_chat_by_name(groupname)
        self._open_chat_info()
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__MEMBERS_SEARCH_ICON).click()
        self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__SEARCH_CONTACTS_INPUT_BOX).click()

    def _wait_for_group_to_open_then_exit(self, groupname, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Exiting from group "{groupname}"', end="... ")
        self._wait_for_chat_to_open(groupname)
        self._exit_from_group(_shouldoutput[1])

    def _exit_from_group(self, _shouldoutput1=True):
        footertext = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__FOOTER).get_attribute('innerText')
        if footertext != 'Type a message':
            if _shouldoutput1 and DEFAULT_SHOULD_OUTPUT:
                print(f'{STRINGS.CHECK_CHAR} Done. You are already exited the group.')
        else:
            self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM__NAME).click()
            self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__EXIT_FROM_GROUP).click()
            self._wait_for_presence_of_an_element(SELECTORS.OVERLAY)
            self._wait_for_an_element_to_be_clickable(SELECTORS.OVERLAY_OK).click()
            self._close_chat_info()
            self._close_info()
            if _shouldoutput1 and DEFAULT_SHOULD_OUTPUT:
                print(f'{STRINGS.CHECK_CHAR} Done')

    def _wait_for_group_info_to_load(self):
        chatinfo = 'click here for group info'
        while chatinfo == 'click here for group info':
            try:
                chatinfo = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__INFO).get_attribute('innerText')
            except:
                pass

    def join_group(self, url, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'joining group from link: "{url}"', end="... ")
        group_code = url[url.rfind("/") + 1:]
        group_url = f'https://web.whatsapp.com/accept?code={group_code}'
        self.browser.get(group_url)
        self._wait_for_web_whatsapp_to_load()
        race_result = self._race_for_presence_of_two_elements(SELECTORS.GROUPS__GROUP_ICON_IN_POP_UP,
                                                              SELECTORS.CHATROOM__NAME)
        if race_result[1] == 0:
            pop_up = self._wait_for_presence_of_an_element(SELECTORS.GROUPS__GROUP_ICON_IN_POP_UP)
            self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__JOIN_BUTTON).click()
            self._wait_for_an_element_to_deattached(pop_up)
            if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
                print(f'{STRINGS.CHECK_CHAR} Done')
        else:
            if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
                print(f'{STRINGS.CHECK_CHAR} You already joined it. Done')

    def join_groups(self, urls, _shouldoutput=(True, True)):
        for url in urls:
            self.join_group(url)

    def delete_chats_of_all_exited_groups(self):
        self._wait_for_presence_of_an_element(SELECTORS.GROUPS__NAME_IN_CHATS)
        self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
        preactive = None
        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        curractive = self.browser.switch_to.active_element
        pregroupname = None
        count = 0
        while curractive != preactive:
            footertext = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__FOOTER).get_attribute('innerText')
            if footertext == r"You can't send messages to this group because you're no longer a participant.":
                self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM__NAME).click()
                self._wait_for_an_element_to_be_clickable(SELECTORS.GROUPS__DELETE_GROUP).click()
                self._wait_for_presence_of_an_element(SELECTORS.OVERLAY)
                self._wait_for_an_element_to_be_clickable(SELECTORS.OVERLAY_OK).click()
                self._close_chat_info()
                self._close_info()

                self._wait_for_presence_of_an_element(SELECTORS.GROUPS__NAME_IN_CHATS)
                self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR).click()
                preactive = None
                if count != 0:
                    for i in range(count):
                        self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
                    count -= 1
                else:
                    self.browser.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
                curractive = self.browser.switch_to.active_element
                pregroupname = None
                continue
            
            preactive = curractive
            pregroupname = self._wait_for_presence_of_an_element(SELECTORS.CHATROOM__NAME)
            curractive.send_keys(Keys.ARROW_DOWN)
            curractive = self.browser.switch_to.active_element
            count += 1


    
    # create_group('yeh', ["Navpreet Devpuri"])

# print(scrape_members_from_group("PROGRAMMING"))
#
# make_group_admins("test1", ["Navpreet Devpuri", "TiDdi"])


# EXTRA
# element = WebDriverWait(browser, 10).until(
#     lambda browser: browser.find_element((By.CSS_SELECTOR, '._210SC') or browser.find_element((By.CSS_SELECTOR, '._210SC'))[0]))
