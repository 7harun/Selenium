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
import sys


class loginclass:
    def loginfunction(user,password,url):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        driver.maximize_window()
        username_box = driver.find_element(By.NAME , "username")
        username_box.send_keys(user)
        password_box = driver.find_element(By.NAME, "password")
        password_box.send_keys(password)
        driver.find_element(By.XPATH  , '//*[@id="sign_in"]/div[3]/div/button').click()
        time.sleep(1)
        html = driver.page_source
        # print(html)
        tree = etree.HTML(html)

        element = tree.xpath('//*[@id="userlogin"]/div[1]')
        if element:                
            static_value = element[0].text.strip()
    #         print("Static Display Value:", static_value)
            if static_value =="Invalid Username or Password!":
                driver.close()
                print(static_value)
        else:
                static_value = "Logged in successfully"
        
        return driver,static_value