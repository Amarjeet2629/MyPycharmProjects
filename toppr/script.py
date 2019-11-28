def get_doubt(take_up_xpath):
    try:
        element = WebDriverWait(browser, 10000000).until(
            EC.presence_of_element_located((By.XPATH, take_up_xpath))

        )
        element.click()
    finally:
        get_doubt(take_up_xpath)


from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome('/home/amarjeet-pc/Downloads/chromedriver_linux64/chromedriver')
browser.get('https://community.toppr.com/')
browser.maximize_window()
browser.implicitly_wait(10)
elem1 = browser.find_element_by_xpath(xpath='//*[@id="app"]/div/div/div[1]/div/div[1]/div[2]/button[1]')
elem1.click()
browser.implicitly_wait(2)
elem2 = browser.find_element_by_id('email-login')
elem3 = browser.find_element_by_id('password-login')
elem2.send_keys('amarjeet.ans.sinha@gmail.com')
elem3.send_keys('ansu2678')
elem4 = browser.find_element_by_xpath('//*[@id="login_modal_form"]/button[2]')
elem4.click()
elem5 = browser.find_element_by_xpath('//*[@id="index-headjs-page"]/body/div[5]/div/div[2]/div[4]/div/div[5]/a')
elem5.click()
handles = browser.window_handles
parent_handle = browser.current_window_handle
for handle in handles:
    if parent_handle != handle:
        browser.switch_to_window(handle)

take_up_xpath = '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[3]/div[2]/button'

get_doubt(take_up_xpath)
