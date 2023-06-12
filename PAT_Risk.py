##this is for the task s-227-79

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


class PAT_risk:
    def PAT_risk():
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
        driver.find_element(By.ID,"Process").click()
        time.sleep(1)
        decision_reports_url = driver.current_url

        
        id_list = ['add_process_capture']
        flow = ["add","edit","delete"]
        
    
        try:
            add_element = driver.find_element(By.ID ,id_list[0])

            
        except:
            add_element = ""
            pass
        if add_element:
            print("button exists and no error")
            add_element.click()
            time.sleep(1)
            # add_element = driver.find_element(By.ID ,id_list[0])
            # add_element.click()
            unique_id = random.randint(1000, 9999)
            PAT_tool = "PAT"+str(unique_id)
            time.sleep(1)
            driver.find_element(By.NAME ,'name').send_keys(PAT_tool)
            time.sleep(0.2)
            driver.find_element(By.ID,"select2-agreement_type-container").click()
            time.sleep(1)
            try:
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                print("PAT already exists")
                pass
            except Exception as e:
                print(e)
                print("entered into exception")
                
            
                time.sleep(1)
                
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("agreement")
                search.send_keys(Keys.RETURN)
                driver.find_element(By.NAME,"description").send_keys("others")
                time.sleep(1)
                        
                driver.find_element(By.ID , 'btnsb').click()
                
                check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                # Get the HTML of the element
                html = check_status.get_attribute('outerHTML')
    #                     print(html,"this is html")
                if "alert alert-danger text-center alert-dismiss " in html:
                    print("PAT already exists")
                if "alert alert-success text-center alert-dismiss " in html:
                    print("new PAT created")
                driver.refresh()
                time.sleep(1)
                pass
            driver.find_element(By.XPATH , '//*[@id="agreementtable_filter"]/label/input').send_keys(PAT_tool)

            
            driver.find_element(By.ID ,'Configure').click()
            time.sleep(1)
            # subdecisionurl = driver.current_url
            driver.find_element(By.NAME,'add_node').click()
            time.sleep(1)
            unique_id = random.randint(1000, 9999)
            test = "short_sub"+str(unique_id)
            driver.find_element(By.NAME,'short').send_keys(test)
            driver.find_element(By.NAME,'full').send_keys('full_description')
            driver.find_element(By.ID,'sid').click()
            time.sleep(1)

            # Define the value of the name attribute
           
            # name = "short"

            # Construct the XPath expression for the table row
            row_xpath = f"//tr[td[b[contains(text(), '{test}')]]]"

            # Find the table row element using the XPath expression
            row = driver.find_element(By.XPATH, row_xpath)

            # Find the "add_node" button within the row by id and name, and click it
            add_node_button = row.find_element(By.XPATH, ".//a[@id='add_subnode' and @name='add_subnode']")
            add_node_button.click()

            unique_id = random.randint(1000, 9999)
            short_sub = "short_sub"+str(unique_id)

            time.sleep(1)
            driver.find_element(By.NAME,'short').send_keys(short_sub)
            driver.find_element(By.NAME,'full').send_keys('short_sub_description')
            driver.find_element(By.ID,'sid').click()
            time.sleep(1)
            
            
            # Wait for the table to be visible
            table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "agreement_id")))

            # Find all rows in the table
            rows = table.find_elements(By.XPATH, ".//tbody/tr")

            # Iterate over the rows to find the desired subnode
            for row in rows:
                    subnode_text = row.find_element(By.XPATH, "./td[2]").text.strip()
                    print(subnode_text)
                    if short_sub in subnode_text :
                        # Find the "Risks" button within the row
                        risks_button = row.find_element(By.XPATH, ".//a[@name='risks']")

                        # Click the "Risks" button
                        risks_button.click()
                        break
            risk_url = driver.current_url
            driver.find_element(By.NAME,'short_name').send_keys(test)
            driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/form/div[2]/div[2]/div/div/div/div[3]/div[2]').send_keys(test)
            # driver.find_element(By.ID,'unit_assertion').click()
            
            driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/form/div[3]/div[2]/div/span/span[1]/span/ul').click()
            search = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/form/div[3]/div[2]/div/span/span[1]/span/ul/li/input')
            search.send_keys("ac_accuracy")
            search.send_keys(Keys.RETURN)
            
            
            driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/form/div[4]/div[2]/div/span/span[1]/span/ul').click()
            search = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/form/div[4]/div[2]/div/span/span[1]/span/ul/li/input')
            search.send_keys("today")
            search.send_keys(Keys.RETURN)
            driver.find_element(By.ID,'riskSubmit').click()

            time.sleep(10)
            driver.refresh()
            

            # Find the table element
            table = driver.find_element(By.CLASS_NAME, "table")

            # Find all rows in the table
            rows = table.find_elements(By.TAG_NAME, "tr")

            # Iterate over the rows to find the desired "Short Name" value
            for row in rows:
                columns = row.find_elements(By.TAG_NAME, "td")
                if len(columns) > 1 and columns[1].text.strip() == test:
                    # Find the "Edit" button within the row
                    edit_button = row.find_element(By.CSS_SELECTOR, "a[title='Update']")

                    # Click the "Edit" button
                    edit_button.click()
                    break

            time.sleep(10)

            short_name = driver.find_element(By.NAME,'short_name')
            short_name.clear()
            upd = test+"update"
            short_name.send_keys(upd)

            driver.find_element(By.ID,'riskSubmit').click()

            time.sleep(10)
            
            # Find the table element
            table = driver.find_element(By.CLASS_NAME, "table")

            # Find all rows in the table
            rows = table.find_elements(By.TAG_NAME, "tr")

            # Iterate over the rows to find the desired "Short Name" value
            for row in rows:
                columns = row.find_elements(By.TAG_NAME, "td")
                if len(columns) > 1 and columns[1].text.strip() == upd:
                    # Find the "Edit" button within the row
                    Delete_button = row.find_element(By.CSS_SELECTOR, "a[title='Delete']")

                    # Click the "Edit" button
                    Delete_button.click()
                    break
            

            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(2)
            print("risk deleted successfully")
            
            

            
            
            


       
        else:
            print("ERROR:nobutton and error")
            

            
        return True