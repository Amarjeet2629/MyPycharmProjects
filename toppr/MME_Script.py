from selenium import webdriver
import random
from selenium.webdriver.support.ui import WebDriverWait
browser = webdriver.Chrome('/home/amarjeet-pc/Downloads/chromedriver_linux64/chromedriver')

browser.get('https://docs.google.com/forms/d/e/1FAIpQLSchRa9hArfvgOoBPAFeAQNt7HSEf8ts3ZSkAULcTwBe9iwsnw/viewform')
browser.maximize_window()
for i in range(42):
    elem = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[{}]/label/div/div[2]/div/span'.format(random.randint(1, 1000000) % 2 +1))
    elem.click()
    elem = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[{}]/label/div/div[2]/div/span'.format(random.randint(1, 1000000) % 2+1))
    elem.click()
    browser.execute_script("window.scrollTo(0,550)")
    elem = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[{}]/label/div/div[2]/div/span'.format(random.randint(1, 1000000) % 3+1))
    elem.click()
    elem = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/label[{}]/div[1]'.format(random.randint(1, 1000000) % 4 + 2))
    elem.click()
    elem = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div/div/div/span/span')
    elem.click()
    browser.implicitly_wait(2)
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSchRa9hArfvgOoBPAFeAQNt7HSEf8ts3ZSkAULcTwBe9iwsnw/viewform?usp=form_confirm')

