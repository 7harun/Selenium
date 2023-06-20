import time 
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from CheckurlinAssignment import CheckUrlinAssignment
from lxml import etree
# import logging
import random
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
        print_statements = []
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
            print_statements.append("Add assignemt page opened successfully")
            pass
        else:
            # logging.info("not able to open Add_assignemnt page")  # Log the message
            print("not able to open Add_assignemnt page")
            print_statements.append("not able to open Add_assignemnt page")
        standardised_reports_url = driver.current_url
        check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standardised_reports_url,check_element_path)
        print(checkinassignment)
        driver.get(standardised_reports_url)
        time.sleep(0.8)
        
        # driver.find_element(By.ID,"select2-pro_company_id_x-container").click()


        driver.find_element(By.ID ,'btnSubmit').click()
        time.sleep(0.5)
        try:
            # Find the field element that contains the mandatory star mark
            #assignment_id
            field_element = driver.find_element(By.NAME ,'assignment_id')
            assignment_id = field_element.get_attribute('outerHTML')
            if "required" in assignment_id:
                print("'assignment_id' Field is mandatory. Please fill it.")
                print_statements.append("'assignment_id' Field is mandatory. Please fill it.")
                
            else:
                print("'assignment_id' Field is not mandatory or no validation error") 
                print_statements.append("'assignment_id' Field is not mandatory or no validation error")
                pass

            #  cluster_category
            field_element = driver.find_element(By.NAME ,'cluster_category')
            cluster_category = field_element.get_attribute('outerHTML')
            if "required" in cluster_category:
                print("'cluster_category' Field is mandatory. Please fill it.")
                print_statements.append("'cluster_category' Field is mandatory. Please fill it.")
            else:
                print("'cluster_category' Field is not mandatory or no validation error")
                print_statements.append("'cluster_category' Field is not mandatory or no validation error")
                pass

             #  cluster_subcategory
            field_element = driver.find_element(By.NAME ,'cluster_subcategory')
            cluster_subcategory = field_element.get_attribute('outerHTML')
            if "required" in cluster_subcategory:
                print("'cluster_subcategory' Field is mandatory. Please fill it.")
                print_statements.append("cluster_subcategory' Field is mandatory. Please fill it.")
            else:
                print("'cluster_subcategory' Field is not mandatory or no validation error")
                print_statements.append("'cluster_subcategory' Field is not mandatory or no validation error") 
                pass

        except:
            pass
        time.sleep(1)
        driver.get(standardised_reports_url)
        time.sleep(1)
        driver.find_element(By.ID,"select2-assignment_id-container").click()
        time.sleep(1)
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


        df = pd.DataFrame({"Print Statements": print_statements})

    # Save the DataFrame to an Excel file
        unique_id = random.randint(1000, 9999)
        excelsave = "AddCluster_Assignment"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)
        return variable




