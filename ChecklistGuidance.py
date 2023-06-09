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


class ChecklistGuidance:
    def checklistguidance():
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
        driver.find_element(By.ID,"CheckLists").click()
        time.sleep(1)
        checklistpage_url = driver.current_url
        xpath_list_perm_page = ['//*[@id="32"]/div/div/table/tbody/tr[4]/td[2]/input']
        unique_id = random.randint(1000, 9999)
        checklist = "checklist_"+str(unique_id)

        driver.get("https://old.anyaudit.co.in/Management/users")
        search = driver.find_element(By.ID  ,"txtSearch")
        search.send_keys("tharun")
        search.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[1]/ul/li[3]/div/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH  ,'/html/body/section/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[11]/a[1]/button').click()
        
        print_statements = []

        check_status = driver.find_element(By.XPATH  ,xpath_list_perm_page[0])
            # Get the HTML of the element
        html = check_status.get_attribute('outerHTML')
            
        if "checked" in html:
            print("checked")
            
            driver.get(checklistpage_url)
            try:
                add_element = driver.find_element(By.NAME,"add")
#                 print("button exists and no error")
            except:
                add_element = ""
                pass
            if add_element:

                time.sleep(2)
                driver.find_element(By.NAME,"add").click()
                time.sleep(1)
                driver.find_element(By.NAME,"checklist_name").send_keys(checklist)
                time.sleep(1)

                driver.find_element(By.ID,"select2-chapters-container").click()
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("others")
                search.send_keys(Keys.RETURN)


                driver.find_element(By.ID,"select2-area_audit_id-container").click()
                search = driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                search.send_keys("account")
                search.send_keys(Keys.RETURN)

                
                driver.find_element(By.ID,"btnsb").click()

                time.sleep(1)
                check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                # Get the HTML of the element
                html = check_status.get_attribute('outerHTML')

                time.sleep(2)
                if "alert alert-danger text-center alert-dismiss " in html:
                        print("checklist already exists")
                        print_statements.append("checklist already exist")
                if "alert alert-success text-center alert-dismiss " in html:
                        print("new checklist created")
                        print_statements.append("new checklist created")

                

                
                

                
                driver.find_element(By.XPATH,'//*[@id="checklistid_filter"]/label/input').send_keys(checklist)
                time.sleep(0.2)
                driver.find_element(By.NAME,"config").click()
                checklistconfigpage = driver.current_url
                try:
                    new = driver.find_element(By.NAME,"guidance")
                except:
                    new = ""
                    pass
                if not new:
                    driver.find_element(By.NAME,"addnode").click()
                    time.sleep(0.2)
                    unique_id = random.randint(1000, 9999)
                    node = "node_"+str(unique_id)
                    driver.find_element(By.NAME,"short_checklist").send_keys(node)
                    driver.find_element(By.ID,"select2-desired_result-container").click()
                    search1 = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
                    search1.send_keys("No")
                    search1.send_keys(Keys.RETURN)
                    driver.find_element(By.ID,"select2-na_as-container").click()
                    search2 = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
                    search2.send_keys("No")
                    search2.send_keys(Keys.RETURN)
                    driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div[3]/div[2]/p/br").send_keys("desc")
                    time.sleep(0.2)
                    driver.find_element(By.ID,"submitid").click()
                    time.sleep(1)

                    
                    driver.get(checklistconfigpage)
                    new = driver.find_element(By.NAME,"guidance")
                new.click()
                guidance_url = driver.current_url

                # check_element_path = '//*[@id="navbar1"]/div[2]/div/button/i'
                # checkinassignment = CheckUrlinAssignment.checkurlinassignment(driver,guidance_url,check_element_path)
                # print(checkinassignment)
                time.sleep(0.2)
                driver.get(guidance_url)
                try:
                    driver.find_element(By.NAME ,'short').send_keys("new_short1")
                    time.sleep(0.2)
                    driver.find_element(By.NAME ,'guidance_notes_name').send_keys("guidance_notes_name")
                    time.sleep(0.2)
                    driver.find_element(By.NAME ,'reference').send_keys("reference")
                    time.sleep(0.2)
                    driver.find_element(By.XPATH ,'/html/body/section/div/div/div/div/div/form/div[4]/div[2]/div/div/div/div[3]/div[2]').send_keys("description")
                    time.sleep(0.2)
                    
                    
                    
                    button = driver.find_element(By.ID ,'save')
                    driver.execute_script("arguments[0].click();", button)

                    
                    
                    check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                    # Get the HTML of the element
                    html = check_status.get_attribute('outerHTML')
            #                     print(html,"this is html")
                    if "alert alert-danger text-center alert-dismiss " in html:
                        print("Node already exists")
                        print_statements.append("checklist already exist")
                    if "alert alert-success text-center alert-dismiss " in html:
                        print("new Node created")
                        print_statements.append("new Node created")
                except Exception as e:
                    print(e)
                    print("cannot add node guidance")
                    print_statements.append("cannot add node guidance")
            
                time.sleep(4) 
                driver.refresh()

                try:
                    # Find the row where Short Answer is "new_short1"
                    row_element = driver.find_element(By.XPATH, "//tr[td[contains(text(), 'new_short1')]]")

                    # Click the edit button in the row
                    edit_button = row_element.find_element(By.ID, "edit")
                    edit_button.click()
                    # edit_button.click()
                    time.sleep(1)
                    new_short = driver.find_element(By.NAME ,'short')
                    new_short.clear()
                    new_short.send_keys("new_short_update")
                    time.sleep(0.2)
                    guidance_notes_name = driver.find_element(By.NAME ,'guidance_notes_name')
                    guidance_notes_name.clear()
                    guidance_notes_name.send_keys("guidance_notes_name_update")
                    time.sleep(0.2)
                    reference = driver.find_element(By.NAME ,'reference')
                    reference.clear()
                    reference.send_keys("reference_update")
                    time.sleep(0.2)
                    description = driver.find_element(By.XPATH ,'/html/body/section/div/div/div/div/div/form/div[4]/div[2]/div/div/div/div[3]/div[2]')
                    description.clear()
                    description.send_keys("description_update")
                    time.sleep(0.2)
                    button = driver.find_element(By.ID ,'save')
                    driver.execute_script("arguments[0].click();", button)
                    check_status = driver.find_element(By.XPATH  ,'/html/body/section/div/div[1]')
                    # Get the HTML of the element
                    html = check_status.get_attribute('outerHTML')
            #                     print(html,"this is html")
                    if "alert alert-danger text-center alert-dismiss " in html:
                        print("Guidance already exists")
                        print_statements.append("Guidance already exists")
                    if "alert alert-success text-center alert-dismiss " in html:
                        print("new Guidance created")
                        print_statements.append("new Guidance created")
                except Exception as e:
                    print(e)
                    print("exception is in edit")
                    print_statements.append("exception is in edit")

                time.sleep(4) 

                driver.refresh()
                try:
                    row_element = driver.find_element(By.XPATH, "//tr[td[contains(text(), 'new_short_update')]]")

                    # Click the edit button in the row
                    delete_button = row_element.find_element(By.ID, "delete")
                    delete_button.click()
                    time.sleep(1)
                except Exception as e:
                    print(e)
                    print("cannot delete guidance")
                    print_statements.append("cannot delete guidence")
            
            else:
                print("ERROR:nobutton and error")
                print_statements.append("ERROR:nobutton and error")


        else:
                print("unchecked")
                flag = "unchecked"
                driver.get(checklistpage_url)
                
                try:
                    add_element = driver.find_element(By.NAME ,"add")
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
        excelsave = "AuditVariable"+str(unique_id)+".xlsx"
        df.to_excel(excelsave, index=False)
        print(excelsave)
        return True