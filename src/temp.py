from session import *
# browser = webdriver.Chrome()
sessionGenerator(shouldCloseBrowser=True, sessionFileName="00.wa")
browser = webdriver.Chrome()
input("Enter to continue")
sessionOpener(browser)
