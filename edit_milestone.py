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
import random
import sys
from login import loginclass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class EditMilestone:
    def editMilestone():
        # logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        user = "tharun"
        password = "tharun123"
        url = "https://old.anyaudit.co.in/login"
        driver,static_value = loginclass.loginfunction(user,password,url)
        print(static_value)
        # clicking on message otp
        driver.find_element(By.XPATH , '//*[@id="sign_in"]/div[3]/div/button').click()
        time.sleep(0.5)
        driver.find_element(By.ID,"myoffice").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,"/html/body/section/div[2]/div/div[1]/div/div[2]/div/div/ul/li[1]/ul/li[2]/a").click()
        
        time.sleep(1)
        driver.find_element(By.ID,"task_search").send_keys("test")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/div[3]/div/div[1]/div[2]/div/table/tbody/tr[6]/td[4]/a").click()
        time.sleep(10)
        
        window_handles = driver.window_handles

        # Switch to the newly opened tab (assuming it's the last in the list)
        new_tab_handle = window_handles[-1]
        driver.switch_to.window(new_tab_handle)
        time.sleep(1)
        current_url = driver.current_url
        print(current_url)
        check_element = driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div/div[1]/div/button[5]/span")
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
        check_element = driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div/div[1]/div/button[5]/span")
        if check_element:          
            print("Add assignemt page opened successfully inside assignment")
            pass
        else:
            print("not able to open Add_assignemnt page inside assignment")
        time.sleep(0.8)
        driver.find_element(By.XPATH ,'/html/body/nav/div/div[2]/div[1]/div[1]/a/img').click()
        time.sleep(2)
        driver.get(current_url)
        driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div/div[1]/div/button[5]/span").click()
        time.sleep(1)
        unique_id = random.randint(1000, 9999)
        test = "test"+str(unique_id)
        update_btn = driver.find_element(By.ID,'activity_name')
        update_btn.clear()

        driver.find_element(By.ID,'activity_name').send_keys(test)
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div/div[2]/div[3]/div[4]/div/div[2]/div/div/div/form/div/div/div[11]/button').click()

        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
        # Get the HTML of the element
        html = check_status.get_attribute('outerHTML')
    #                     print(html,"this is html")
        if "alert alert-danger text-center alert-dismiss " in html:
            print("Milestone is not updated")
            variable = "Milestone is not updated"
        if "alert alert-success text-center alert-dismiss " in html:
            print("Milestone updated successfully")
            variable = "Milestone updated successfully"


        time.sleep(10)
        return variable




