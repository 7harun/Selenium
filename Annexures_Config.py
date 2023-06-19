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


class Annexures_config:
    def annexures_config():
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
        driver.find_element(By.ID,"Annexures").click()
        time.sleep(1)
        annexures_reports_url = driver.current_url
        
        driver.get("https://old.anyaudit.co.in/Management/users")
        search = driver.find_element(By.ID  ,"txtSearch")
        search.send_keys("tharun")
        search.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[1]/td[2]/input']
        id_list = ['add_annexure','add_annexure','add_annexure']
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
            driver.get(annexures_reports_url)
            try:
                add_element = driver.find_element(By.ID ,id_list[0])
#                 print("button exists and no error")
            except:
                add_element = ""
                pass
            add_element.click()
            time.sleep(0.2)

            unique_id = random.randint(1000, 9999)
            annexure = "annexure_"+str(unique_id)

            
            driver.find_element(By.NAME ,'annexure_name').send_keys(annexure)
            time.sleep(0.2)
            driver.find_element(By.ID,"select2-chapters-container").click()
            time.sleep(1)
            try:
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(2)
                print("annexure already exists")
                variable = ""
                
            except Exception as e:
                print(e)
                variable = "add_all_items"
                print("entered into exception")
                pass
            if variable == "add_all_items":
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("others")
                search.send_keys(Keys.RETURN)
                driver.find_element(By.ID,"select2-area_audit_id-container").click()
                time.sleep(1)
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("Audit of Account Receivable & Payable")
                search.send_keys(Keys.RETURN)

                driver.find_element(By.NAME ,'annexure_description').send_keys("New_description")                 
                driver.find_element(By.ID , 'btnsb').click()
                
                check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                # Get the HTML of the element
                html = check_status.get_attribute('outerHTML')
#                     print(html,"this is html")
                if "alert alert-danger text-center alert-dismiss " in html:
                    print("Annexure already exists")
                if "alert alert-success text-center alert-dismiss " in html:
                    print("new Annexure created")
            time.sleep(2)
            driver.find_element(By.XPATH , '//*[@id="annextureact_filter"]/label/input').send_keys(annexure)
            driver.find_element(By.ID ,'configure').click()
            time.sleep(1)
            annexures_reports_url = driver.current_url
            for i in range(0,len(id_list)):
                if add_element:
                    print("button exists and no error")
                    if flow[i] == "add":
                        
                        # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
                        # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,annexures_reports_url,check_element_path)
                        # print(checkinassignment)
                        driver.get(annexures_reports_url)
                        driver.find_element(By.ID ,'add_under').click()
                        time.sleep(1)
                        driver.find_element(By.ID , 'sid').click()
                        try:
                            # Find the field element that contains the mandatory star mark
                            #fieldname
                            field_element = driver.find_element(By.NAME, 'fieldname')
                            fieldname = field_element.get_attribute('outerHTML')
                            if "required" in fieldname:
                                print("'fieldname' Field is mandatory. Please fill it.")
                            else:
                                print("'fieldname' Field is not mandatory or no validation error") 
                                pass

                            field_element = driver.find_element(By.NAME, 'fieldtype')
                            fieldtype = field_element.get_attribute('outerHTML')
                            if "required" in fieldname:
                                print("'fieldtype' Field is mandatory. Please fill it.")
                            else:
                                print("'fieldtype' Field is not mandatory or no validation error") 
                                pass
                        except Exception as e:
                            print("ERROR:not able to check mandatory check")
                            print(e)
                            pass
                        driver.refresh()
                        driver.find_element(By.ID ,'add_under').click()
                        time.sleep(1)
                        driver.find_element(By.NAME ,'fieldname').send_keys("testing2")
                        driver.find_element(By.ID,"select2-fieldtype-container").click()
                        time.sleep(0.2)
                        search = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
                        time.sleep(0.2)
                        search.send_keys("numerical")
                        time.sleep(0.2)
                        search.send_keys(Keys.ENTER)
                        time.sleep(0.2)
                        driver.find_element(By.NAME,"sid").click()                                        
                        time.sleep(2)
                            
                    elif flow[i] == "edit":
                        driver.refresh()
                        unique_id = random.randint(1000, 9999)
                        test = "test"+str(unique_id)
                        # Find the row with the field name "sdfsf"
                        field_name = "testing2"
                        row_xpath = f"//tr[td[text()='{field_name}']]"
                        row = driver.find_element(By.XPATH, row_xpath)

                        # Find the edit button within the row and click it
                        edit_button_xpath = ".//a[@title='Edit']"
                        edit_button = row.find_element(By.XPATH, edit_button_xpath)
                        edit_button.click()
                        time.sleep(1)
                        search = driver.find_element(By.NAME ,'fieldname')
                        search.clear()
                        search.send_keys(test)
                        time.sleep(1)
                        driver.find_element(By.ID,"select2-fieldtype-container").click()
                        time.sleep(0.2)
                        search = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
                        time.sleep(0.2)
                        search.send_keys("numerical")
                        time.sleep(0.2)
                        search.send_keys(Keys.ENTER)
                        time.sleep(0.2)
                        driver.find_element(By.NAME,"sid").click() 
                        time.sleep(2)

                        
                    elif flow[i] == "delete":
                        time.sleep(2)
                        driver.refresh()
                         # Find the row with the field name "sdfsf"
                        # field_name = test
                        row_xpath = f"//tr[td[text()='{test}']]"
                        row = driver.find_element(By.XPATH, row_xpath)
                        # Find the delete button within the row and click it
                        delete_button_xpath = ".//a[@title='Delete']"
                        delete_button = row.find_element(By.XPATH, delete_button_xpath)
                        delete_button.click()
                        
                        alert = driver.switch_to.alert
                        alert.accept()
                        time.sleep(2)


                else:
                    print("ERROR:nobutton and error")
                

                
            else:
                print("unchecked")
                flag = "unchecked"
                driver.get(annexures_reports_url)
                
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