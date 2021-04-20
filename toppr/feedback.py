from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/home/amarjeet-pc/Downloads/chromedriver_linux64/chromedriver')


browser.get('http://www.iitbhuacademics.com/login/')


browser.maximize_window()

browser.execute_script("document.body.style.zoom='75%'")
browser.implicitly_wait(10)
browser.get('http://www.iitbhuacademics.com/login/google-oauth2')
browser.implicitly_wait(10)
elem = browser.find_element_by_xpath('//*[@id="identifierId"]')
elem.send_keys("Insert Email")
elem = browser.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
elem.click()
elem = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
elem.send_keys("Insert Password")
elem = browser.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
elem.click()
browser.execute_script("window.scrollTo(0,750)")
for i in range(1, 8):
    x__path = '//*[@id="no-more-tables"]/table/tbody/tr[{}]/td[5]/a'.format(i)
    elem = browser.find_element_by_xpath(x__path)
    elem1 = browser.find_element_by_xpath('//*[@id="no-more-tables"]/table/tbody/tr[{}]/td[2]'.format(i))
    print("What rating u want to give from 1 to 5 to {}. 1 is best while 5 is worst: ".format(elem1.text))
    rating = input()
    rating = int(rating)
    browser.implicitly_wait(5)
    elem.click()
    for j in range(2, 20):
        if j != 7 and j != 13:
            x_path = '/html/body/div[2]/form/p[{}]/span'.format(j)
            x_path = x_path + '/input[{}]'.format(rating)
            elem = browser.find_element_by_xpath(x_path)
            elem.click()
            browser.execute_script("window.scrollTo(0,750)")
    browser.execute_script("window.scrollTo(0,750)")
    browser.execute_script("window.scrollTo(0,750)")
    browser.execute_script("window.scrollTo(0,750)")
    elem = browser.find_element_by_xpath('/html/body/div[2]/form/button')
    elem.click()
    alert = browser.switch_to_alert()
    alert.accept()
    browser.switch_to_default_content()
    browser.implicitly_wait(5)
    browser.execute_script("window.scrollTo(0,750)")





