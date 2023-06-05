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



class AddClusterreport:
    def addClusterreport():
        # logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        user = "tharun"
        password = "tharun123"
        url = "https://old.anyaudit.co.in/login"
        driver,static_value = loginclass.loginfunction(user,password,url)
        print(static_value)
        # clicking on message otp
        driver.find_element(By.XPATH , '//*[@id="sign_in"]/div[3]/div/button').click()
        time.sleep(0.5)
        driver.find_element(By.ID,"bl14").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/div[1]/ul/li[6]/a").click()
        
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/a[2]/i").click()
        current_url = driver.current_url
        check_element = driver.find_element(By.ID,"select2-assignment_id-container")
        if check_element:
            # logging.info("Add assignemt page opened successfully")  # Log the message

            print("Add assignemt page opened successfully")
            pass
        else:
            # logging.info("not able to open Add_assignemnt page")  # Log the message
            print("not able to open Add_assignemnt page")

        # Access check
        driver.get("https://old.anyaudit.co.in/Navigation")
        driver.find_element(By.XPATH , '//*[@id="select2-selassignmentchange_dashboard-container"]').click()  
        new = driver.find_element(By.XPATH , '/html/body/span/span/span[1]/input')
        new.send_keys(3003)
        time.sleep(2)
        driver.find_element(By.XPATH , '/html/body/span/span/span[2]').click()
        time.sleep(2)
        driver.get(current_url)
        check_element = driver.find_element(By.ID,"select2-assignment_id-container")
        if check_element:          
            print("Add assignemt page opened successfully inside assignment")
            pass
        else:
            print("not able to open Add_assignemnt page inside assignment")
        time.sleep(0.8)
        driver.find_element(By.XPATH ,'/html/body/nav/div/div[2]/div[1]/div[1]/a/img').click()
        time.sleep(2)
        driver.get(current_url)
        driver.find_element(By.ID,"select2-assignment_id-container").click()
        time.sleep(1)
        # driver.find_element(By.ID,"select2-pro_company_id_x-container").click()
        select_box = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        select_box.send_keys("3003")
        select_box.send_keys(Keys.RETURN)
        # Wait for the dropdown options to appear
        driver.find_element(By.ID,"select2-cluster_category-container").click()
        select_box = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        select_box.send_keys("Genders")
        select_box.send_keys(Keys.RETURN)
        time.sleep(10)
        driver.find_element(By.ID,"select2-cluster_subcategory-container").click()
        select_box = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        select_box.send_keys("Male")
        select_box.send_keys(Keys.RETURN)
        time.sleep(1)
        try:                
            alert = driver.switch_to.alert
        except:
            alert = ""
            pass
        

        print(alert)
        if alert:
            alert.accept()
            variable = "Already exists"
        else:
            driver.find_element(By.ID,"btnSubmit").click()
            variable = "new cluster created"

        time.sleep(10)
        return variable




