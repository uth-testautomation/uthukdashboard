import os
import shutil
from zipfile import ZipFile
import datetime
from utils import sevendays_cron as cron
from utils.local_cache import Caching

def creating_zip_file():
    # zipping all the files in the log folder
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    XCAL_Log_directory = os.path.join(desktop_path, "XCAL_Logs")
    os.chdir("..\\..")
    adb_log_file = os.listdir(os.getcwd())
    for file in adb_log_file:
        if file.__contains__("Date") and file.__contains__("Time"):
            shutil.move(file, XCAL_Log_directory)
            # os.remove(file)
    XCAL_Log_path = os.path.join(os.getcwd(), "XCAL_Logs")
    if (os.path.exists(XCAL_Log_path)):
        shutil.rmtree(XCAL_Log_path)

    shutil.copytree(XCAL_Log_directory,XCAL_Log_path)

    print("Zipping the files")
    current_time = datetime.datetime.now()
    time_stamp = current_time.timestamp()
    date_time = datetime.datetime.fromtimestamp(time_stamp)
    str_date_time = "Date_" + date_time.strftime("%d_%m_%Y_Time_%H_%M_%S") + ".zip"

    zipped_log_file = os.path.join(os.getcwd(), str_date_time)
    with ZipFile(zipped_log_file, 'w') as zip_object:
        for folder_name, sub_folder, file_name in os.walk(XCAL_Log_path):
            for filename in file_name:
                file_path = os.path.join(folder_name,filename)
                zip_object.write(file_path,os.path.basename(file_path))
    traces_path = os.path.join(os.getcwd(), "traces")
    # shutil.copy(zipped_log_file,traces_path)
    shutil.move(zipped_log_file,traces_path)
    cron.sevendaysCron(traces_path)

    # for file in adb_log_file:
    #     if file.__contains__("Date") and file.__contains__("Time"):
    #         print("filename: " + file)
    #         os.remove(file)

    # shutil.rmtree(XCAL_Log_directory)