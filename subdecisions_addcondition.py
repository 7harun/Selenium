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


class SubDecisions_addcondition:
    def subdecisions_addcondition():
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
        driver.find_element(By.ID,"Decisions").click()
        time.sleep(1)
        decision_reports_url = driver.current_url
        # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standardised_reports_url,check_element_path)
        # print(checkinassignment)
        driver.get("https://old.anyaudit.co.in/Management/users")
        search = driver.find_element(By.ID  ,"txtSearch")
        search.send_keys("tharun")
        search.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="38"]/div/div/table/tbody/tr[1]/td[2]/input']
        id_list = ['add_decisions']
        flow = ["add","edit","delete"]
        
        time.sleep(2)
        driver.get(new_page_url)
#         driver.refresh()
        time.sleep(0.5)
        check_status = driver.find_element(By.XPATH  ,xpath_list_perm_page[0])
        # Get the HTML of the element
        html = check_status.get_attribute('outerHTML')
        print(html)
        if "checked" in html:
            print("checked")
            flag_add = "checked"
            driver.get(decision_reports_url)
            try:
                add_element = driver.find_element(By.ID ,id_list[0])

                add_element.click()
            except:
                add_element = ""
                pass
            if add_element:
                print("button exists and no error")
                time.sleep(1)
                # add_element = driver.find_element(By.ID ,id_list[0])
                # add_element.click()
                time.sleep(1)
                driver.find_element(By.ID ,'dec_name').send_keys("new_decision")
                time.sleep(0.2)
                driver.find_element(By.ID,"select2-dec_type-container").click()
                time.sleep(1)
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("normal")
                search.send_keys(Keys.RETURN)
                driver.find_element(By.ID,"select2-chapters-container").click()
                time.sleep(1)
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("others")
                search.send_keys(Keys.RETURN)

                driver.find_element(By.ID,"select2-area_audit_id-container").click()
                time.sleep(1)
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("Audit of Account Receivable & Payable")
                search.send_keys(Keys.RETURN)

                driver.find_element(By.NAME ,'dec_description').send_keys("New_description")                 
                driver.find_element(By.ID , 'btnsb').click()
                
                check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                # Get the HTML of the element
                html = check_status.get_attribute('outerHTML')
#                     print(html,"this is html")
                if "alert alert-danger text-center alert-dismiss " in html:
                    print("Decision already exists")
                if "alert alert-success text-center alert-dismiss " in html:
                    print("new Decision created")
                driver.refresh()
                time.sleep(1)
                driver.find_element(By.XPATH , '//*[@id="decisionid_filter"]/label/input').send_keys("new_decision")
                driver.find_element(By.ID ,'configure').click()
                time.sleep(1)
                subdecisionurl = driver.current_url
                driver.find_element(By.XPATH,'//*[@id="navbar1"]/div[2]/div/div/a[2]').click()
                time.sleep(1)
                driver.find_element(By.NAME,'subdec_name').send_keys('new_decision')
                driver.find_element(By.NAME,'subdec_desc').send_keys('new_decision_description')
                driver.find_element(By.ID,'btnsb').click()
                time.sleep(0.1)
                check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                # Get the HTML of the element
                html = check_status.get_attribute('outerHTML')
                if "alert alert-danger text-center alert-dismiss " in html:
                    print("subDecision already exists")
                    driver.get(subdecisionurl)
                if "alert alert-success text-center alert-dismiss " in html:
                    print("new subDecision created")
                # Find the row with the name "new_decision"
                driver.refresh()
                time.sleep(2)
                # Find the row with the name "new_decision"
                name = "new_decision"
                row_xpath = f"//tr[td[b[contains(text(), '{name}')]]]"
                row = driver.find_element(By.XPATH, row_xpath)

                # Find the "+" button within the row by id and name and click it
                add_conditions_button = row.find_element(By.XPATH, ".//a[@id='add_conditions' and @name='add_conditions']")
                add_conditions_button.click()
                time.sleep(1)
                driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div[2]/form/div[2]/div[2]/div/div/span/span[1]/span').click()
                time.sleep(0.2)
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("12345")
                search.send_keys(Keys.RETURN)
                driver.find_element(By.ID,"btnsb").click() 
                time.sleep(0.2)
                check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                # Get the HTML of the element
                html = check_status.get_attribute('outerHTML')
                if "alert alert-danger text-center alert-dismiss " in html:
                    print("condition already exists")
                    driver.get(subdecisionurl)
                if "alert alert-success text-center alert-dismiss " in html:
                    print("new condition created")

                      
                
            else:
                print("ERROR:nobutton and error")
            

            
        else:
            print("unchecked")
            flag = "unchecked"
            driver.get(decision_reports_url)
            
            try:
                add_element = driver.find_element(By.ID ,id_list[i])
#                 if not add_element:
#                 print("button not  exists and no error")
            except:
                add_element = ""
                pass
            print(add_element,"this is add_elelmtn")
            if add_element:
                print("ERROR:button exists and error")
            else:
                print("nobutton and no error")
        return True