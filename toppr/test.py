from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
browser = webdriver.Chrome('/home/amarjeet-pc/Downloads/chromedriver_linux64/chromedriver')
browser.get('https://www.google.com')


browser.maximize_window()

browser.implicitly_wait(10)
url_list = ['www.youtube.com', 'www.gmail.com', 'www.facebook.com']

for url1 in url_list:
    url1 = 'https://'+url1
    browser.execute_script('window.open("{}", "_blank");'.format(url1))
