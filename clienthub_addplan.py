import time 
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from lxml import etree
# import logging
import sys
from login import loginclass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random


class client_add_plan:
    def client_add_plan():
        # logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        user = "tharun"
        password = "tharun123"
        url = "https://old.anyaudit.co.in/login"
        driver,static_value = loginclass.loginfunction(user,password,url)
        print(static_value)
        # clicking on message otp
        driver.find_element(By.XPATH , '//*[@id="sign_in"]/div[3]/div/button').click()
        driver.find_element(By.XPATH,'//*[@id="tree2"]/li[2]').click()
        time.sleep(0.5)
        driver.find_element(By.NAME,'client_hub').click()
        time.sleep(0.5)
        user_field = driver.find_element(By.ID,"select2-clienthubselectajax-container")
        user_field.click()
        # time.sleep(10)
        user_input = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
        user_input.send_keys("testing client")
        time.sleep(2)
        user_input.send_keys(Keys.RETURN)
        time.sleep(0.2)
        driver.find_element(By.NAME,"e_edit").click()
        time.sleep(1)
        search = driver.find_element(By.NAME,"cname")
        search.clear()
        unique_id = random.randint(1000, 9999)
        test = "test"+str(unique_id)
        search.send_keys(test)
        driver.find_element(By.NAME,"submit").click()     
        

        
        
        return True




