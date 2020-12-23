from tithiwa import *

tithiwabot = Tithiwa()
# tithiwabot.generate_session("00")

tithiwabot.open_session()
print()

# print("'" + tithiwabot.get_my_name() + "', '" + tithiwabot.get_my_about() + "'")
# tithiwabot.remove_group_admins("Test", ["Navpreet Devpuri"])
# tithiwabot.quit()

# browser = 3
# #doing something else with browser
# tithiwabot = Tithiwa(browser)
# tithiwabot.browser = webdriver.Chrome()
# tithiwabot.open_session()
# print("'" + tithiwabot.get_my_name() + "', '" + tithiwabot.get_my_about() + "'")
# tithiwabot.quit()
session = tithiwabot.browser.execute_script("return window.localStorage;")

# session = eval('''
# ''')
tithiwabot.browser.execute_script(
    """
var keys = Object.keys(arguments[0]);
var values = Object.values(arguments[0]);
for(i=0;i<keys.length;++i) window.localStorage.setItem(keys[i], values[i]);
""",
    session,
)

'''
window.indexedDB = window.indexedDB || window.mozIndexedDB ||
    window.webkitIndexedDB || window.msIndexedDB;

//prefixes of window.IDB objects
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
res;
'''

'''

window.indexedDB = window.indexedDB || window.mozIndexedDB ||
    window.webkitIndexedDB || window.msIndexedDB;

//prefixes of window.IDB objects
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

localStorage.clear();
await new Promise((resolve, reject) => {
   var request = db.transaction(["user"], "readwrite")
   .objectStore("user")
   .clear();
   
   request.onsuccess = function(event) {
      resolve(1);
      // alert("prasad entry has been removed from your database.");
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
            //       alert("Prasad has been added to your database.");
        };

        request.onerror = function(event) {
            resolve(1);
            //       alert("Unable to add data\\r\\nPrasad is already exist in your database! ");
        }
    });
}
a = arguments[0].split("\\nnavi");
for (i = 0; i < a.length; i += 2) {
    await add(a[i], a[i + 1]);
}
'''
