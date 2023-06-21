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



class EditMilestoneUpdates:
    def editMilestoneupdates():
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
        print_statements = []
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
            print_statements.append("Add assignemt page opened successfully")
            pass
        else:
            # logging.info("not able to open Add_assignemnt page")  # Log the message
            print("not able to open Add_assignemnt page")
            print_statements.append("not able to open Add_assignemnt page")

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
            print_statements.append("Add assignemt page opened successfully inside assignment")
            pass
        else:
            print("not able to open Add_assignemnt page inside assignment")
            print_statements.append("not able to open Add_assignemnt page inside assignment")
        time.sleep(0.8)
        driver.find_element(By.XPATH ,'/html/body/nav/div/div[2]/div[1]/div[1]/a/img').click()
        time.sleep(2)
        driver.get(current_url)
        driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div/div[1]/div/button[4]/span").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/a/i").click()
        driver.find_element(By.ID,"description_perf").send_keys("test")
        driver.find_element(By.ID,"perftimespent").send_keys(8)
        driver.find_element(By.ID,"perfdate").send_keys("30-05-2023")

        
        driver.find_element(By.XPATH,'//*[@id="currentstatus"]/option[3]').click()

        driver.find_element(By.XPATH,'//*[@id="addperformance"]/form[1]/div/div/div[2]/div[5]/div/button').click()
        # Get the HTML of the element
        # check_status = driver.find_element(By.XPATH,'/html/body/section/div/div[1]')
        # html = check_status.get_attribute('innerHTML')
        # print(html,"this is html")
        variable = ""
        # if "alert alert-danger text-center alert-dismiss " in html:
        #     print("Updates not updated")
        #     variable = "Updates not updated"
        # if "alert alert-success text-center alert-dismiss " in html:
        #     print("Updates updated")
        #     variable = "Updates updated"

        df = pd.DataFrame({"Print Statements": print_statements})

    # Save the DataFrame to an Excel file
        unique_id = random.randint(1000, 9999)
        excelsave = "edit_milestoneUpdate"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)
        time.sleep(20)
        return variable




