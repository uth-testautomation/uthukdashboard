import os
import shutil
import subprocess
from utils import allure_reporting as ar, ftp_logs
from utils import zipping_file as zip

print("Starting Test")

try:
    for filename in os.listdir():
        if (filename.startswith("TC") or filename.startswith("MO")  or filename.startswith("MT")
        or filename.startswith("Log")) and filename.endswith(".txt"):
            os.remove(filename)
except Exception as e:
    print("Error occurred while deleting files:", e)

try:
    os.chdir("..")
    current_working_dir = os.getcwd()
    XCAL_Log_path = os.path.join(current_working_dir, "XCAL_Logs")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    XCAL_Log_directory = os.path.join(desktop_path, "XCAL_Logs")
    shutil.rmtree(XCAL_Log_directory)
    if os.path.exists("XCAL_Logs"):
        shutil.rmtree("XCAL_Logs")
        print("The XCAL Log file has been removed")
    os.makedirs(XCAL_Log_path, exist_ok=True)
    os.makedirs(XCAL_Log_directory, exist_ok=True)
    for filename in os.listdir(str(XCAL_Log_path)):
        os.remove(os.path.join(XCAL_Log_path, filename))
except Exception as e:
    print("Error occurred while deleting files:", e)

if os.path.exists("allure-report"):
    shutil.rmtree("allure-report")

if os.path.exists("allure-result"):
    shutil.rmtree("allure-result")

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

try:
    command = f"behave -v --no-skipped --tags=all -f allure_behave.formatter:AllureFormatter -o allure-result .\\features"
    print("\nRunning 'behave' command :\n\n", command)
    subprocess.run(command, check=True)
    print("Skipping")

except Exception as e:
    print("Error occurred \n", e)


ar.allure_reporting()
zip.creating_zip_file()
ftp_logs.ftp_logs()