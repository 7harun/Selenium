from flask import Flask, render_template, request
from threading import Thread
from selenium import webdriver
from dateHub_add_assignment import Datehub_add_assignment
from FIFW import fifwclass
from User_add_assignment import User_add_assignment
from AddCluster_assignment import AddClusterreport
from edit_milestone import EditMilestone
from editMilestoneUpdates import EditMilestoneUpdates
from StandardisedReports import Standardised_reports
from Auditplanningtemplate import APT
from Conditions import CheckConditions
from AuditVariables import Auditvariables
from Risks import Risks
from Annexures import Annexures
from Decisions import Decisions
from Compliance_calender import Compliancecalender
from Standard_text import Standard_text
from CustomReports import Custom_Reports


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_selenium', methods=['POST'])
def run_selenium():

    # Define your Selenium automation script here
    def selenium_script():
        
        datehubaddassignment = Datehub_add_assignment.datehub_add_assignment()
        print(datehubaddassignment)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/run_fifw', methods=['POST'])
def run_fifw():

    # Define your Selenium automation script here
    def selenium_script():
        
        fifw_obj = fifwclass.fifw()
        print(fifw_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/run_useraddassignment', methods=['POST'])
def run_useraddassignment():

    # Define your Selenium automation script here
    def selenium_script():
        
        useraddassignemnt_obj = User_add_assignment.user_add_assignment()
        print(useraddassignemnt_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script



@app.route('/Addclusterreport', methods=['POST'])
def Addclusterreport():

    # Define your Selenium automation script here
    def selenium_script():
        
        addclusterreport_obj = AddClusterreport.addClusterreport()
        print(addclusterreport_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script




@app.route('/editmilestone', methods=['POST'])
def run_Editmilestone():

    # Define your Selenium automation script here
    def selenium_script():
        
        Editmilestone_obj = EditMilestone.editMilestone()
        print(Editmilestone_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/editmilestoneupdates', methods=['POST'])
def run_Editmilestoneupdates():

    # Define your Selenium automation script here
    def selenium_script():
        
        Editmilestoneupd_obj = EditMilestoneUpdates.editMilestoneupdates()
        print(Editmilestoneupd_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/standardisedreports', methods=['POST'])
def run_Standardisedreports():

    # Define your Selenium automation script here
    def selenium_script():
        
        standardisedreports_obj = Standardised_reports.standardised_reports()
        print(standardisedreports_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/apt', methods=['POST'])
def apt():

    # Define your Selenium automation script here
    def selenium_script():
        
        apt_obj = APT.apt()
        print(apt_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script

@app.route('/condition', methods=['POST'])
def condition():

    # Define your Selenium automation script here
    def selenium_script():
        
        condition_obj = CheckConditions.checkconditions()
        print(condition_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script



@app.route('/auditvariable', methods=['POST'])
def run_Auditvariables():

    # Define your Selenium automation script here
    def selenium_script():
        
        AuditVariable_obj = Auditvariables.audit_variable()
        print(AuditVariable_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/risks', methods=['POST'])
def run_Risks():

    # Define your Selenium automation script here
    def selenium_script():
        
        Risks_obj = Risks.risks()
        print(Risks_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script\
    


@app.route('/decisions', methods=['POST'])
def run_Decision():

    # Define your Selenium automation script here
    def selenium_script():
        
        decision_obj = Decisions.decisions()
        print(decision_obj)
        # driver.get('path/to/webpage.html')

        # Your Selenium code here
        # Interact with elements on the webpage (e.g., fill forms, click buttons, etc.)
        # Perform automated testing using Selenium

        # driver.quit()

    # Run the Selenium script in a separate thread
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/annexures', methods=['POST'])
def run_Annexures():

    # Define your Selenium automation script here
    def selenium_script():
        
        decision_obj = Annexures.annexures()
        print(decision_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script

@app.route('/cc', methods=['POST'])
def run_CC():

    # Define your Selenium automation script here
    def selenium_script():
        
        cc_obj = Compliancecalender.compliance_calender()
        print(cc_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/standard', methods=['POST'])
def run_standard():

    # Define your Selenium automation script here
    def selenium_script():
        
        st_obj = Standard_text.standard_text()
        print(st_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/customreport', methods=['POST'])
def run_customreports():

    # Define your Selenium automation script here
    def selenium_script():
        
        cr_obj = Custom_Reports.cutomreports()
        print(cr_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script

if __name__ == '__main__':
    app.run()
