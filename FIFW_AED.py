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


class FIFW_AED:
    def fifw_aed():
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
        time.sleep(3)
        

        driver.find_element(By.NAME,"Financial").click()
        time.sleep(1)
        standard_text_url = driver.current_url
        check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standard_text_url,check_element_path)
        print(checkinassignment)
        try:
            driver.get("https://old.anyaudit.co.in/SignOffReports/permissionreports")
            time.sleep(0.8)
            driver.find_element(By.XPATH ,'/html/body/nav/div/div[2]/div[1]/div[1]/a/img').click()
            time.sleep(2)
        except:
            pass
        driver.get(standard_text_url)
        id_list = ['add_ff','edit','mark_inactive']
        flow = ["add","edit","delete"]
        for i in range(0,len(id_list)):
            time.sleep(2)
            driver.get(standard_text_url)
    #         driver.refresh()
            time.sleep(0.5)
    
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
                    driver.find_element(By.NAME , 'submit').click()
                    try:
                        # Find the field element that contains the mandatory star mark
                        #fss_head_name
                        field_element = driver.find_element(By.NAME ,'fss_head_name')
                        html = field_element.get_attribute('outerHTML')
            #                     print(html,"this is html")
                        if "required" in html:
                            print("'fss_head_name' Field is mandatory. Please fill it.")
                        else:
                        #     Field is not mandatory or no validation error
                            print("'fss_head_name' Field is not mandatory or no validation error") 
                            pass
                        #Description
                        field_element = driver.find_element(By.NAME, 'description')
                        html = field_element.get_attribute('outerHTML')
            #                     print(html,"this is html")
                        if "required" in html:
                            print("'Description' Field is mandatory. Please fill it.")
                        else:
                        #     Field is not mandatory or no validation error4    
                            print("'Description' Field is not mandatory or no validation error") 
                            pass

                    except:
                        pass



                    input_element = [".","alpha1","alpha@1",12345]
                    for j in input_element:
                        # driver.get(decision_reports_url)
                        try:
                            
                            driver.get(standard_text_url)
                            time.sleep(1)
                            add_element = driver.find_element(By.NAME ,id_list[i])
                            add_element.click()
                            print("check1")
                            time.sleep(1)
                            
                            driver.find_element(By.NAME ,'fss_head_name').send_keys(j)
                            time.sleep(1)
                            driver.find_element(By.NAME,"description").send_keys(j)
                            time.sleep(1)
                                            
                            driver.find_element(By.NAME , 'submit').click()
                                                    

                            try:
                                    
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
                            except:
                                print("no alert")
                                pass
                        except Exception as e:
                            print("error",e)
                    

                    driver.get(standard_text_url)
                    time.sleep(1)
                    add_element = driver.find_element(By.NAME ,id_list[i])
                    add_element.click()
                    time.sleep(1)
                    driver.find_element(By.NAME ,'fss_head_name').send_keys("new_ff")
                    time.sleep(0.2)
                    driver.find_element(By.NAME ,'description').send_keys("new_ff_description")
                    time.sleep(0.2)
                    
                    
                    driver.find_element(By.ID , 'submit').click()
                    try:

                        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                        # Get the HTML of the element
                        html = check_status.get_attribute('outerHTML')
            #                     print(html,"this is html")
                        if "alert alert-danger text-center alert-dismiss " in html:
                            print("Decision already exists")
                        if "alert alert-success text-center alert-dismiss " in html:
                            print("new Decision created")
                    except:
                        print("no alert")
                        pass
                        
                elif flow[i] == "edit":
                    unique_id = random.randint(1000, 9999)
                    test = "test"+str(unique_id)
                    driver.find_element(By.XPATH , '//*[@id="fss_head_filter"]/label/input').send_keys("new_ff")
                    driver.find_element(By.ID ,id_list[i]).click()
                    
                    time.sleep(0.2)
                    decision_btn = driver.find_element(By.NAME ,'fss_head_name')
                    decision_btn.clear()
                    decision_btn.send_keys(test)
                    time.sleep(0.2)              
                    driver.find_element(By.NAME , 'submit').click()
                    time.sleep(5)
                    
                    check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                    # Get the HTML of the element
                    html = check_status.get_attribute('outerHTML')
        #                     print(html,"this is html")
                    if "alert alert-danger text-center alert-dismiss " in html:
                        print("Decision already exists")
                    if "alert alert-success text-center alert-dismiss " in html:
                        print("new Decision created")

                    
                elif flow[i] == "delete":
                    driver.find_element(By.XPATH , '//*[@id="fss_head_filter"]/label/input').send_keys(test)
        #                     search_btn.send_keys("new_checklist")
                    delete_btn = driver.find_element(By.NAME , "mark_inactive")
                    delete_btn.click()
                    alert = driver.switch_to.alert
                    alert.accept()
                    time.sleep(2)

            else:
                print("ERROR:nobutton and error")
       
                

                
            
        return True