import os
import subprocess
import pathlib
import time
import psutil
import datetime
import shutil
import re


current_working_dir = os.getcwd();
XCAL_Log_path = os.path.join(current_working_dir, "XCAL_Logs")
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
XCAL_Log_directory = os.path.join(desktop_path, "XCAL_Logs")

def Start_Logging():
    try:
        project_path = pathlib.Path(__file__).parent.parent
        # print(project_path)
        cmd = str(project_path).replace("\\","/") + '/voLTE/DMRacTest_Sample/Sample_Logging_Start.cmd'
        subprocess.call(cmd)
    except Exception as e:
        print(f"Unable to start the logs \n"
              f"1.Check for XCAL is up and running"
              f"\n1.Check if TM/Test-Manager is enabled"
              f"\nException: {e}")


def Stop_Logging(destination_directory, new_file_name):

    try:
        project_path = pathlib.Path(__file__).parent.parent
        cmd = str(project_path).replace("\\","/") + '/voLTE/DMRacTest_Sample/Sample_Logging_Stop.cmd'
        subprocess.call(cmd)
        time.sleep(0.3)
        move_file(destination_directory, new_file_name)
        time.sleep(0.2)
    except Exception as e:
        print(f"Unable to stop the logs \n"
              f"1.Check for XCAL is up and running"
              f"\n1.Check if TM/Test-Manager is enabled"
              f"\nException: {e}")


def move_file(destination_directory, new_file_name):

    expected_filename = new_file_name

    try:
        file_location = destination_directory

        timestamp = datetime.datetime.now().timestamp()
        formatted_string = datetime.datetime.fromtimestamp(timestamp).strftime("_Date_%Y_%m_%d_Time_%H_%M_%S")
        print("Formatted Timestamp:", formatted_string)

        for filename in os.listdir(destination_directory):
            if filename.startswith("SRAN10.1_VoLTE-Enhancement_") and filename.endswith(".aof"):
                source_file = str(file_location).replace("\\", "/") + "/" + str(filename)
                match = re.search(r'M(\d+)\.aof$', filename)
                num = match.group(1)
                new_file_name = str(new_file_name) + str(formatted_string) +"_M"+str(num)+ str(".aof")
                destination_file = os.path.join(destination_directory, new_file_name)
                shutil.move(source_file, destination_file)
                print(f"File moved from {source_file} to {destination_file}")
                new_file_name = expected_filename
    except Exception as e:
        print(f"Exception: {e}")



# def get_XCAL_Filename(Subscriber, test_name):

#     filename = None
#     # test_name = "TC014_Call_Forward_Not_Answer_"
#     numb = {
#         '07944531930':'M1',
#         '07581045780':'M2',
#         '07944532088':'M3'
#     }

#     # list_of_files = os.listdir(os.path.join(os.path.expanduser("~"), "Desktop\\XCAL_Logs"))

#     # with allure.step(str(list_of_files)): pass

#     for file in XCAL_Log_path:
#         # with allure.step(str(file)): pass
#         if file.startswith(test_name) and numb[Subscriber] in file and file.endswith(".aof"):
#             filename = os.path.join(XCAL_Log_path, file)

#     return filename

# def move_file(destination_directory, new_file_name):
#
#     expected_filename = new_file_name
#
#     try:
#         file_location = destination_directory
#
#         timestamp = datetime.datetime.now().timestamp()
#         formatted_string = datetime.datetime.fromtimestamp(timestamp).strftime("_Date_%Y_%m_%d_Time_%H_%M_%S")
#         print("Formatted Timestamp:", formatted_string)
#
#         # new_file_name = str(new_file_name) + str(formatted_string) + str(".aof")
#         count = 1
#         for filename in os.listdir(destination_directory):
#             if filename.startswith("SRAN10.1_VoLTE-Enhancement_") and filename.endswith(".aof"):
#                 source_file = str(file_location).replace("\\", "/") + "/" + str(filename)
#                 new_file_name = str(new_file_name) + str(formatted_string) +"_M"+str(count)+ str(".aof")
#                 count=count+1
#                 destination_file = os.path.join(destination_directory, new_file_name)
#                 shutil.move(source_file, destination_file)
#                 print(f"File moved from {source_file} to {destination_file}")
#                 new_file_name = expected_filename
#     except Exception as e:
#         print(f"Exception: {e}")

def Launch_XCAL():
    # Based on the given inputs it is derived that the application resides in below default location
    try:
        os.startfile(u"C:\\Program Files (x86)\\Accuver\\XCAL-M\\XCAL-M.exe")
        time.sleep(95)
        # Place a verification check-point here to see if the app is launched successfully
    except Exception as e:
        print(f"Unable to launch file from the location C:/Program Files (x86)/Accuver/XCAL-M/XCAL-M.exe\n"
              f"Check for the file in above location\nException: {e}")


def Stop_XCAL():
    process_name = "XCAL-M.exe"
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            try:
                pid = process.info['pid']
                p = psutil.Process(pid)
                try:
                    p.terminate()
                except:
                    p.kill()  # to forcefully terminate
                print(f"Process {process_name} (PID {pid}) terminated.")
            except psutil.NoSuchProcess as e:
                print(f"Error terminating process: {e}")

