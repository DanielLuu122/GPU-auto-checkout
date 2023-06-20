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
print("asdf")
