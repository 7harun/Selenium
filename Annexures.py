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


class Annexures:
    def annexures():
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
        driver.find_element(By.ID,"Annexures").click()
        time.sleep(1)
        annexures_reports_url = driver.current_url
        check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,annexures_reports_url,check_element_path)
        print(checkinassignment)
        driver.get("https://old.anyaudit.co.in/Management/users")
        search = driver.find_element(By.ID  ,"txtSearch")
        search.send_keys("tharun")
        search.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[1]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[33]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[17]/td[2]/input']
        id_list = ['add_annexure','edit','mark_inactive']
        flow = ["add","edit","delete"]
        print_statements = []
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
                driver.get(annexures_reports_url)
                try:
                    add_element = driver.find_element(By.ID ,id_list[i])
    #                 print("button exists and no error")
                except:
                    add_element = ""
                    pass
                if add_element:
                    print("button exists and no error")
                    print_statements.append("button exists and no error")
                    if flow[i] == "add":
                        add_element.click()
                        time.sleep(0.2)

                        driver.find_element(By.ID , 'btnsb').click()
                        try:
                            # Find the field element that contains the mandatory star mark
                            #name
                            field_element = driver.find_element(By.XPATH, '//*[@id="annex"]/div/div/div[1]/div')
                            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
                            is_mandatory = "*" in field_element.text

                            if has_validation_error or is_mandatory:
                                print("'Name' Field is mandatory. Please fill it.")
                                print_statements.append("'Name' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'Name' Field is not mandatory or no validation error") 
                                print_statements.append("'Name' Field is not mandatory or no validation error")
                                pass


                            #chapter
                            field_element = driver.find_element(By.XPATH, '//*[@id="annex"]/div/div/div[2]/div')
                            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
                            is_mandatory = "*" in field_element.text

                            if has_validation_error or is_mandatory:
                                print("'Chapter' Field is mandatory. Please fill it.")
                                print_statements.append("'Chapter' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error4    
                                print("'Chapter' Field is not mandatory or no validation error") 
                                print_statements.append("'Chapter' Field is not mandatory or no validation error")
                                pass
                            



                            #area of audit
                            field_element = driver.find_element(By.XPATH, '//*[@id="annex"]/div/div/div[3]/div')

                            #field_name = field_element.get_attribute("Area of audit")
                            # Checking if the field has any validation error or highlighting indicating it is mandatory
                            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
                            is_mandatory = "*" in field_element.text

                            if has_validation_error or is_mandatory:
                                print("'Area of audit' Field is mandatory. Please fill it.")
                                print_statements.append("'Area of audit' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'Area of audit' Field is not mandatory or no validation error") 
                                print_statements.append("'Area of audit' Field is not mandatory or no validation error")
                                pass


                            #description
                            field_element = driver.find_element(By.XPATH, '//*[@id="annex"]/div/div/div[4]/div')
                            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
                            is_mandatory = "*" in field_element.text

                            if has_validation_error or is_mandatory:
                                print("'Description' Field is mandatory. Please fill it.")
                                print_statements.append("'Description' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'Description' Field is not mandatory or no validation error")
                                print_statements.append("'Description' Field is not mandatory or no validation error") 

                                pass

                        except:
                            pass

                        unique_id = random.randint(1000, 9999)
                        annexure = "annexure_"+str(unique_id)
                        driver.find_element(By.NAME ,'annexure_name').send_keys(annexure)
                        time.sleep(0.2)
                        driver.find_element(By.ID,"select2-chapters-container").click()
                        time.sleep(1)
                        try:
                            alert = driver.switch_to.alert
                            alert.accept()
                            time.sleep(2)
                            print("annexure already exists")
                            print_statements.append("annexure already exists")
                            continue
                        except Exception as e:
                            print(e)
                            print("entered into exception")
                            print_statements.append("entered into exception")
                            pass
                        
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        search.send_keys("others")
                        search.send_keys(Keys.RETURN)
                        driver.find_element(By.ID,"select2-area_audit_id-container").click()
                        time.sleep(1)
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        search.send_keys("Audit of Account Receivable & Payable")
                        search.send_keys(Keys.RETURN)

                        driver.find_element(By.NAME ,'annexure_description').send_keys("New_description")                 
                        driver.find_element(By.ID , 'btnsb').click()
                        
                        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                        # Get the HTML of the element
                        html = check_status.get_attribute('outerHTML')
    #                     print(html,"this is html")
                        if "alert alert-danger text-center alert-dismiss " in html:
                            print("Decision already exists")
                            print_statements.append("Decision already exists")
                        if "alert alert-success text-center alert-dismiss " in html:
                            print("new Decision created")
                            print_statements.append("new Decision created")
                            
                    elif flow[i] == "edit":
                        annexure_upd = annexure+"_update"
                        driver.find_element(By.XPATH , '//*[@id="annextureact_filter"]/label/input').send_keys(annexure)
                        driver.find_element(By.NAME ,'edit').click()
                        
                        time.sleep(0.2)
                        decision_btn = driver.find_element(By.NAME ,'annexure_name')
                        decision_btn.clear()
                        decision_btn.send_keys(annexure_upd)
                        time.sleep(1)              
                        driver.find_element(By.NAME , 'btnsb').click()
                        
                        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                        # Get the HTML of the element
                        html = check_status.get_attribute('outerHTML')
    #                     print(html,"this is html")
                        if "alert alert-danger text-center alert-dismiss " in html:
                            print("Decision already exists")
                            print_statements.append("Decision already exists")
                        if "alert alert-success text-center alert-dismiss " in html:
                            print("new Decision created")
                            print_statements.append("new Decision created")

                        
                    elif flow[i] == "delete":
                        driver.find_element(By.XPATH , '//*[@id="annextureact_filter"]/label/input').send_keys(annexure_upd)
    #                     search_btn.send_keys("new_checklist")
                        delete_btn = driver.find_element(By.NAME ,'mark_inactive')
                        delete_btn.click()
                        alert = driver.switch_to.alert
                        alert.accept()
                        time.sleep(2)


                else:
                    print("ERROR:nobutton and error")
                    print_statements.append("ERROR:nobutton and error")
                

                
            else:
                print("unchecked")
                flag = "unchecked"
                driver.get(annexures_reports_url)
                
                try:
                    add_element = driver.find_element(By.ID ,id_list[i])
    #                 if not add_element:
    #                 print("button not  exists and no error")
                except:
                    add_element = ""
                    pass
                print(add_element,"this is add_elelmtn")
                print_statements.append("this is add_elelmtn")
                if add_element:
                    print("ERROR:button exists and error")
                    print_statements.append("ERROR:button exists and error")
                else:
                    print("nobutton and no error")
                    print_statements.append("nobutton and no error")

                    df = pd.DataFrame({"Print Statements": print_statements})

    # Save the DataFrame to an Excel file
        unique_id = random.randint(1000, 9999)
        excelsave = "Annexures"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)

        return True