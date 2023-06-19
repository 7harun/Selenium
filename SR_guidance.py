##this is for the task s-227-102
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


class Standardised_reports_guidance:
    def standardised_reports_guidance():
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
        driver.find_element(By.ID,"Standardized").click()
        time.sleep(1)
        standardised_reports_url = driver.current_url
        # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standardised_reports_url,check_element_path)
        # print(checkinassignment)
        driver.get("https://old.anyaudit.co.in/Management/users")
        txtSearch = driver.find_element(By.ID  ,"txtSearch")
        driver.find_element(By.ID  ,"txtSearch").send_keys("tharun")
        txtSearch.send_keys(Keys.RETURN)
        time.sleep(1)
        # driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        # time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[14]/td[2]/input']
        id_list = ['add_standardized']
        flow = ["add","edit","delete"]
    
    
        driver.get(new_page_url)
#         driver.refresh()
        time.sleep(2)
        check_status = driver.find_element(By.XPATH  ,xpath_list_perm_page[0])
        # Get the HTML of the element
        html = check_status.get_attribute('outerHTML')
        print(html)
        if "checked" in html:
            print("checked")
            flag_add = "checked"
            driver.get(standardised_reports_url)
            try:
                add_element = driver.find_element(By.ID ,id_list[0])
#                 print("button exists and no error")
            except:
                add_element = ""
                pass
            if add_element:
                print("button exists and no error")
            
                add_element.click()

                time.sleep(1)
                unique_id = random.randint(1000, 9999)
                Stand_r = "SR_"+str(unique_id)
                driver.find_element(By.NAME ,'report_name').send_keys(Stand_r)
                driver.find_element(By.XPATH , '//*[@id="reort_valid"]/div/div[4]/div/div/span/span[1]/span').click()  
                new = driver.find_element(By.XPATH , '/html/body/span/span/span[1]/input')
                new.send_keys("Others")
                new.send_keys(Keys.RETURN)
                time.sleep(2)
                driver.find_element(By.ID , 'btnsb').click()
                
                check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                # Get the HTML of the element
                html = check_status.get_attribute('outerHTML')
#                     print(html,"this is html")
                if "alert alert-danger text-center alert-dismiss " in html:
                    print("Standardised Report already exists")
                if "alert alert-success text-center alert-dismiss " in html:
                    print("new Standardised Report created")

                time.sleep(2)
                driver.find_element(By.XPATH , '//*[@id="report_active_filter"]/label/input').send_keys(Stand_r)
                driver.find_element(By.NAME ,'config').click()
                time.sleep(3)
                driver.find_element(By.NAME ,'add_questions').click()
                quest = Stand_r+"_question"
                driver.find_element(By.NAME ,'q_short').send_keys(quest)
                driver.find_element(By.XPATH ,'/html/body/section/div/div/div/div/div/form/div[2]/div[2]/div/div/div/div[3]/div[2]/p/br').send_keys(quest)
                time.sleep(2)
                driver.find_element(By.NAME ,'btnsb').click()
                time.sleep(3)


                # Wait for the table to be visible
                table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "question_table")))

                # Find all rows in the table
                rows = table.find_elements(By.XPATH, ".//tbody/tr")

                # Iterate over the rows to find the desired subnode
                for row in rows:
                        guidance_text = row.find_element(By.XPATH, "./td[2]").text.strip()
                        print(guidance_text)
                        if quest in guidance_text :
                            # Find the "Risks" button within the row
                            guidance_button = row.find_element(By.XPATH, ".//a[@name='guidance']")

                            # Click the "Risks" button
                            guidance_button.click()
                            break
                            

                short = Stand_r+"_short"
                
                driver.find_element(By.NAME ,'short').send_keys(short)
                driver.find_element(By.NAME ,'guidance_notes_name').send_keys(short)
                driver.find_element(By.NAME ,'reference').send_keys(short)
                driver.find_element(By.XPATH ,'/html/body/section/div/div/div/div/div/form/div[4]/div[2]/div/div/div/div[3]/div[2]').send_keys(short)
                time.sleep(2)
                button = driver.find_element(By.NAME ,'btnsb')
                driver.execute_script("arguments[0].click();", button)

                time.sleep(2)

                # Wait for the table to be visible
                table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "guidance_table")))

                # Find all rows in the table
                rows = table.find_elements(By.XPATH, ".//tbody/tr")

                # Iterate over the rows to find the desired subnode
                for row in rows:
                        guidance_text = row.find_element(By.XPATH, "./td[2]").text.strip()
                        print(guidance_text)
                        if short in guidance_text :
                            # Find the "Risks" button within the row
                            guidance_button = row.find_element(By.XPATH, ".//a[@name='edit']")

                            # Click the "Risks" button
                            guidance_button.click()
                            break

                time.sleep(1)
                upd = short+"_update"
                short = driver.find_element(By.NAME ,'short')
                short.clear()
                short.send_keys(upd)
                guidance_notes_name = driver.find_element(By.NAME ,'guidance_notes_name')
                guidance_notes_name.clear()
                guidance_notes_name.send_keys(upd)
                time.sleep(3)
                button = driver.find_element(By.NAME ,'btnsb')
                driver.execute_script("arguments[0].click();", button)


                time.sleep(1)

                # Wait for the table to be visible
                table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "guidance_table")))

                # Find all rows in the table
                rows = table.find_elements(By.XPATH, ".//tbody/tr")

                # Iterate over the rows to find the desired subnode
                for row in rows:
                        guidance_text = row.find_element(By.XPATH, "./td[2]").text.strip()
                        print(guidance_text)
                        if upd in guidance_text :
                            # Find the "Risks" button within the row
                            guidance_button = row.find_element(By.XPATH, ".//a[@name='delete']")

                            # Click the "Risks" button
                            guidance_button.click()
                            break

                time.sleep(1)
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                


                

                


                    

                    
                    

                    


            else:
                print("ERROR:nobutton and error")
            

            
        else:
            print("unchecked")
            flag = "unchecked"
            driver.get(standardised_reports_url)
            
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