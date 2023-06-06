import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import os,glob
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from lxml import etree
import time 
import sys
import threading as Thread
import warnings
warnings.filterwarnings("ignore")



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://old.anyaudit.co.in/login")
driver.maximize_window()
username_box = driver.find_element(By.NAME , "username")
username_box.send_keys("tharun")
password_box = driver.find_element(By.NAME, "password")
password_box.send_keys("tharun123")
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


input_element = ["",".","alpa1","alpha@1",12345]
for i in input_element:
    driver.get("https://old.anyaudit.co.in/Clusters/clusters/")
    driver.find_element(By.XPATH , "/html/body/div[2]/div[2]/div/div/a[2]").click()


    try:
        se =  driver.find_element(By.XPATH , "/html/body/div[14]/div/div/div[2]/div/form/div/div[1]/div/div/input")
        se.send_keys(i)
        se.send_keys(Keys.ENTER)
        try:
            category_name_input = driver.find_element(By.ID ,"category_name") 
            category_name_input.submit() 
            # Switch to the alert 
            alert = Alert(driver) 
            # Capture the alert message 
            alert_message = alert.text 
            print(alert_message)
        except Exception as e1:
            print(e1)
            pass


        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[2]')
         # Get the HTML of the element
        html = check_status.get_attribute('innerHTML')
        print(html)
        if "alert alert-danger text-center alert-dismiss " in html:
            print("already exists")
        if "alert alert-success text-center alert-dismiss " in html:
            print("new record created")
        #     message = element.text
    #     print(message)
    except Exception as e:
        print("error",e)

