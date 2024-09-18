import datetime
import json
import os
import shutil
import subprocess, time

from utils.local_cache import Caching
from utils import sevendays_cron as cron

current_working_dir = os.getcwd()
xcal_log_path = os.path.join(current_working_dir, "XCAL_Logs")
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
xcal_log_directory = os.path.join(desktop_path, "XCAL_Logs")

caching = Caching()
def allure_reporting():
    # Generate Allure report
    # generate_command = f"allure generate allure-result -o allure-report --clean"
    # os.chdir("..")
    generate_command = f"allure generate --single-file allure-result --clean"
    print("\nRunning generate allure-result command : \n\n", generate_command)
    subprocess.run(generate_command, shell=True, check=True)

    oldfile = os.path.join('allure-report', 'index.html')
    current_time = datetime.datetime.now()
    time_stamp = current_time.timestamp()
    date_time = datetime.datetime.fromtimestamp(time_stamp)
    str_date_time = "Date_" + date_time.strftime("%d_%m_%Y_Time_%H_%M_%S") + ".html"
    newfile = os.path.join(os.getcwd(),'allure-report', str_date_time)
    os.rename(oldfile,newfile)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    XCAL_Log_directory = os.path.join(desktop_path, "XCAL_Logs")
    print("the allure report directory is:" + newfile)
    shutil.copy(newfile, XCAL_Log_directory)
    allure_history = os.path.join(os.getcwd(),"templates\\allure-report-history")
    print("allure_history: " + allure_history)
    shutil.copy(newfile, allure_history)
    try:
        config_file = os.path.join(os.getcwd(),"_internal\\config\\deviceConfig.json")
        allure_report_history = os.path.join(os.getcwd(), "templates\\report-drafts")
        with open(config_file, 'r') as file:
            data = json.load(file)
        email_ids = data.get('emailIds', [])
        if email_ids:
            print("email ids:", email_ids)
            shutil.copy(newfile, allure_report_history)
        else:
            print("email ids not found")
    except FileNotFoundError:
        print("Config file not found")
    except json.JSONDecodeError:
        print("Error decoding JSON from the config file")    # allure_report_history = os.path.join(allure_history,"allure-report-history")

    time.sleep(2)

    report_cmd = f"allure serve allure-result\\"
    print("\nRunning allure serve command : \n\n", report_cmd)
    # subprocess.run(report_cmd, shell=True, check=True)
    subprocess.Popen(report_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    #Clearing the logs older than 7 days
    behave_logs = os.path.join(os.getcwd(), "logs")
    cron.sevendaysCron(behave_logs)
    cron.sevendaysCron(allure_history)
    cron.sevendaysCron(allure_report_history)