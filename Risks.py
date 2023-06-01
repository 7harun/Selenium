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


class Risks:
    def risks():
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
        time.sleep(0.5)
        driver.find_element(By.ID,"Risks").click()
        time.sleep(1)
        standardised_reports_url = driver.current_url
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

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[15]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[47]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[31]/td[2]/input']
        id_list = ['add_risk','edit','mark_inactive']
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
                        time.sleep(0.2)
                        driver.find_element(By.NAME ,'impact_name').send_keys("new_impact")
                        time.sleep(0.2)
                        driver.find_element(By.ID,"select2-impact_type-container").click()
                        time.sleep(2)
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        search.send_keys("single")
                        search.send_keys(Keys.RETURN)

                        driver.find_element(By.ID , 'btnsb').click()
                        
    #                     check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
    #                     # Get the HTML of the element
    #                     html = check_status.get_attribute('outerHTML')
    # #                     print(html,"this is html")
    #                     if "alert alert-danger text-center alert-dismiss " in html:
    #                         print("APT already exists")
    #                     if "alert alert-success text-center alert-dismiss " in html:
    #                         print("new APT created")
                            
                    elif flow[i] == "edit":
                        driver.find_element(By.XPATH , '//*[@id="active_audit_filter"]/label/input').send_keys("new_impact")
                        driver.find_element(By.ID ,'edit').click()
                        time.sleep(1)
                        update_btn = driver.find_element(By.ID ,'impact_name')
                        update_btn.clear()
                        update_btn.send_keys("new_impact22")
                        time.sleep(1)
                        driver.find_element(By.ID,"select2-impact_type-container").click()
                        time.sleep(2)
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        search.send_keys("single")
                        search.send_keys(Keys.RETURN)

                        driver.find_element(By.ID , 'btnsb').click()

                        
                    elif flow[i] == "delete":
                        driver.find_element(By.XPATH , '//*[@id="active_audit_filter"]/label/input').send_keys("new_impact22")
    #                     search_btn.send_keys("new_checklist")
                        delete_btn = driver.find_element(By.ID ,'mark_inactive')
                        delete_btn.click()
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