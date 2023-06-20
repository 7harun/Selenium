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
from CheckurlinAssignment import CheckUrlinAssignment


class CheckRecurring_milestone:
    def CheckRecurring_milestone():
        user = "madhukanth"
        password = "12345"
        url = "https://old.anyaudit.co.in/login"
        driver,static_value = loginclass.loginfunction(user,password,url)
        print(static_value)
        # clicking on message otp
        driver.find_element(By.XPATH , '//*[@id="sign_in"]/div[3]/div/button').click()
        time.sleep(0.5)
        driver.find_element(By.ID,"bl18").click()
        time.sleep(1)
        driver.find_element(By.ID,"Recurring").click()
        time.sleep(5)
        recurring_url = driver.current_url
        driver.find_element(By.ID,"addchild").click()
        time.sleep(5)
        Save=driver.find_element(By.ID ,"save")
        if Save:
            Save.click()
            time.sleep(5)
        else:
            print("Element not found.")
        try:
            field_element = driver.find_element(By.ID ,'task_name')
            cname = field_element.get_attribute('outerHTML')
            if "required" in cname:
                print("Please enter Task name")
            else:
                print("'ConditionName' Field is not mandatory or no validation error") 
                pass
            field_element = driver.find_element(By.NAME ,'comment')
            operator = field_element.get_attribute('outerHTML')
            if "required" in operator:
                print("Please enter description")
            else:
                print("Field is not mandatory or no validation error") 
                pass

        except:
               pass
        
        try:
            driver.get(recurring_url)
            time.sleep(1)
            add_element = driver.find_element(By.ID ,"addchild")
            add_element.click()
            print("check1")
            time.sleep(1)
            driver.find_element(By.ID ,'task_name').send_keys("test")
            
            time.sleep(0.2)
        
            # driver.find_element(By.ID,"select2-operator-container").click()
            # op_btn = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
            driver.find_element(By.NAME ,'comment').send_keys("madhu")
            # op_btn.send_keys(Keys.RETURN)
            time.sleep(0.5)
            # driver.find_element(By.NAME,"value_one").send_keys(j)
            # try:
            #     driver.find_element(By.NAME,"value_two").send_keys(j)
            # except:
            #     pass
            # driver.find_element(By.ID,"cond_desc").send_keys(j)                        
            
            time.sleep(2)
            driver.find_element(By.ID , 'save').click()
            time.sleep(1)
            
            # print(html)
            if "alert alert-danger text-center alert-dismiss " in html:
                print("already exists")
            if "alert alert-success text-center alert-dismiss " in html:
                print("new record created")
            #     message = element.text
        #     print(message)
        except Exception as e:
            print("error",e)
            time.sleep(100)





        # driver.find_element(By.ID ,'task_name').send_keys("madhu")
        # driver.find_element(By.NAME ,'comment').send_keys("madhu")
        # Save=driver.find_element(By.ID ,"save")
        # if Save:
        #     Save.click()
        #     time.sleep(5)
        # else:
        #     print("Element not found.")
        # time.sleep(5)

        # search=driver.find_element(By.XPATH ,"//input[contains(@aria-controls,'contactinfo')]")
        # if search:
        #     search.click()
        #     time.sleep(5)
        #     search.send_keys("madhu")
        #     time.sleep(5)
        # else:
        #     print("Element not found.")
        # time.sleep(100)