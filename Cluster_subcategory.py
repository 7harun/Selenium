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


class Cluster_sub:
    def cluster_sub():
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
        driver.find_element(By.ID,"Assignment_cluster").click()
        time.sleep(1)
        standardised_reports_url = driver.current_url
        driver.get("https://old.anyaudit.co.in/Management/users")
        search = driver.find_element(By.ID  ,"txtSearch")
        search.send_keys("tharun")
        search.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[6]/td[2]/input']
        id_list = ['add_category']
        flow = ["add"]
    
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
                add_element = driver.find_element(By.ID ,id_list[0])
                print("button exists and no error")
                add_element.click()
            except:
                add_element = ""
                pass
                

