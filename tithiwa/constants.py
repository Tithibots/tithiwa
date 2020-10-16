__all__ = ['MODULEDIR', 'SESSIONDIR', 'SELECTORS']

import os

MODULEDIR = os.path.dirname(__file__)
SESSIONDIR = os.path.join(MODULEDIR, 'sessions')


class SELECTORS(object):
    MAIN_SEARCH_BAR = '._3FRCZ'
    MAIN_SEARCH_BAR_DONE = '.MfAhJ'
    MAIN_SEARCH_BAR_SEARCH_ICON = '._3e4VU'
    MAIN_SEARCH_BAR_BACK_ARROW = '._3e4VU'
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

    class CHATROOM(object):
        NAME_AND_INFO = '._33QME'
        NAME = '.DP7CM'
        INFO = '._3-cMa._3Whw5'

    class GROUPS(object):
        MEMBERS_SEARCH_ICON = '._3lS1C'
        SEARCH_CONTACTS_INPUT_BOX = '._9a59P ._3FRCZ'
        CONTACTS_SEARCH_NAME = '._3ko75'
        CLOSE_CONTACTS_SEARCH = '._2HE5l .t4a8o'
        ADMIN_ICON = '.LwCwJ'
        MAKE_ADMIN = '.Ut_N0'
        REMOVE = '.Ut_N0[title="Remove"]'
        EXIT_FROM_GROUP = '._3wAoe._3DSZk[title="Exit group"]'
        EXIT_DIALOG_BOX = '._9a59P'
        EXIT_BUTTON_EXIT_DIALOG_BOX = '.S7_rT.FV2Qy'
        CLOSE_GROUP_INFO = '[data-testid="x"]'
        NO_LONGER_A_PARTICIPANT = '._3ge3i'
