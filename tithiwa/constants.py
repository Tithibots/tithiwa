import os

from selenium.webdriver.common.by import By

MODULEDIR = os.path.dirname(__file__)
SESSIONDIR = os.path.join(MODULEDIR, 'sessions')

DEFAULT_SHOULD_OUTPUT = True


class SELECTORS(object):
    OVERLAY = (By.CSS_SELECTOR, 'div[class^="overlay"]')
    OVERLAY_OK = (By.CSS_SELECTOR, 'div[class^="overlay"] div[role="button"]:nth-child(2)')
    QR_CODE = (By.CSS_SELECTOR, 'div[data-ref]')
    MAIN_SEARCH_BAR = (By.CSS_SELECTOR, '#side [contenteditable="true"]')
    MAIN_SEARCH_BAR__DONE = (By.CSS_SELECTOR, 'span[data-testid="x-alt"]')
    MAIN_SEARCH_BAR__SEARCH_ICON = (By.CSS_SELECTOR, 'span[data-testid="search"]')
    MAIN_SEARCH_BAR__BACK_ARROW = (By.CSS_SELECTOR, 'span[data-testid="search"]')
    MAIN_SEARCH_BAR__RESULT_NAMES = (By.CSS_SELECTOR, 'span[title]')
    MESSAGE_INPUT_BOX = (By.CSS_SELECTOR, '#main [contenteditable="true"]')
    CLOSE_INFO = (By.CSS_SELECTOR, 'span[data-testid="x-alt"]')
    BACK_BUTTON = (By.CSS_SELECTOR, 'span[data-testid="back"]')
    NAME_AND_ABOUT = (By.CSS_SELECTOR, '[contenteditable="false"]')
    MAIN_MENU_OPTIONS__MENU_ICON = (By.CSS_SELECTOR, '[data-testid=menu]')
    MAIN_MENU_OPTIONS__NEW_GROUP = (By.CSS_SELECTOR, '[title="New group"]')
    MAIN_MENU_OPTIONS__SETTINGS = (By.CSS_SELECTOR, '[title="Settings"]')
    MAIN_MENU_OPTIONS__PROFILE = (By.CSS_SELECTOR, '[title="Profile"]')
    CREATE_NEW_GROUP__TYPE_CONTACTS_INPUT_BOX = (By.CSS_SELECTOR, '[placeholder="Type contact name"]')
    CREATE_NEW_GROUP__RESULT_BOX = (By.CSS_SELECTOR, 'header + div div[style^="height"]')
    CREATE_NEW_GROUP__OK_CONTACTS_TYPE = (By.CSS_SELECTOR, '[data-testid="arrow-forward"]')
    CREATE_NEW_GROUP__TYPE_GROUP_NAME = (By.CSS_SELECTOR, '[contenteditable="true"]')
    CREATE_NEW_GROUP__OK_GROUP_NAME_TYPE = (By.CSS_SELECTOR, '[data-testid="checkmark-medium"]')
    CHATROOM__NAME = (By.CSS_SELECTOR, '#main header span[dir="auto"]')
    CHATROOM__ONLINE = (By.CSS_SELECTOR, '[title="online"]')
    CHATROOM__INFO = (By.CSS_SELECTOR, '#main > header > div > div > span')
    CHATROOM__INFO_NUMBER = (By.CSS_SELECTOR, 'span[class*="invisible-space"][dir="auto"] span[class*="_"]')
    CHATROOM__CLOSE_INFO = (
        By.CSS_SELECTOR, 'div[style="height: 100%; transform: translateX(0%);"] span[data-testid="x"]')
    CHATROOM__OPTIONS = (By.CSS_SELECTOR, '[data-testid="menu"]')
    CHATROOM__INFO_DELETE_CHAT = (By.CSS_SELECTOR, '._1OwwW ._3oTCZ[title="Delete chat"]')
    CHATROOM__DELETE_CHAT = (By.CSS_SELECTOR, 'li div[title="Delete chat"]')
    CHATROOM__FOOTER = (By.CSS_SELECTOR, 'footer')
    CONTACTS__NAME_IN_CHATS = (By.CSS_SELECTOR, '#side div[aria-label^="Chat list"] div span span[dir="auto"][title]')
    GROUPS__MEMBERS_SEARCH_ICON = (By.CSS_SELECTOR, 'div[role="button"] span[data-testid="search"]')
    GROUPS__SEARCH_CONTACTS_INPUT_BOX = (
        By.CSS_SELECTOR, 'div[data-animate-modal-body="true"] label div[contenteditable="true"]')
    GROUPS__CONTACTS_SEARCH_NAME = (
        By.CSS_SELECTOR, 'div > span[title="You"], div > span span[title]')  # div[data-animate-modal-body="true"]
    GROUPS__CLOSE_CONTACTS_SEARCH = (By.CSS_SELECTOR, 'div[data-animate-modal-backdrop="true"] span[data-testid="x"]')
    # GROUPS__ADMIN_ICON = (By.CSS_SELECTOR, '.LwCwJ')
    GROUPS__MAKE_ADMIN = (By.CSS_SELECTOR, 'li > div[title="Make group admin"]')
    GROUPS__REMOVE_ADMIN = (By.CSS_SELECTOR, 'div[title="Dismiss as admin"]')
    GROUPS__REMOVE = (By.CSS_SELECTOR, 'div[title="Remove"]')
    GROUPS__EXIT_FROM_GROUP = (By.CSS_SELECTOR, 'div[title="Exit group"]')
    # GROUPS__EXIT_DIALOG_BOX_EXIT_BUTTON = (By.CSS_SELECTOR, 'div[class^="overlay"] div[role="button"]:nth-child(2)')
    # GROUPS__NO_LONGER_A_PARTICIPANT = (By.CSS_SELECTOR, '._3ge3i')
    GROUPS__NAME_IN_CHATS = (By.CSS_SELECTOR, '#side div[aria-label^="Chat list"] div > span[dir="auto"][title]')
    GROUPS__GROUP_ICON_IN_POP_UP = (By.CSS_SELECTOR, '.overlay span[data-testid="default-group"]')
    GROUPS__JOIN_BUTTON = (By.CSS_SELECTOR, '.overlay div[role="button"]:nth-child(2)')
    SETTINGS__OK_BUTTON = (By.CSS_SELECTOR, 'div[class^="overlay"] div[role="button"]:nth-child(2)')
    SETTINGS__THEME = (By.CSS_SELECTOR, 'div[title="Theme"]')
    SETTINGS__NOTIFICATIONS = (By.CSS_SELECTOR, 'div[title="Notifications"]')
    SETTINGS__BLOCKED = (By.CSS_SELECTOR, 'div[title="Blocked"]')
    SETTINGS__ADD_BLOCKED_CONTACT = (By.CSS_SELECTOR, 'div[title="Add blocked contact"]')
    SETTINGS__NOTIFICATIONS_OPTIONS = (By.CSS_SELECTOR, 'div[role="checkbox"]')
    SETTINGS__NOTIFICATIONS_TURN_OFF_OPTIONS = (By.CSS_SELECTOR, 'div[class^="overlay"] input')
    # SETTINGS__NOTIFICATIONS_MUTE_OR_UNMUTE = (By.CSS_SELECTOR, '.S7_rT.FV2Qy')
    # SETTINGS__PROFILE = (By.CSS_SELECTOR, '._1V82l')


class STRINGS(object):
    CHECK_CHAR = '✔'
    CROSS_CHAR = '❌'
    THEME_LIGHT = 'light'
    THEME_DARK = 'dark'
    THEME_SYSTEM = 'system'


class INTEGERS(object):
    TURN_OFF_NOTIFICATIONS_FOR_8_HOURS = 0
    TURN_OFF_NOTIFICATIONS_FOR_1_WEEK = 1
    TURN_OFF_NOTIFICATIONS_FOR_ALWAYS = 2
    DEFAULT_WAIT = 89


_SETUP_SESSION = '''
window.indexedDB = window.indexedDB || window.mozIndexedDB ||
    window.webkitIndexedDB || window.msIndexedDB; 
window.IDBTransaction = window.IDBTransaction ||
    window.webkitIDBTransaction || window.msIDBTransaction;
window.IDBKeyRange = window.IDBKeyRange || window.webkitIDBKeyRange ||
    window.msIDBKeyRange
if (!window.indexedDB) {
    window.alert("Your browser doesn't support a stable version of IndexedDB.")
}
var db = await new Promise((resolve, reject) => {
    var request = window.indexedDB.open("wawc");
    request.onerror = function(event) {
        console.log(event);
        resolve(0);
    };

    request.onsuccess = function(event) {
        resolve(request.result);
    };

    request.onupgradeneeded = function(event) {
        resolve(event.target.result)
    }

});
'''

GET_SESSION = _SETUP_SESSION + '''
function readAll() {
    return new Promise((resolve, reject) => {
        res = [];
        var objectStore = db.transaction("user").objectStore("user");
        objectStore.openCursor().onsuccess = function(event) {
            var cursor = event.target.result;
            if (cursor) {
                res.push(cursor.value);
                cursor.continue();
            } else {
                resolve(res);
            }
        };
    });
}
session = await readAll();
res = "";
for (i in session) {
    res += session[i].key + "\\nnavi" + session[i].value + "\\nnavi";
}
return res;
'''

PUT_SESSION = _SETUP_SESSION + '''
await new Promise((resolve, reject) => {
   var request = db.transaction(["user"], "readwrite")
   .objectStore("user")
   .clear();
   request.onsuccess = function(event) {
      resolve(1);
   };
});
function add(key, value) {
    return new Promise((resolve, reject) => {
        var request = db.transaction(["user"], "readwrite")
            .objectStore("user")
            .add({
                key: key,
                value: value
            });
        request.onsuccess = function(event) {
            resolve(0);
        };
        request.onerror = function(event) {
            resolve(1);
        }
    });
}
a = arguments[0].split("\\nnavi");
for (i = 0; i < a.length - 1; i += 2) {
    await add(a[i], a[i + 1]);
}
localStorage.clear();
for (i = 0; i < a.length - 1; i += 2) {
    localStorage.setItem(a[i], a[i+1])
}
'''
