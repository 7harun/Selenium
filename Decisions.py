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


class Decisions:
    def decisions():
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
        driver.find_element(By.ID,"Decisions").click()
        time.sleep(1)
        decision_reports_url = driver.current_url
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

        xpath_list_perm_page = ['//*[@id="38"]/div/div/table/tbody/tr[1]/td[2]/input','//*[@id="38"]/div/div/table/tbody/tr[3]/td[2]/input','//*[@id="38"]/div/div/table/tbody/tr[2]/td[2]/input']
        id_list = ['add_decisions','edit','mark_inacticve']
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
                driver.get(decision_reports_url)
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
                            # ConditionName
                            field_element = driver.find_element(By.NAME ,'dec_name')
                            cname = field_element.get_attribute('outerHTML')
                            if "required" in cname:
                                print("'ConditionName' Field is mandatory. Please fill it.")
                                print_statements.append("'ConditionName' Field is mandatory. Please fill it.")
                            else:
                                print("'ConditionName' Field is not mandatory or no validation error")
                                print_statements.append("'ConditionName' Field is not mandatory or no validation error") 
                                pass

                            #Type
                            field_element = driver.find_element(By.ID ,'select2-dec_type-container')
                            cname = field_element.get_attribute('outerHTML')
                            if "required" in cname:
                                print("'Type' Field is mandatory. Please fill it.")
                                print_statements.append("'Type' Field is mandatory. Please fill it.")
                            else:
                                print("'Type' Field is not mandatory or no validation error") 
                                print_statements.append("'Type' Field is not mandatory or no validation error")
                                pass



                            field_element = driver.find_element(By.NAME ,'chapters')
                            operator = field_element.get_attribute('outerHTML')
                            # print(html)
                            if "required" in operator:
                                print("'operator' Field is mandatory. Please fill it.")
                                print_statements.append("'operator' Field is mandatory. Please fill it.")

                            else:
                                print("'operator' Field is not mandatory or no validation error")
                                print_statements.append("'operator' Field is not mandatory or no validation error")
                                 
                                pass

                            #Area of Audit
                            field_element = driver.find_element(By.ID ,'select2-area_audit_id-container')
                            Area_audit = field_element.get_attribute('outerHTML')
                            if "required" in Area_audit:
                                print("'Area of Audit' Field is mandatory. Please fill it.")
                                print_statements.append("'Area of Audit' Field is mandatory. Please fill it.")
                            else:
                                print("'Area of Audit' Field is not mandatory or no validation error") 
                                print_statements.append("'Area of Audit' Field is not mandatory or no validation error")
                                pass

                            #dec_description
                            field_element = driver.find_element(By.NAME ,'dec_description')
                            description = field_element.get_attribute('outerHTML')
                            # print(html)
                            if "required" in description:
                                print("'description' Field is mandatory. Please fill it.")
                                print_statements.append("'description' Field is mandatory. Please fill it.")
                            else:
                                print("'description' Field is not mandatory or no validation error") 
                                print_statements.append("'description' Field is not mandatory or no validation error")
                                pass

                        except:
                            pass

                        input_element = ["..","alpha1","alpha@1",12345]
                        for j in input_element:
                            # driver.get(decision_reports_url)
                            try:
                                
                                driver.get(decision_reports_url)
                                time.sleep(1)
                                add_element = driver.find_element(By.ID ,id_list[i])
                                add_element.click()
                                print("check1")
                                time.sleep(1)
                                
                                

                                driver.find_element(By.NAME ,'dec_name').send_keys(j)
                                time.sleep(0.2)
                                driver.find_element(By.ID,"select2-dec_type-container").click()
                                time.sleep(1)
                                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                                search.send_keys("normal")
                                search.send_keys(Keys.RETURN)
                                driver.find_element(By.ID,"select2-chapters-container").click()
                                time.sleep(1)
                                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                                search.send_keys("others")
                                search.send_keys(Keys.RETURN)

                                driver.find_element(By.ID,"select2-area_audit_id-container").click()
                                time.sleep(1)
                                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                                search.send_keys("Audit of Account Receivable & Payable")
                                search.send_keys(Keys.RETURN)

                                driver.find_element(By.NAME ,'dec_description').send_keys(j)   
                                driver.find_element(By.ID , 'btnsb').click()   
                                # print(html)
                                if "alert alert-danger text-center alert-dismiss " in html:
                                    print("already exists")
                                    print_statements.append("already exists")
                                if "alert alert-success text-center alert-dismiss " in html:
                                    print("new record created")
                                    print_statements.append("new record created")
                                #     message = element.text
                            #     print(message)
                            except Exception as e:
                                print("error",e)

                        driver.get(decision_reports_url)
                        time.sleep(1)
                        add_element = driver.find_element(By.ID ,id_list[i])
                        add_element.click()
                        time.sleep(1)


                        driver.find_element(By.NAME ,'dec_name').send_keys("new_decision")
                        time.sleep(0.2)
                        driver.find_element(By.ID,"select2-dec_type-container").click()
                        time.sleep(1)
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        search.send_keys("normal")
                        search.send_keys(Keys.RETURN)
                        driver.find_element(By.ID,"select2-chapters-container").click()
                        time.sleep(1)
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        search.send_keys("others")
                        search.send_keys(Keys.RETURN)

                        driver.find_element(By.ID,"select2-area_audit_id-container").click()
                        time.sleep(1)
                        search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        search.send_keys("Audit of Account Receivable & Payable")
                        search.send_keys(Keys.RETURN)

                        driver.find_element(By.NAME ,'dec_description').send_keys("New_description")                 
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
                        unique_id = random.randint(1000, 9999)
                        test = "test"+str(unique_id)
                        driver.find_element(By.XPATH , '//*[@id="decisionid_filter"]/label/input').send_keys("new_decision")
                        driver.find_element(By.ID ,'edit').click()
                        
                        time.sleep(0.2)
                        decision_btn = driver.find_element(By.NAME ,'dec_name')
                        decision_btn.clear()
                        decision_btn.send_keys(test)
                        time.sleep(0.2)              
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

                        
                    elif flow[i] == "delete":
                        driver.find_element(By.XPATH , '//*[@id="decisionid_filter"]/label/input').send_keys(test)
    #                     search_btn.send_keys("new_checklist")
                        delete_btn = driver.find_element(By.NAME ,'mark_inacticve')
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
                driver.get(decision_reports_url)
                
                try:
                    add_element = driver.find_element(By.ID ,id_list[i])
    #                 if not add_element:
    #                 print("button not  exists and no error")
                except:
                    add_element = ""
                    pass
                print(add_element,"this is add_elelmtn")
                print_statements.append(add_element,"this is add_elelmtn")
                if add_element:
                    print("ERROR:button exists and error")
                    print_statements.append("ERROR:button exists and error")
                else:
                    print("nobutton and no error")
                    print_statements.append("nobutton and no error")

                df = pd.DataFrame({"Print Statements": print_statements})

    # Save the DataFrame to an Excel file
        unique_id = random.randint(1000, 9999)
        excelsave = "Decisions"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)
        return True