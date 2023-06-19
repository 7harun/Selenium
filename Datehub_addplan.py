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
from CheckurlinAssignment import CheckUrlinAssignment
from selenium.webdriver.support.ui import WebDriverWait



class Datehub_add_plan:
    def datehub_add_plan():
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
        driver.find_element(By.XPATH,'//*[@id="tree2"]/li[2]/ul/li[6]/a').click()
        time.sleep(0.5)
        date_field = driver.find_element(By.ID,"seldate_datehub")
        date_field.send_keys("09062023")
        time.sleep(0.5)
        driver.find_element(By.NAME,'p_plans').click()
        time.sleep(0.2)
        driver.find_element(By.NAME,'fa_plus').click()
        standardised_reports_url = driver.current_url
        check_element = driver.find_element(By.ID,"select2-planuserclient-container")
        if check_element:
            # logging.info("Add assignemt page opened successfully")  # Log the message

            print("Add plan page opened successfully")
            pass
        else:
            # logging.info("not able to open Add_assignemnt page")  # Log the message
            print("not able to open add plan page")

       

        # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standardised_reports_url,check_element_path)
        # print(checkinassignment)
        driver.get(standardised_reports_url)
        try:
            driver.find_element(By.NAME,"save")
            field_element = driver.find_element(By.NAME,"planuserclient")
            planuserclient = field_element.get_attribute('outerHTML')
            if "required" in planuserclient:
                print("'planuserclient' Field is mandatory. Please fill it.")
            else:
                print("'planuserclient' Field is not mandatory or no validation error") 
                pass

            field_element = driver.find_element(By.NAME,"planuserwork")
            planuserwork = field_element.get_attribute('outerHTML')
            if "required" in planuserwork:
                print("'planuserwork' Field is mandatory. Please fill it.")
            else:
                print("'planuserwork' Field is not mandatory or no validation error") 
                pass

            field_element = driver.find_element(By.NAME,"tasklist")
            tasklist = field_element.get_attribute('outerHTML')
            if "required" in tasklist:
                print("'tasklist' Field is mandatory. Please fill it.")
            else:
                print("'tasklist' Field is not mandatory or no validation error") 
                pass

            field_element = driver.find_element(By.NAME,"tomdate")
            tomdate = field_element.get_attribute('outerHTML')
            if "required" in tomdate:
                print("'date' Field is mandatory. Please fill it.")
            else:
                print("'date' Field is not mandatory or no validation error") 
                pass

            field_element = driver.find_element(By.NAME,"planuser_1")
            planuser_1 = field_element.get_attribute('outerHTML')
            if "required" in planuser_1:
                print("'user' Field is mandatory. Please fill it.")
            else:
                print("'user' Field is not mandatory or no validation error") 
                pass

            field_element = driver.find_element(By.NAME,"useresthrs")
            useresthrs = field_element.get_attribute('outerHTML')
            if "required" in useresthrs:
                print("'EST hours' Field is mandatory. Please fill it.")
            else:
                print("'EST hours' Field is not mandatory or no validation error") 
                pass

            field_element = driver.find_element(By.NAME,"planuserdescription")
            planuserdescription = field_element.get_attribute('outerHTML')
            if "required" in planuserdescription:
                print("'Description' Field is mandatory. Please fill it.")
            else:
                print("'Description' Field is not mandatory or no validation error") 
                pass     
        except:
            pass
        

        driver.refresh()
        planuserclient = driver.find_element(By.ID,"select2-planuserclient-container")
        planuserclient.click()
        search = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        search.send_keys("Anyaudit")
        search.send_keys(Keys.RETURN)
        time.sleep(5)

        planuserwork = driver.find_element(By.XPATH,'//*[@id="mainForm1"]/div/div/div[2]/div[2]/span[2]/span[1]/span')
        planuserwork.click()
        search = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        search.send_keys("Download")
        search.send_keys(Keys.RETURN)
        time.sleep(1)

        tasklist = driver.find_element(By.ID,"select2-tasklist-container")
        tasklist.click()
        search = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        search.send_keys("quest_")
        search.send_keys(Keys.RETURN)
        time.sleep(1)

        
        driver.find_element(By.ID,'tomdate').send_keys("09-06-2023")
        time.sleep(1)


        planuser_1 = driver.find_element(By.ID,"select2-planuser-container")
        planuser_1.click()
        search = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        search.send_keys("bharath")
        search.send_keys(Keys.RETURN)
        time.sleep(1)

        
        driver.find_element(By.ID,'useresthrs').send_keys("8")
        time.sleep(1)

        driver.find_element(By.ID,'planuserdescription').send_keys("description")
        time.sleep(1)


        driver.find_element(By.NAME,"save").click()
        time.sleep(5)






        


        



        return True




