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
import sys
from login import loginclass
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait



class fifwclass:
    def fifw():
        user = "tharun"
        password = "tharun123"
        url = "https://old.anyaudit.co.in/login"
        driver,static_value = loginclass.loginfunction(user,password,url)
        print(static_value)
        # clicking on message otp
        driver.find_element(By.XPATH , '//*[@id="sign_in"]/div[3]/div/button').click()
        #going to the base url
        fifw = "Test on march 8"
        driver.get("https://old.anyaudit.co.in/Reclassificationreports/Fss")
        time.sleep(0.2)
        driver.find_element(By.ID,"iff").click()
        time.sleep(0.2)
        search_input = driver.find_element(By.XPATH,'//*[@id="fss_head_inact_filter"]/label')

        
        search_input.click()
        driver.find_element(By.XPATH,'//*[@id="fss_head_inact_filter"]/label/input').send_keys(fifw)
        # driver.find_element(By.XPATH,'fss_head_filter').send_keys(fifw)
        # time.sleep(100)
        driver.find_element(By.ID,'mark_active').click()
        alert = driver.switch_to.alert
        alert.accept()
        driver.find_element(By.ID,'aff').click()
        time.sleep(1)
        search_input = driver.find_element(By.XPATH,'//*[@id="fss_head_filter"]/label')

        
        search_input.click()
        driver.find_element(By.XPATH,'//*[@id="fss_head_filter"]/label/input').send_keys(fifw)
        time.sleep(0.5)
        check_status = driver.find_element(By.XPATH,'//*[@id="fss_head"]/tbody/tr/td[2]')
        html = check_status.get_attribute('outerHTML')
        print(html)
        try:
            if  fifw in html:
                variable = "FIFW activated"
                # print("new_assignment is created")
            else:
                raise Exception
        except Exception as e:
                variable = "FIFW not activated"
                print(variable,e)
                pass      

        return variable