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

class CheckUrlinAssignment:
    def checkurlinassignment(driver,current_url,check_element_path):
        driver.get("https://old.anyaudit.co.in/Navigation")
        driver.find_element(By.XPATH , '//*[@id="select2-selassignmentchange_dashboard-container"]').click()  
        new = driver.find_element(By.XPATH , '/html/body/span/span/span[1]/input')
        new.send_keys(3003)
        time.sleep(2)

        print_statements = []

        driver.find_element(By.XPATH , '/html/body/span/span/span[2]').click()
        time.sleep(2)
        driver.get(current_url)
        try:
            check_element = driver.find_element(By.XPATH,check_element_path)
        except:
            check_element = ""
            pass
        if check_element:          
            print("Add assignemt page opened successfully inside assignment")
            print_statements.append("Add assignemt page opened successfully inside assignment")
            result = "Add assignemt page opened successfully inside assignment"
            time.sleep(0.8)
            driver.find_element(By.XPATH ,'/html/body/nav/div/div[2]/div[1]/div[1]/a/img').click()
            time.sleep(2)
            pass
        else:
            print("not able to open Add_assignemnt page inside assignment")
            print_statements.append("not able to open Add_assignemnt page inside assignment")
            result = "not able to open Add_assignemnt page inside assignment"

            df = pd.DataFrame({"Print Statements": print_statements})

    # Save the DataFrame to an Excel file
        unique_id = random.randint(1000, 9999)
        excelsave = "CheckurlinAssignment"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)
       
        return result