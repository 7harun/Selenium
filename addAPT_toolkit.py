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


class APT_toolkit:
    def apt_toolkit():
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
        driver.find_element(By.ID,"Planning_Template").click()
        time.sleep(1)
        standardised_reports_url = driver.current_url
        # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standardised_reports_url,check_element_path)
        # print(checkinassignment)
        driver.get("https://old.anyaudit.co.in/Management/users")
        search = driver.find_element(By.ID  ,"txtSearch")
        driver.find_element(By.ID  ,"txtSearch").send_keys("tharun")
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        
        # driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[9]/td[2]/input']
        id_list = ['add_cinfigure_temp','add_cinfigure_temp']
        flow = ["add","delete"]
        for i in range(0,len(id_list)):
        
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
                    add_element = driver.find_element(By.ID ,id_list[i])
    #                 print("button exists and no error")
                except:
                    add_element = ""
                    pass
                if add_element:
                    print("button exists and no error")
                    if flow[i] == "add":
                        add_element.click()
                    
                        time.sleep(1)
                        driver.get(standardised_reports_url)
                        time.sleep(1)
                        add_element = driver.find_element(By.ID ,id_list[i])
                        add_element.click()
                        time.sleep(1)

                        driver.find_element(By.ID ,'template_name').send_keys("template_test")
                        driver.find_element(By.ID,"template").send_keys("template_description")
                        time.sleep(2)
                        driver.find_element(By.ID , 'btnsb').click()
                        
                        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                        # Get the HTML of the element
                        html = check_status.get_attribute('outerHTML')
    #                     print(html,"this is html")
                        if "alert alert-danger text-center alert-dismiss " in html:
                            print("APT already exists")
                        if "alert alert-success text-center alert-dismiss " in html:
                            print("new APT created")
                        time.sleep(1)
                        driver.find_element(By.XPATH , '//*[@id="configuration_act_filter"]/label/input').send_keys("template_test")
                        driver.find_element(By.NAME ,'configure').click()
                        time.sleep(1)


                        
                        driver.find_element(By.NAME ,'add_toolkit').click()
                        time.sleep(0.5)
                        driver.find_element(By.NAME ,'addToolBtn').click()
                        time.sleep(0.2)


                        driver.find_element(By.ID ,'save_btn').click()
                        time.sleep(0.5)
                        try:
                            # Find the field element that contains the mandatory star mark
                            #TOOL
                            field_element = driver.find_element(By.ID ,'tool_1')
                            TOOL = field_element.get_attribute('outerHTML')
                            if "required" in TOOL:
                                print("'TOOL' Field is mandatory. Please fill it.")
                            else:
                                print("'TOOL' Field is not mandatory or no validation error") 
                                pass

                            #  TOOL_kit
                            field_element = driver.find_element(By.ID ,'toolkit_1')
                            TOOL_kit = field_element.get_attribute('outerHTML')
                            if "required" in TOOL_kit:
                                print("'TOOL_kit' Field is mandatory. Please fill it.")
                            else:
                                print("'TOOL_kit' Field is not mandatory or no validation error") 
                                pass

                        except:
                            pass
                        driver.refresh()
                        driver.find_element(By.NAME ,'add_toolkit').click()
                        time.sleep(0.5)
                        driver.find_element(By.NAME ,'addToolBtn').click()
                        time.sleep(0.2)
                        driver.find_element(By.ID,"select2-tool_1-container").click()
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")

                        search.send_keys("Annexures")
                        search.send_keys(Keys.ENTER)

                        time.sleep(3)

                        driver.find_element(By.XPATH,'//*[@id="toolTable"]/tbody/tr/td[2]/span/span[1]/span/ul').click()
                        time.sleep(2)

                        search = driver.find_element(By.XPATH,'//*[@id="toolTable"]/tbody/tr/td[2]/span/span[1]/span')
                        time.sleep(2)
                        driver.find_element(By.XPATH,'//*[@id="toolTable"]/tbody/tr/td[2]/span/span[1]/span/ul/li/input').send_keys("test")
                        search.send_keys(Keys.ENTER)

                        driver.find_element(By.NAME,"save_btn").click()
                    if flow[i] == "delete":
                        time.sleep(1)
                        driver.find_element(By.XPATH , '//*[@id="configuration_act_filter"]/label/input').send_keys("template_test")
                        driver.find_element(By.NAME ,'configure').click()
                        time.sleep(1)
                    
                        delete_button_xpath = "//tr[td[text()='Annexures']]//a[@class='btn btn-danger btn-sm deleteconfgtmpgrp']"
                        delete_button = driver.find_element(By.XPATH, delete_button_xpath)
                        delete_button.click()
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