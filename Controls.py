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


class Controls:
    def controls():
        # logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        user = "tharun"
        password = "tharun123"
        url = "https://old.anyaudit.co.in/login"
        driver,static_value = loginclass.loginfunction(user,password,url)
        print(static_value)
        # clicking on message otp
        driver.find_element(By.XPATH , '//*[@id="sign_in"]/div[3]/div/button').click()
        time.sleep(0.5)
        driver.find_element(By.ID,"bl18").click()
        time.sleep(1)
        driver.find_element(By.ID,"Controls").click()
        time.sleep(1)
        standardised_reports_url = driver.current_url
        # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standardised_reports_url,check_element_path)
        # print(checkinassignment)
        # new_page_url = driver.current_url
        id_list = ['addtype','edit','mark_inactive']
        flow = ["add","edit","delete"]
        print_statements = []
        for i in range(0,len(id_list)):
        
            driver.get(standardised_reports_url)          

            if flow[i] == "add":
                try:
                    add_element = driver.find_element(By.ID ,id_list[i])
                except:
                    add_element = ""
                    print("no add element button")
                    print_statements.append("no add element button")
                    pass
                add_element.click()
                time.sleep(0.2)

                driver.find_element(By.ID , 'btnsb').click()
                #Control Name
                field_element = driver.find_element(By.NAME ,'category_name')
                Control_name = field_element.get_attribute('outerHTML')
                if "required" in Control_name:
                    print("'Area of Audit' Field is mandatory. Please fill it.")
                    print_statements.append("'Area of Audit' Field is mandatory. Please fill it.")
                else:
                    print("'Area of Audit' Field is not mandatory or no validation error")
                    print_statements.append("'Area of Audit' Field is not mandatory or no validation error")
                    pass
                    
                input_element = ["..","alpha1","alpha@1",12345]
                for j in input_element:
                    # driver.get(decision_reports_url)
                    try:
                        
                        driver.get(standardised_reports_url)
                        time.sleep(1)
                        add_element = driver.find_element(By.ID ,id_list[i])
                        add_element.click()
                        print("check1")
                        time.sleep(1)
                        driver.find_element(By.NAME ,'category_name').send_keys(j)
                        time.sleep(0.2)
                        driver.find_element(By.ID , 'btnsb').click()
                    except Exception as e:
                        print("error",e)
                driver.get(standardised_reports_url)
                time.sleep(1)
                add_element = driver.find_element(By.ID ,id_list[i])
                add_element.click()
                time.sleep(1)


                driver.find_element(By.NAME ,'category_name').send_keys("new_control")
                time.sleep(0.2)
                driver.find_element(By.ID , 'btnsb').click()
            elif flow[i] == "edit":
                unique_id = random.randint(1000, 9999)
                test = "test"+str(unique_id)
                driver.find_element(By.XPATH , '//*[@id="controlid_filter"]/label/input').send_keys("new_control")
                driver.find_element(By.ID ,'edit').click()
                decision_btn = driver.find_element(By.NAME ,'category_name')
                decision_btn.clear()
                decision_btn.send_keys(test)
                driver.find_element(By.ID , 'btnsb').click()
            elif flow[i] == "delete":
                driver.find_element(By.XPATH , '//*[@id="controlid_filter"]/label/input').send_keys(test)
#                     search_btn.send_keys("new_checklist")
                time.sleep(0.5)
                delete_btn = driver.find_element(By.NAME ,'mark_inactive')
                delete_btn.click()
                time.sleep(0.5)
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                df = pd.DataFrame({"Print Statements": print_statements})

    # Save the DataFrame to an Excel file
        unique_id = random.randint(1000, 9999)
        excelsave = "Controls"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)
        return True