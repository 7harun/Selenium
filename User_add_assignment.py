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



class User_add_assignment:
    def user_add_assignment():
        # logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        user = "tharun"
        password = "tharun123"
        url = "https://old.anyaudit.co.in/login"
        driver,static_value = loginclass.loginfunction(user,password,url)
        print(static_value)
        # clicking on message otp
        driver.find_element(By.XPATH , '//*[@id="sign_in"]/div[3]/div/button').click()
        driver.find_element(By.XPATH,'//*[@id="tree2"]/li[2]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'//*[@id="tree2"]/li[2]/ul/li[5]/a').click()
        time.sleep(0.5)
        user_field = driver.find_element(By.ID,"select2-usershubselectajax-container")
        user_field.click()
        # time.sleep(10)
        user_input = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
        user_input.send_keys("tharun")
        time.sleep(2)
        user_input.send_keys(Keys.RETURN)
        # user_field.send_keys("tharun")
        # time.sleep(10)
        driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/div[1]/button[2]').click()
        time.sleep(1)
        assignment_button = driver.find_element(By.XPATH,' /html/body/section/div/div/div/div/div/div[2]/div[1]/div/div/div/a/i')
        assignment_button.click()
        time.sleep(1)
        current_url = driver.current_url
        check_element = driver.find_element(By.ID,"pname")
        if check_element:
            # logging.info("Add assignemt page opened successfully")  # Log the message

            print("Add assignemt page opened successfully")
            pass
        else:
            # logging.info("not able to open Add_assignemnt page")  # Log the message
            print("not able to open Add_assignemnt page")

        # Access check
        driver.get("https://old.anyaudit.co.in/Navigation")
        driver.find_element(By.XPATH , '//*[@id="select2-selassignmentchange_dashboard-container"]').click()  
        new = driver.find_element(By.XPATH , '/html/body/span/span/span[1]/input')
        new.send_keys(3003)
        time.sleep(2)
        driver.find_element(By.XPATH , '/html/body/span/span/span[2]').click()
        time.sleep(2)
        driver.get(current_url)
        check_element = driver.find_element(By.ID,"pname")
        if check_element:          
            print("Add assignemt page opened successfully inside assignment")
            pass
        else:
            print("not able to open Add_assignemnt page inside assignment")
        time.sleep(0.8)
        driver.find_element(By.XPATH ,'/html/body/nav/div/div[2]/div[1]/div[1]/a/img').click()
        time.sleep(2)
        driver.get(current_url)
        driver.find_element(By.ID,"pname").send_keys("testassignment45421")
        driver.find_element(By.ID,"select2-pro_company_id_x-container").click()
        select_box = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        select_box.send_keys("Anyaudit")
        # Wait for the dropdown options to appear
        options_locator = (By.CSS_SELECTOR, "ul.select2-results__options li")
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(options_locator))

        # Find the desired option with exact text match
        options = driver.find_elements(*options_locator)
        for option in options:
            if option.text == "Anyaudit":
                option.click()
                break
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/div/form/div/div[2]/div/div[1]/div/span/span[1]/span/ul').click()
        dropdown_button = driver.find_element(By.XPATH,'//*[@id="systemrightsForm"]/div/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input')
        dropdown_button.send_keys("tharun")
        time.sleep(2)
        dropdown_button.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH,'//*[@id="select2-amuser_Deleted-container"]').click()
        ep = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        ep.send_keys("tharun")
        ep.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH,'//*[@id="select2-rvuser_Deleted-container"]').click()
        rp = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        rp.send_keys("tharun")
        rp.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/div/form/div/div[2]/div/div[2]/div/span/span[1]/span/ul').click()
        dropdown_button2 = driver.find_element(By.XPATH,'//*[@id="systemrightsForm"]/div/div[2]/div/div[2]/div/span/span[1]/span/ul/li/input')
        dropdown_button2.send_keys("krishna@ext")
        time.sleep(2)
        dropdown_button2.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH,'//*[@id="select2-period-container"]').click()
        period = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        period.send_keys("2023-24")
        period.send_keys(Keys.RETURN)

        time.sleep(2)
        driver.find_element(By.ID,'est_start_date').send_keys("23-04-2023")
        time.sleep(0.8)
        driver.find_element(By.ID,'est_end_date').send_keys("24-04-2023")

        driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/div/form/div/div[8]/button').click()
        
        time.sleep(1)
        
        
        check_status = driver.find_element(By.XPATH  ,'//*[@id="exampleModalLabel"]')
        # Get the HTML of the element
        html = check_status.get_attribute('outerHTML')
        print(html,"this is html")
        try:
            if "Confirmation" in html:
                variable = "new_assignment is created"
                print("new_assignment is created")
            else:
                raise Exception
        except Exception as e:
            if "Assignment Name Already Exist!" in html:
                variable = "Assignment Name Already Exist!"
                print(variable,e)
                pass      
        time.sleep(100)
        return variable




