from selenium import webdriver
from fake_useragent import UserAgent

useragent = UserAgent(browsers=['chrome', 'opera', 'firefox'])

options = webdriver.ChromeOptions()
options.binary_location = 'C:/Windows/Cursors/Cent Browser/chrome.exe'
options.add_argument(f'user-agent={useragent.random}')
options.headless = True

driver = webdriver.Chrome(options=options)
