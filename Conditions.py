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


class CheckConditions:
    def checkconditions():
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
        driver.find_element(By.ID,"Conditions").click()
        time.sleep(1)
        condition_url = driver.current_url
        # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
        # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,condition_url,check_element_path)
        # print(checkinassignment)
        driver.get("https://old.anyaudit.co.in/Management/users")
        search = driver.find_element(By.ID  ,"txtSearch")
        search.send_keys("tharun")
        search.send_keys(Keys.RETURN)

        time.sleep(0.2)
        # driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        new_page_url = driver.current_url

        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[8]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[40]/td[2]/input','//*[@id="32"]/div/div/table/tbody/tr[24]/td[2]/input']
        id_list = ['add_conditions','edit','delete']
        flow = ["add","edit","delete"]
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
                driver.get(condition_url)
                try:
                    add_element = driver.find_element(By.ID ,id_list[i])
    #                 print("button exists and no error")
                except:
                    add_element = ""
                    if flow[i] == "delete":
                        add_element = "delete"
                    pass
                if add_element:
                    print("button exists and no error")
                    if flow[i] == "add":
                        add_element.click()
                        time.sleep(0.2)

                        driver.find_element(By.ID , 'btnsb').click()


                        try:
                            # Find the field element that contains the mandatory star mark
                            # ConditionName
                            field_element = driver.find_element(By.NAME ,'cond_name')
                            # has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
                            # is_mandatory = "*" in field_element.text
                            cname = field_element.get_attribute('outerHTML')
                            # print(html)
                            if "required" in cname:
                                print("'ConditionName' Field is mandatory. Please fill it.")
                            # if "alert alert-success text-center alert-dismiss " in cname:
                            #     print("new record created")
                            # if has_validation_error or is_mandatory:
                            #     print("'ConditionName' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'ConditionName' Field is not mandatory or no validation error") 
                                pass


                            field_element = driver.find_element(By.XPATH ,'//*[@id="fact_decision_id"]')
                            has_validation_error = field_element.get_attribute("class") == "your-validation-error-class"
                            is_mandatory = "*" in field_element.text

                            if has_validation_error or is_mandatory:
                                print("'Variable' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'Variable' Field is not mandatory or no validation error") 
                                pass

                            field_element = driver.find_element(By.NAME ,'operator')
                            operator = field_element.get_attribute('outerHTML')
                            # print(html)
                            if "required" in operator:
                                print("'operator' Field is mandatory. Please fill it.")
                            # if "alert alert-success text-center alert-dismiss " in cname:
                            #     print("new record created")
                            # if has_validation_error or is_mandatory:
                            #     print("'ConditionName' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'operator' Field is not mandatory or no validation error") 
                                pass


                            field_element = driver.find_element(By.NAME ,'value_one')
                            value1 = field_element.get_attribute('outerHTML')
                            # print(html)
                            if "required" in value1:
                                print("'value1' Field is mandatory. Please fill it.")
                            # if "alert alert-success text-center alert-dismiss " in cname:
                            #     print("new record created")
                            # if has_validation_error or is_mandatory:
                            #     print("'ConditionName' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'value1' Field is not mandatory or no validation error") 
                                pass

                            field_element = driver.find_element(By.NAME ,'cond_desc')
                            description = field_element.get_attribute('outerHTML')
                            # print(html)
                            if "required" in description:
                                print("'description' Field is mandatory. Please fill it.")
                            # if "alert alert-success text-center alert-dismiss " in cname:
                            #     print("new record created")
                            # if has_validation_error or is_mandatory:
                            #     print("'ConditionName' Field is mandatory. Please fill it.")
                            else:
                            #     Field is not mandatory or no validation error
                                print("'description' Field is not mandatory or no validation error") 
                                pass

                        except:
                            pass



                        input_element = ["..","alpha1","alpha@1",12345]
                        for j in input_element:
                            # driver.get(decision_reports_url)
                            try:
                                
                                driver.get(condition_url)
                                time.sleep(1)
                                add_element = driver.find_element(By.ID ,id_list[i])
                                add_element.click()
                                print("check1")
                                time.sleep(1)
                                driver.find_element(By.ID ,'cond_name').send_keys(j)
                                driver.find_element(By.ID,"select2-fact_decision_id-container").click()
                                btn = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                                driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("test")
                                btn.send_keys(Keys.RETURN)
                                time.sleep(0.2)
                            
                                driver.find_element(By.ID,"select2-operator-container").click()
                                op_btn = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                                driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("equal to")
                                op_btn.send_keys(Keys.RETURN)
                                time.sleep(0.5)
                                driver.find_element(By.NAME,"value_one").send_keys(j)
                                try:
                                    driver.find_element(By.NAME,"value_two").send_keys(j)
                                except:
                                    pass
                                driver.find_element(By.ID,"cond_desc").send_keys(j)                        
                                
                                time.sleep(2)
                                driver.find_element(By.ID , 'btnsb').click()
                                time.sleep(1)
                                
                                # print(html)
                                if "alert alert-danger text-center alert-dismiss " in html:
                                    print("already exists")
                                if "alert alert-success text-center alert-dismiss " in html:
                                    print("new record created")
                                #     message = element.text
                            #     print(message)
                            except Exception as e:
                                print("error",e)

                        driver.get(condition_url)
                        time.sleep(1)
                        add_element = driver.find_element(By.ID ,id_list[i])
                        add_element.click()
                        time.sleep(1)
                        
                        
                        driver.find_element(By.ID ,'cond_name').send_keys("new_condition32333")
                        driver.find_element(By.ID,"select2-fact_decision_id-container").click()
                        time.sleep(0.5)
                        try:
                            alert = driver.switch_to.alert
                            alert.accept()
                            time.sleep(2)
                            print("condition already exists")
                            continue
                        except Exception as e:
                            print(e)
                            print("entered into exception")
                            pass
                        
                        btn = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("test")
                        btn.send_keys(Keys.RETURN)
                        time.sleep(0.2)
                        try:
                            driver.find_element(By.ID,"select2-operator-container").click()
                            op_btn = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                            driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("equal to")
                            op_btn.send_keys(Keys.RETURN)
                            time.sleep(0.5)
                            driver.find_element(By.NAME,"value_one").send_keys(10)
                            try:
                                driver.find_element(By.NAME,"value_two").send_keys(11)
                            except:
                                pass
                            driver.find_element(By.ID,"cond_desc").send_keys("cond_description")                        
                            
                            time.sleep(2)
                            driver.find_element(By.ID , 'btnsb').click()
                            time.sleep(1)
                            check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                            # Get the HTML of the element
                            html = check_status.get_attribute('outerHTML')
        #                     print(html,"this is html")
                            if "alert alert-danger text-center alert-dismiss " in html:
                                print("conditions already exists")
                            if "alert alert-success text-center alert-dismiss " in html:
                                print("new conditions created")
                        except:
                            alert = driver.switch_to.alert
                            alert.accept()
                            time.sleep(2)
                            
                    elif flow[i] == "edit":
                        unique_id = random.randint(1000, 9999)
                        test = "test"+str(unique_id)
                        # search = driver.find_element(By.ID,"con_data_filter")
                        # search.click()
                        driver.find_element(By.XPATH,'//*[@id="con_data_filter"]/label/input').send_keys("new_condition32333")
                        driver.find_element(By.ID,"edit").click()
                        time.sleep(0.5)
                        con = driver.find_element(By.ID ,'cond_name')
                        con.clear()

                        con.send_keys(test)
                        driver.find_element(By.ID,"select2-fact_decision_id-container").click()
                        btn = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("test")
                        btn.send_keys(Keys.RETURN)
                        driver.find_element(By.ID,"select2-operator-container").click()
                        op_btn = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                        driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("equal to")
                        op_btn.send_keys(Keys.RETURN)
                        time.sleep(0.5)
                        value1 = driver.find_element(By.NAME,"value_one")
                        value1.clear()
                        value1.send_keys(10)
                        try:
                            value2 = driver.find_element(By.NAME,"value_two")
                            value2.clear()
                            value2.send_keys(11)
                        except:
                            pass
                        con_desc = driver.find_element(By.ID,"cond_desc")
                        con_desc.clear()
                        con_desc.send_keys("cond_description")                        
                        
                        time.sleep(2)
                        driver.find_element(By.ID , 'btnsb').click()
                        
                        check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                        # Get the HTML of the element
                        html = check_status.get_attribute('outerHTML')
    #                     print(html,"this is html")
                        if "alert alert-danger text-center alert-dismiss " in html:
                            print("conditions already exists")
                        if "alert alert-success text-center alert-dismiss " in html:
                            print("new conditions created")
                        
                    elif flow[i] == "delete":
                        time.sleep(1)
                        driver.find_element(By.XPATH,'//*[@id="con_data_filter"]/label/input').send_keys(test)
                        time.sleep(1)
                        driver.find_element(By.ID,"edit").click()
                        time.sleep(0.5)
                        driver.find_element(By.ID,"delete").click()
                        alert = driver.switch_to.alert
                        alert.accept()
                        time.sleep(2)


                else:
                    print("ERROR:nobutton and error")
                

                
            else:
                print("unchecked")
                flag = "unchecked"
                driver.get(condition_url)
                
                try:
                    id = id_list[i]
                    if(id == "delete"):
                        id = "edit"
                    add_element = driver.find_element(By.ID ,id)
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