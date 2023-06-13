from flask import Flask, render_template, request
from threading import Thread
from selenium import webdriver
from dateHub_add_assignment import Datehub_add_assignment
from FIFW import fifwclass
from User_add_assignment import User_add_assignment
from User_addplan import User_add_plan
from AddCluster_assignment import AddClusterreport
from edit_milestone import EditMilestone
from editMilestoneUpdates import EditMilestoneUpdates
from StandardisedReports import Standardised_reports
from Auditplanningtemplate import APT
from Conditions import CheckConditions
from AuditVariables import Auditvariables
from Risks import Risks
from Annexures import Annexures
from Annexures_Config import Annexures_config
from Decisions import Decisions
from Compliance_calender import Compliancecalender
from Standard_text import Standard_text
from CustomReports import Custom_Reports
from ChecklistGuidance import ChecklistGuidance
from Controls import Controls
from subdecisions_addcondition import SubDecisions_addcondition
from FIFW_AED import FIFW_AED
from addAPT_toolkit import APT_toolkit
from Datehub_addplan import Datehub_add_plan
from datehub_addmilestone import Datehub_add_MS
from clienthub_addplan import client_add_plan
from clienthub_addMS import client_add_MS
from sub_decisions import SubDecisions
from PAT_Risk import PAT_risk
from PAT_addcontrol import PAT_control
from PAT_answer import PAT_answer
from Cluster_subcategory import Cluster_sub


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


@app.route('/datehubaddplan', methods=['POST'])
def datehubaddplan():

    # Define your Selenium automation script here
    def selenium_script():
        
        datehubaddassignment = Datehub_add_plan.datehub_add_plan()
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


@app.route('/datehubaddMS', methods=['POST'])
def datehubaddMS():

    # Define your Selenium automation script here
    def selenium_script():
        
        datehubaddassignment = Datehub_add_MS.datehub_add_MS()
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


@app.route('/useraddplan', methods=['POST'])
def useraddplan():

    # Define your Selenium automation script here
    def selenium_script():
        
        useraddassignemnt_obj = User_add_plan.user_add_plan()
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


@app.route('/clientaddplan', methods=['POST'])
def clientaddplan():

    # Define your Selenium automation script here
    def selenium_script():
        
        useraddassignemnt_obj = client_add_plan.client_add_plan()
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



@app.route('/clientaddMS', methods=['POST'])
def clientaddMS():

    # Define your Selenium automation script here
    def selenium_script():
        
        useraddassignemnt_obj = client_add_MS.client_add_ms()
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


@app.route('/annexuresconfig', methods=['POST'])
def run_Annexuresconfig():

    # Define your Selenium automation script here
    def selenium_script():
        
        decision_obj = Annexures_config.annexures_config()
        print(decision_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/subdecisionsaddc', methods=['POST'])
def run_subdecision_addcondition():

    # Define your Selenium automation script here
    def selenium_script():
        
        decision_obj = SubDecisions_addcondition.subdecisions_addcondition()
        print(decision_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/pat_addrisk', methods=['POST'])
def run_PAT_addrisk():

    # Define your Selenium automation script here
    def selenium_script():
        
        decision_obj = PAT_risk.PAT_risk()
        print(decision_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/pat_control', methods=['POST'])
def run_PAT_control():

    # Define your Selenium automation script here
    def selenium_script():
        
        decision_obj = PAT_control.PAT_control()
        print(decision_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/pat_answer', methods=['POST'])
def run_PAT_answer():

    # Define your Selenium automation script here
    def selenium_script():
        
        decision_obj = PAT_answer.PAT_answer()
        print(decision_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script




@app.route('/subdecisions', methods=['POST'])
def run_subdecision():

    # Define your Selenium automation script here
    def selenium_script():
        
        decision_obj = SubDecisions.subdecisions()
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


@app.route('/guidance', methods=['POST'])
def run_guidance():

    # Define your Selenium automation script here
    def selenium_script():
        
        cr_obj = ChecklistGuidance.checklistguidance()
        print(cr_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script

@app.route('/controls', methods=['POST'])
def run_control():

    # Define your Selenium automation script here
    def selenium_script():
        
        cr_obj = Controls.controls()
        print(cr_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script

@app.route('/ff', methods=['POST'])
def run_FF():

    # Define your Selenium automation script here
    def selenium_script():
        
        ff_obj = FIFW_AED.fifw_aed()
        print(ff_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script

@app.route('/apt_toolkit', methods=['POST'])
def apt_toolkit():

    # Define your Selenium automation script here
    def selenium_script():
        
        ff_obj = APT_toolkit.apt_toolkit()
        print(ff_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script


@app.route('/cluster_sub', methods=['POST'])
def apt_cluster_sub():

    # Define your Selenium automation script here
    def selenium_script():
        
        ff_obj = Cluster_sub.cluster_sub()
        print(ff_obj)
        
    thread = Thread(target=selenium_script)
    thread.start()

    return selenium_script

if __name__ == '__main__':
    app.run()
