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



class Datehub_add_assignment:
    def datehub_add_assignment():
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
        driver.find_element(By.XPATH,'//*[@id="sticky_hub"]/button[2]/span').click()
        time.sleep(0.2)
        driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/div/div[2]/div[1]/div/div[1]/a/i').click()
        current_url = driver.current_url
        check_element = driver.find_element(By.ID,"pname")
        print_statements = []
        if check_element:
            # logging.info("Add assignemt page opened successfully")  # Log the message

            print("Add assignemt page opened successfully")
            print_statements.append("Add assignemt page opened successfully")
            pass
        else:
            # logging.info("not able to open Add_assignemnt page")  # Log the message
            print("not able to open Add_assignemnt page")
            print_statements.append("not able to open Add_assignemnt page")

        # Access check
        standardised_reports_url = driver.current_url
        # check_element = driver.find_element(By.ID,"pname")
        
        check_element_path = '//*[@id="pname"]'
        checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,standardised_reports_url,check_element_path)
        print(checkinassignment)
        time.sleep(1)
        driver.get(standardised_reports_url)


        try:
            driver.find_element(By.NAME,"submitBtn").click()
            
            field_element = driver.find_element(By.NAME,"pname")
            pname = field_element.get_attribute('outerHTML')
            if "required" in pname:
                print("'assignment name' Field is mandatory. Please fill it.")
                print_statements.append("'assignment name' Field is mandatory. Please fill it.")
            else:
                print("'assignment name' Field is not mandatory or no validation error") 
                print_statements.append("'assignment name' Field is not mandatory or no validation error")
                pass


            #Client
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[1]/div/div[2]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'Client' Field is mandatory. Please fill it.")
                print_statements.append("'Client' Field is mandatory. Please fill it.")

            else:
                print("' Client' Field is not mandatory")
                print_statements.append("'Client' Field is not mandatory")

            #     Field is not mandatory or no validation error
                pass


            #User
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[2]/div/div[1]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'User' Field is mandatory. Please fill it.")
                print_statements.append("'User' Field is mandatory. Please fill it.")
            else:
                print("' User' Field is not mandatory")
                print_statements.append("' User' Field is not mandatory")

            #     Field is not mandatory or no validation error
                pass

             #AM user
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[1]/div/div[3]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'AM user' Field is mandatory. Please fill it.")
                print_statements.append("'AM user' Field is mandatory. Please fill it.")
            else:
                print("'AM User' Field is not mandatory")
                print_statements.append("'AM User' Field is not mandatory")

            #     Field is not mandatory or no validation error
                pass

            #Review partner
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[1]/div/div[4]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'Review partner' Field is mandatory. Please fill it.")
                print_statements.append("'Review partner' Field is mandatory. Please fill it.")
            else:
                print("'Review partner' Field is not mandatory")
                print_statements.append("'Review partner' Field is not mandatory")
                

            #     Field is not mandatory or no validation error
                pass


            #External User
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[2]/div/div[2]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'External User' Field is mandatory. Please fill it.")
                print_statements.append("'External User' Field is mandatory. Please fill it.")
            else:
                print("'External User' Field is not mandatory")
                print_statements.append("'External User' Field is not mandatory")
            #     Field is not mandatory or no validation error
                pass


            #Period
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[4]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'Period' Field is mandatory. Please fill it.")
                print_statements.append("'Period' Field is mandatory. Please fill it.")
            else:
                print("'Period' Field is not mandatory")
                print_statements.append("'Period' Field is not mandatory")
            #     Field is not mandatory or no validation error
                pass


            #Previous Assignment
            field_element = driver.find_element(By.XPATH, '//*[@id="prevdiv"]')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'Previous Assignment' Field is mandatory. Please fill it.")
                print_statements.append("'Previous Assignment' Field is mandatory. Please fill it.")
            else:
                print("'Previous Assignment' Field is not mandatory")
                print_statements.append("'Previous Assignment' Field is not mandatory")

            #     Field is not mandatory or no validation error
                pass


            #start date
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[6]/div[1]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'start date' Field is mandatory. Please fill it.")
                print_statements.append("'start date' Field is mandatory. Please fill it.")
            else:
                print("'start date' Field is not mandatory")
                print_statements.append("'start date' Field is not mandatory")

            #     Field is not mandatory or no validation error
                pass


            #End date
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[6]/div[2]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'End date' Field is mandatory. Please fill it.")
                print_statements.append("'End date' Field is mandatory. Please fill it.")
            else:
                print("'End date' Field is not mandatory")
                print_statements.append("'End date' Field is not mandatory")

            #     Field is not mandatory or no validation error
                pass

            #Description
            field_element = driver.find_element(By.XPATH, '//*[@id="systemrightsForm"]/div/div[7]/div')
            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
            is_mandatory = "*" in field_element.text

            if has_validation_error or is_mandatory:
                print("'Description' Field is mandatory. Please fill it.")
                print_statements.append("'Description' Field is mandatory. Please fill it.")
            else:
                print("'Description' Field is not mandatory")
                print_statements.append("'Description' Field is not mandatory")

            #     Field is not mandatory or no validation error
                pass





            
        except:
            pass

        driver.get(standardised_reports_url)
        time.sleep(1)
        driver.find_element(By.ID,"pname").send_keys("testassignment454212")
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
        driver.find_element(By.ID,'est_start_date').send_keys("09-06-2023")
        time.sleep(0.8)
        driver.find_element(By.ID,'est_end_date').send_keys("09-06-2023")

        driver.find_element(By.NAME,'submitBtn').click()
        
        time.sleep(1)
        
        
        check_status = driver.find_element(By.XPATH  ,'//*[@id="exampleModalLabel"]')
        # Get the HTML of the element
        html = check_status.get_attribute('outerHTML')
        print(html,"this is html")
        try:
            if "Confirmation" in html:
                variable = "new_assignment is created"
                print("new_assignment is created")
                print_statements.append("new_assignment is created")
            else:
                raise Exception
        except Exception as e:
            if "Assignment Name Already Exist!" in html:
                variable = "Assignment Name Already Exist!"
                print(variable,e)
                print_statements.append(variable,e)
                pass      

            df = pd.DataFrame({"Print Statements": print_statements})

    # Save the DataFrame to an Excel file
        unique_id = random.randint(1000, 9999)
        excelsave = "Datahub_add_assignment"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)
        time.sleep(10)
        return variable




