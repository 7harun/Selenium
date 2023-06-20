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


class APT:
    def apt():
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
        driver.find_element(By.ID  ,"txtSearch").send_keys("tharun")
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[9]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[41]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[25]/td[2]/input']
        id_list = ['add_cinfigure_temp','edit','mark_inactive']
        flow = ["add","edit","delete"]
        print_statements = []

        for i in range(0,len(xpath_list_perm_page)):
        
            driver.get(new_page_url)
    #         driver.refresh()
            time.sleep(2)
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
                    print_statements.append("button exists and no error")
                    if flow[i] == "add":
                        add_element.click()

                        time.sleep(1)
                        driver.find_element(By.ID ,'btnsb').click()
                        time.sleep(0.5)
                        try:
                            # Find the field element that contains the mandatory star mark
                            #REPORT_name
                            field_element = driver.find_element(By.NAME ,'template_name')
                            REPORT_name = field_element.get_attribute('outerHTML')
                            if "required" in REPORT_name:
                                print("'REPORT_name' Field is mandatory. Please fill it.")
                                print_statements.append("'REPORT_name' Field is mandatory. Please fill it.")
                            else:
                                print("'REPORT_name' Field is not mandatory or no validation error") 
                                print_statements.append("'REPORT_name' Field is not mandatory or no validation error")
                                pass

                            #  Chapter_name
                            field_element = driver.find_element(By.NAME ,'template')
                            Chapter_name = field_element.get_attribute('outerHTML')
                            if "required" in Chapter_name:
                                print("'Chapter_name' Field is mandatory. Please fill it.")
                                print_statements.append("'Chapter_name' Field is mandatory. Please fill it.")
                            else:
                                print("'Chapter_name' Field is not mandatory or no validation error")
                                print_statements.append("'Chapter_name' Field is not mandatory or no validation error")
                                pass

                        except:
                            pass


                        input_element = ["..","alpha1","alpha@1",12345]
                        for j in input_element:
                            # driver.get(decision_reports_url)
                            try:
                                
                                driver.get(standardised_reports_url)
                                time.sleep(1)
                                add_element = driver.find_element(By.ID ,id_list[i])
                                add_element.click()
                                print("check1")
                                time.sleep(1)                             
                                
                                driver.find_element(By.ID ,'template_name').send_keys(j)
                                time.sleep(0.2)
                                driver.find_element(By.ID,"template").send_keys(j)
                                time.sleep(2)
                                driver.find_element(By.ID , 'btnsb').click()

                                if "alert alert-danger text-center alert-dismiss " in html:
                                    print("already exists")
                                    print_statements.append("already exists")
                                if "alert alert-success text-center alert-dismiss " in html:
                                    print("new record created")
                                    print_statements.append("new record created")
                            except Exception as e:
                                print("ERROR",e)
                                pass
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
                            print_statements.append("APT already exists")
                        if "alert alert-success text-center alert-dismiss " in html:
                            print("new APT created")
                            print_statements.append("new APT created")

                            
                    elif flow[i] == "edit":
                        unique_id = random.randint(1000, 9999)
                        test = "test"+str(unique_id)
                        driver.find_element(By.XPATH , '//*[@id="configuration_act_filter"]/label/input').send_keys("template_test")
                        driver.find_element(By.ID ,'edit').click()
                        time.sleep(1)
                        update_btn = driver.find_element(By.ID ,'template_name')
                        update_btn.clear()
                        update_btn.send_keys(test)
                        time.sleep(1)
                        update_desc = driver.find_element(By.ID,"template")
                        update_desc.clear()
                        update_desc.send_keys(test)
                        time.sleep(2)
                        driver.find_element(By.ID , 'btnsb').click()

                        
                    elif flow[i] == "delete":
                        driver.find_element(By.XPATH , '//*[@id="configuration_act_filter"]/label/input').send_keys(test)
    #                     search_btn.send_keys("new_checklist")
                        delete_btn = driver.find_element(By.ID ,'mark_inactive')
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
                driver.get(standardised_reports_url)
                
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
        excelsave = "AuditPlanningTemplate"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)
        return True