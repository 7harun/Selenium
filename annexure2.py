import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import os,glob
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from lxml import etree
import time 
import sys
import threading as Thread
import warnings
warnings.filterwarnings("ignore")




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://old.anyaudit.co.in/login")
#driver.maximize_window()
username_box = driver.find_element(By.NAME , "username")
username_box.send_keys("swaroop")
password_box = driver.find_element(By.NAME, "password")
password_box.send_keys("09876")
driver.find_element(By.XPATH  , '//*[@id="sign_in"]/div[3]/div/button').click()
time.sleep(1)
html = driver.page_source
# print(html)
tree = etree.HTML(html)

try:
    element = tree.xpath('//*[@id="userlogin"]/div[1]')
    if element:
        static_value = element[0].text.strip()
#         print("Static Display Value:", static_value)
        if static_value =="Invalid Username or Password!":
            driver.close()
            print(static_value)
    else:
        print("Logged in successfully")
#         print(elemtn[0])
except:
    pass
    
driver.find_element(By.XPATH , '//*[@id="sign_in"]/div[3]/div/button').click()

#Going directly to annexure home page


driver.get("https://old.anyaudit.co.in/Annexures/annexure")

data = {}
try:    
    driver.find_element(By.XPATH,'//*[@id="navbar1"]/div[1]/div').click()
    print("Page opened successfully and Label name is present")
    data["behaviour"] = "success"
    time.sleep(1)
except Exception:
    data["behaviour"] = "whitescreen"
    time.sleep(1)


    
#add button

data = {}
try:    
    driver.find_element(By.XPATH,'//*[@id="navbar1"]/div[2]/div/div/a[2]').click()
    print("Add Button access successfull")
    data["behaviour"] = "success"
    time.sleep(1)
except Exception:
    data["behaviour"] = "whitescreen"
    time.sleep(1)    


s = driver.find_element(By.XPATH, '//*[@id="btnsb"]')
time.sleep(1)
s.click()

# Find the field element that contains the mandatory star mark
#name
field_element = driver.find_element(By.XPATH, '//*[@id="annex"]/div/div/div[1]/div')
has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
is_mandatory = "*" in field_element.text

if has_validation_error or is_mandatory:
     print("'Name' Field is mandatory. Please fill it.")
else:
#     Field is not mandatory or no validation error
    pass


#chapter
field_element = driver.find_element(By.XPATH, '//*[@id="annex"]/div/div/div[2]/div')
has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
is_mandatory = "*" in field_element.text

if has_validation_error or is_mandatory:
     print("'Chapter' Field is mandatory. Please fill it.")
else:
#     Field is not mandatory or no validation error
    pass



#area of audit
field_element = driver.find_element(By.XPATH, '//*[@id="annex"]/div/div/div[3]/div')

#field_name = field_element.get_attribute("Area of audit")
# Checking if the field has any validation error or highlighting indicating it is mandatory
has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
is_mandatory = "*" in field_element.text

if has_validation_error or is_mandatory:
     print("'Area of audit' Field is mandatory. Please fill it.")
else:
#     Field is not mandatory or no validation error
    pass


#description
field_element = driver.find_element(By.XPATH, '//*[@id="annex"]/div/div/div[4]/div')
has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
is_mandatory = "*" in field_element.text

if has_validation_error or is_mandatory:
     print("'Description' Field is mandatory. Please fill it.")
else:
#     Field is not mandatory or no validation error
    pass

