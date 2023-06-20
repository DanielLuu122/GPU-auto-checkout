from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import info
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get(info.link)

buy = False

while not buy:
    try:
        addToCartBtn = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/article/section[2]/aside/section/div[1]/div/div[4]/form/div/div[2]/button")
        time.sleep(1)
        addToCartBtn.click()
        
    except: 
        time.sleep(1)
        driver.refresh()
        continue
    try:
        driver.get("https://www.memoryexpress.com/User/Login?ReturnUrl=%2fCheckout%2fShippingPayment")
        email = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/div/div[1]/form/fieldset[2]/div/div[1]/div/input")
        email.send_keys(info.email)
        pw = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/div/div[1]/form/fieldset[2]/div/div[2]/div/input")
        pw.send_keys(info.password)
        login = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/div/div[1]/form/div/div[2]/button")
        login.click()
        driver.get("https://www.memoryexpress.com/Checkout/ShippingPayment")
    except:
        continue
    try:
        time.sleep(4)
        shipping = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/form/section[4]/section/div[4]/div[1]/div[1]/label/input")
        shipping.click()
        time.sleep(2)
        processorder = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/form/section[10]/div/div[1]/button")
        processorder.click()
    except:
        print("confirmation error")
        continue
    try:
        time.sleep(1)
        name = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/form/div[3]/div/div[2]/div[2]/div/div[1]/div/input")
        name.send_keys(info.name)
        card = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/form/div[3]/div/div[2]/div[2]/div/div[2]/div/input")
        card.send_keys(info.card)
        select = Select(driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/form/div[3]/div/div[2]/div[2]/div/div[3]/div/select[1]"))
        select.select_by_value(info.month)
        select = Select(driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/form/div[3]/div/div[2]/div[2]/div/div[3]/div/select[2]"))
        select.select_by_value(info.year)
        ccv = driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/form/div[3]/div/div[2]/div[2]/div/div[4]/div/input")
        ccv.send_keys(info.ccv)
        finish =  driver.find_element_by_xpath("/html/body/section/section/div/div[3]/div[3]/div[2]/main/section[3]/div/div[2]/form/div[4]/section/div[1]/button")
        finish.click()
        print("order placed")
        buy = True
    except:
        print("credit card error")
        buy = True
        continue
