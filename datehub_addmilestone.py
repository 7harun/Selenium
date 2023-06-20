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
import random
from login import loginclass
from selenium.webdriver.support import expected_conditions as EC
from CheckurlinAssignment import CheckUrlinAssignment
from selenium.webdriver.support.ui import WebDriverWait



class Datehub_add_MS:
    def datehub_add_MS():
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
        driver.find_element(By.XPATH,'//*[@id="tree2"]/li[2]/ul/li[6]/a').click()
        time.sleep(0.5)
        date_field = driver.find_element(By.ID,"seldate_datehub")
        date_field.send_keys("09062023")
        time.sleep(0.5)
        driver.find_element(By.NAME,'m_milestone').click()
        time.sleep(0.2)
        driver.find_element(By.NAME,'am_addmilestone').click()
        time.sleep(1)
        standardised_reports_url = driver.current_url
        check_element = driver.find_element(By.NAME,"assignmentid")
        print_statements = []
        if check_element:
            # logging.info("Add assignemt page opened successfully")  # Log the message

            print("Add Milestone page opened successfully")
            print_statements.append("Add Milestone page opened successfully")
            pass
        else:
            # logging.info("not able to open Add_assignemnt page")  # Log the message
            print("not able to open add Milestone page")
            print_statements.append("not able to open add Milestone page")

       

        # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standardised_reports_url,check_element_path)
        # print(checkinassignment)
        driver.get(standardised_reports_url)
        try:
            driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/form/div[2]/div/button').click()
            field_element = driver.find_element(By.NAME,"assignmentid")
            assignmentid = field_element.get_attribute('outerHTML')
            if "required" in assignmentid:
                print("'assignmentid' Field is mandatory. Please fill it.")
                print_statements.append("'assignmentid' Field is mandatory. Please fill it.")
            else:
                print("'assignmentid' Field is not mandatory or no validation error")
                print_statements.append("'assignmentid' Field is not mandatory or no validation error") 
                pass

            field_element = driver.find_element(By.NAME,"activity_name")
            activity_name = field_element.get_attribute('outerHTML')
            if "required" in activity_name:
                print("'activity_name' Field is mandatory. Please fill it.")
                print_statements.append("'activity_name' Field is mandatory. Please fill it.")
            else:
                print("'activity_name' Field is not mandatory or no validation error") 
                print_statements.append("'activity_name' Field is not mandatory or no validation error")
                pass

            field_element = driver.find_element(By.NAME,"dur_hrs")
            dur_hrs = field_element.get_attribute('outerHTML')
            if "required" in dur_hrs:
                print("'dur_hrs' Field is mandatory. Please fill it.")
                print_statements.append("'dur_hrs' Field is mandatory. Please fill it.")
            else:
                print("'dur_hrs' Field is not mandatory or no validation error")
                print_statements.append("'dur_hrs' Field is not mandatory or no validation error")
                pass

            field_element = driver.find_element(By.NAME,"avalue")
            avalue = field_element.get_attribute('outerHTML')
            if "required" in avalue:
                print("'avalue' Field is mandatory. Please fill it.")
                print_statements.append("'avalue' Field is mandatory. Please fill it.")
            else:
                print("'avalue' Field is not mandatory or no validation error") 
                print_statements.append("'avalue' Field is not mandatory or no validation error")
                pass

            field_element = driver.find_element(By.NAME,"chapter_id")
            chapter_id = field_element.get_attribute('outerHTML')
            if "required" in chapter_id:
                print("'chapter_id' Field is mandatory. Please fill it.")
                print_statements.append("'chapter_id' Field is mandatory. Please fill it.")
            else:
                print("'chapter_id' Field is not mandatory or no validation error") 
                print_statements.append("'chapter_id' Field is not mandatory or no validation error")
                pass

            field_element = driver.find_element(By.NAME,"est_start_date")
            est_start_date = field_element.get_attribute('outerHTML')
            if "required" in est_start_date:
                print("'est_start_date' Field is mandatory. Please fill it.")
                print_statements.append("'est_start_date' Field is mandatory. Please fill it.")

            else:
                print("'est_start_date' Field is not mandatory or no validation error") 
                print_statements.append("'est_start_date' Field is not mandatory or no validation error")
                pass

            field_element = driver.find_element(By.NAME,"est_end_date")
            est_end_date = field_element.get_attribute('outerHTML')
            if "required" in est_end_date:
                print("'est_end_date' Field is mandatory. Please fill it.")
                print_statements.append("'est_end_date' Field is mandatory. Please fill it.")
            else:
                print("'est_end_date' Field is not mandatory or no validation error") 
                print_statements.append("'est_end_date' Field is not mandatory or no validation error")
                pass     
        except:
            pass
        

        driver.refresh()
        planuserclient = driver.find_element(By.ID,"select2-assignmentid-container")
        planuserclient.click()
        search = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        search.send_keys("4069")
        search.send_keys(Keys.RETURN)
        time.sleep(5)

        # planuserwork = driver.find_element(By.XPATH,'//*[@id="mainForm1"]/div/div/div[2]/div[2]/span[2]/span[1]/span')
        # planuserwork.click()
        search = driver.find_element(By.NAME,'activity_name')
        search.send_keys("New_milestone")
        # search.send_keys(Keys.RETURN)
        time.sleep(1)

        # tasklist = driver.find_element(By.ID,"select2-tasklist-container")
        # tasklist.click()
        search = driver.find_element(By.NAME,'dur_hrs')
        search.send_keys(8)
        # search.send_keys(Keys.RETURN)
        time.sleep(1)

        tasklist = driver.find_element(By.XPATH,'//*[@id="mainForm1"]/div[1]/div[2]/div[1]/div/div/span/span[1]/span')
        tasklist.click()
        search = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        search.send_keys("configuration")
        search.send_keys(Keys.RETURN)
        time.sleep(1)   

        
        est_start_date = driver.find_element(By.ID,'est_start_date')
        est_start_date.click()
        # est_start_date.send_keys("09-06-2023")
        time.sleep(1)

        est_end_date = driver.find_element(By.ID,'est_end_date')
        est_end_date.click()
        # est_end_date.send_keys("09-06-2023")
        time.sleep(1)


        


        driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/form/div[2]/div/button').click()
        time.sleep(2)
        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
        # Get the HTML of the element
        html = check_status.get_attribute('outerHTML')
        if "alert alert-danger text-center alert-dismiss " in html:
            print("Milestone is not added")
            print_statements.append("Milestone is not added")
            variable = "Milestone is not added"
        if "alert alert-success text-center alert-dismiss " in html:
            print("Milestone added successfully")
            print_statements.append("Milestone added successfully")
            variable = "Milestone added successfully"    

            df = pd.DataFrame({"Print Statements": print_statements})

    # Save the DataFrame to an Excel file
        unique_id = random.randint(1000, 9999)
        excelsave = "Datahub_add_milestone"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)

        return variable




