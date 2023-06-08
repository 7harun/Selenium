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


class Custom_Reports:
    def cutomreports():
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
        driver.find_element(By.ID,"Customized").click()
        time.sleep(1)
        check_url = driver.current_url
        check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,check_url,check_element_path)
        print(checkinassignment)
        driver.get("https://old.anyaudit.co.in/Management/users")
        search = driver.find_element(By.ID  ,"txtSearch")
        search.send_keys("tharun")
        search.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[10]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[42]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[26]/td[2]/input']
        id_list = ['add_custom','edit','inactive']
        flow = ["add","edit","delete"]
        for i in range(0,len(xpath_list_perm_page)):
            time.sleep(2)
            driver.get(new_page_url)
    #         driver.refresh()
            time.sleep(0.5)
            check_status = driver.find_element(By.XPATH  ,xpath_list_perm_page[i])
            # Get the HTML of the element
            html = check_status.get_attribute('outerHTML')
            print(html)
            if "checked" in html:
                print("checked")
                flag_add = "checked"
                driver.get(check_url)
                try:
                    add_element = driver.find_element(By.ID ,id_list[i])
    #                 print("button exists and no error")
                except:
                    add_element = ""
                    pass
                if add_element:
                    print("button exists and no error")
                    if flow[i] == "add":
                        add_element.click()
                        time.sleep(0.2)

                        driver.find_element(By.NAME ,'add').click()
                        try:
                            # Find the field element that contains the mandatory star mark
                            #Draft Name
                            field_element = driver.find_element(By.NAME ,'draft')
                            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
                            is_mandatory = "*" in field_element.text

                            if has_validation_error or is_mandatory:
                                print("'Draft Name' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'Draft Name' Field is not mandatory or no validation error") 
                                pass


                            #chapter
                            field_element = driver.find_element(By.XPATH, '//*[@id="customreport"]/div/form/div/div[3]')
                            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
                            is_mandatory = "*" in field_element.text

                            if has_validation_error or is_mandatory:
                                print("'Chapter' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error4    
                                print("'Chapter' Field is not mandatory or no validation error") 
                                pass

                        except:
                            pass


                        input_element = [".","alpha1","alpha@1",12345]
                        for j in input_element:
                            # driver.get(decision_reports_url)
                            try:
                                
                                driver.get(check_url)
                                time.sleep(1)
                                add_element = driver.find_element(By.NAME ,id_list[i])
                                add_element.click()
                                print("check1")
                                time.sleep(1)
                                
                                driver.find_element(By.NAME ,'draft').send_keys(j)
                                time.sleep(1)
                                driver.find_element(By.ID ,'select2-chapters-container').click()
                                time.sleep(0.2)
                                driver.find_element(By.XPATH ,'/html/body/span/span/span[1]/input').send_keys(j)
                                time.sleep(1)
                                check_status = driver.find_element(By.XPATH  ,'//*[@id="select2-chapters-results"]/li')
                                # Get the HTML of the element
                                dropdownitems = check_status.get_attribute('innerHTML')
                                if "No results found" in dropdownitems:
                                    print(j,"No results found")
                                else:
                                    dropdownitems.send_keys(Keys.RETURN)
                                
                                driver.find_element(By.ID , 'btnsb').click()
                                                        


                                check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[2]')
                                # Get the HTML of the element
                                html = check_status.get_attribute('innerHTML')
                                # print(html)
                                if "alert alert-danger text-center alert-dismiss " in html:
                                    print("already exists")
                                if "alert alert-success text-center alert-dismiss " in html:
                                    print("new record created")
                                #     message = element.text
                            #     print(message)
                            except Exception as e:
                                print("error",e)
                        

                        driver.get(check_url)
                        time.sleep(1)
                        add_element = driver.find_element(By.NAME ,id_list[i])
                        add_element.click()
                        time.sleep(1)
                        driver.find_element(By.NAME ,'draft').send_keys("new_custom_draft")
                        time.sleep(0.2)
                        driver.find_element(By.ID ,'select2-chapters-container').click()
                        time.sleep(0.2)
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        search.send_keys("others")
                        search.send_keys(Keys.RETURN)
                        
                        driver.find_element(By.NAME ,'add').click()
                        
                        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                        # Get the HTML of the element
                        html = check_status.get_attribute('outerHTML')
    #                     print(html,"this is html")
                        if "alert alert-danger text-center alert-dismiss " in html:
                            print("Decision already exists")
                        if "alert alert-success text-center alert-dismiss " in html:
                            print("new Decision created")
                            
                    elif flow[i] == "edit":
                        unique_id = random.randint(1000, 9999)
                        test = "test"+str(unique_id)
                        driver.find_element(By.XPATH , '//*[@id="custom_draft_filter"]/label/input').send_keys("new_custom_draft")
                        time.sleep(0.5)
                        driver.find_element(By.ID ,id_list[i]).click()
                        time.sleep(0.2)
                        decision_btn = driver.find_element(By.NAME ,'draft')
                        decision_btn.clear()
                        decision_btn.send_keys(test)
                        time.sleep(0.2)              
                        driver.find_element(By.ID , 'update').click()
                        
                        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                        # Get the HTML of the element
                        html = check_status.get_attribute('outerHTML')
    #                     print(html,"this is html")
                        if "alert alert-danger text-center alert-dismiss " in html:
                            print("Decision already exists")
                        if "alert alert-success text-center alert-dismiss " in html:
                            print("new Decision created")

                        
                    elif flow[i] == "delete":
                        driver.find_element(By.XPATH , '//*[@id="custom_draft_filter"]/label/input').send_keys(test)
    #                     search_btn.send_keys("new_checklist")
                        delete_btn = driver.find_element(By.NAME ,id_list[i])
                        delete_btn.click()
                        alert = driver.switch_to.alert
                        alert.accept()
                        time.sleep(2)


                else:
                    print("ERROR:nobutton and error")
                

                
            else:
                print("unchecked")
                flag = "unchecked"
                driver.get(check_url)
                
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