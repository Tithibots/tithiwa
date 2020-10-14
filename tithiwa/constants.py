__all__ = ['MODULEDIR', 'SESSIONDIR',  'SELECTORS']

import os

MODULEDIR = os.path.dirname(__file__)
SESSIONDIR = os.path.join(MODULEDIR, 'sessions')

class SELECTORS(object):
    MAIN_SEARCH_BAR = '._3FRCZ'
    MAIN_SEARCH_BAR_DONE = '.MfAhJ'
    MESSAGE_INPUT_BOX = '#main footer ._3FRCZ'

    class MAIN_MENU_OPTIONS(object):
        MENU_ICON = '[data-testid=menu]'
        NEW_GROUP = '[title="New group"]'

    class CREATE_NEW_GROUP(object):
        TYPE_CONTACTS_INPUT_BOX = '._17ePo'
        RESULT_CONTACT = '._210SC'
        OK_CONTACTS_TYPE = '[data-testid="arrow-forward"]'
        TYPE_GROUP_NAME = '._3FRCZ'
        OK_GROUP_NAME_TYPE = '._3y5oW'
        ENCRYPTED_LOCK_SIGN = '._2VO5X'

    class GROUPS(object):
        NAME = '.DP7CM'
        MEMBERS_SEARCH_ICON = '._3lS1C'
        SEARCH_CONTACTS_INPUT_BOX = '._9a59P ._3FRCZ'
        CONTACTS_SEARCH_NAME = '._3ko75'
        CLOSE_CONTACTS_SEARCH = '._2HE5l .t4a8o'
        ADMIN_ICON = '.LwCwJ'
        MAKE_ADMIN = '.Ut_N0'
        REMOVE = '.Ut_N0[title="Remove"]'
