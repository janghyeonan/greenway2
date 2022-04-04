
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome('[PATH]chromedriver')

driver.implicitly_wait(15)
driver.get('[URL]')
driver.find_element_by_xpath('//*[@id="notice_checkbox_865"]').click()
driver.find_element_by_xpath('//*[@id="notice_layer_865"]/div/div/div/fieldset/ul/li/button/img').click()
driver.find_element_by_xpath('//*[@id="login_id"]').send_keys("[ID]")
driver.find_element_by_xpath('//*[@id="login_passwd"]').send_keys("[PASSWORD]")
driver.find_element_by_xpath('//*[@id="header"]/div[2]/fieldset/form/ul[1]/li[3]/a/img').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[1]/div[1]/ul[2]/li[2]/a').click()

while True:
    driver.find_element_by_xpath('//*[@id="mCSB_2"]/div[1]/table/tbody/tr[4]/td[1]').click()
    driver.find_element_by_xpath('//*[@id="calendarTable"]/tbody/tr[5]/td[7]/a').click()
    time.sleep(0.8)
    for i in range(1, 24):
        if i <= 9:
            driver.find_element_by_xpath('//*[@id="0003000'+str(i)+'"]').click()
        else:
            driver.find_element_by_xpath('//*[@id="000300'+str(i)+'"]').click()
        driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/p/a/img').click()
        Alert(driver).accept()

    driver.find_element_by_xpath('//*[@id="calendarTable"]/tbody/tr[4]/td[7]/a').click()
    time.sleep(1)
    for i in range(1, 24):
        if i <= 9:
            driver.find_element_by_xpath('//*[@id="0003000'+str(i)+'"]').click()
        else:
            driver.find_element_by_xpath('//*[@id="000300'+str(i)+'"]').click()
        driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/p/a/img').click()
        Alert(driver).accept()

    driver.find_element_by_xpath('//*[@id="calendarTable"]/tbody/tr[3]/td[7]/a').click()
    time.sleep(1)
    for i in range(1, 24):
        if i <= 9:
            driver.find_element_by_xpath('//*[@id="0003000'+str(i)+'"]').click()
        else:
            driver.find_element_by_xpath('//*[@id="000300'+str(i)+'"]').click()
        driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/p/a/img').click()
        Alert(driver).accept()
