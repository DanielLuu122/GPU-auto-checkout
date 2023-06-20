from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import info
import time

driver = webdriver.Chrome("chromedriver.exe")

buy = False
driver.get(info.link)

while not buy:
    try:
        addToCartBtn = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div/div[1]/div[1]/div[3]/div/div[2]/button")
        time.sleep(1)
        addToCartBtn.click()
        driver.get("https://secure.newegg.ca/shop/cart")
    except:
        time.sleep(1)
        continue
    try:
        checkoutBtn = driver.find_element_by_xpath("/html/body/div[6]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button")
        checkoutBtn.click()
        time.sleep(1)
        email = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div/div/div[1]/form[1]/div/div[1]/div/input")
        email.send_keys(info.email)
        signInE = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div/div/div[1]/form[1]/div/div[3]/button")
        signInE.click()
    except:
        continue
#    try:
 #       pw = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div/div/div[2]/form[1]/div/div[2]/div/input")
  #      pw.send_keys(info.password)
   #     signIn = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]/div/div/div[2]/form[1]/div/div[3]/button")
    #    signIn.click()        
    #except:
      #  continue
    try:
        payment = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button")))
        payment.click()
        time.sleep(2)
        cvv = driver.find_element_by_xpath("/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/label/div[4]/input")
        cvv.click()
        cvv.send_keys(info.cvv)
        review = driver.find_element_by_xpath("/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[3]/button")
        review.click()
        time.sleep(2)
        verify = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[2]/div[1]/input")
        verify.send_keys(info.card)
        save = driver.find_element_by_xpath("/html/body/div[6]/div/div[3]/button[2]")
        save.click()
        buy = True
    except:
        driver.refresh()
        continue
print("order placed")
        
        
        
        
