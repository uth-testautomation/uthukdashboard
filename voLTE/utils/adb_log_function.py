import time
import subprocess
import datetime

from utils.local_cache import Caching

caching = Caching()
def clear_adb_logs(Device_ID):

    try:
        for i in range(4):
            clear_command = f"adb -s " + str(Device_ID) + " logcat -c"
            subprocess.Popen(clear_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            time.sleep(0.1)
    except:
        pass


def generate_filename(test_case, device_id):

    current_time = datetime.datetime.now()
    time_stamp = current_time.timestamp()
    date_time = datetime.datetime.fromtimestamp(time_stamp)
    str_date_time = date_time.strftime("%d_%m_%Y_Time_%H_%M_%S")
    Test_caseName = test_case + "_" + device_id + "_"
    filename = Test_caseName + "log_Date_" + str_date_time + ".txt"
    return filename

def create_log_file(device_ID, Test_case):

    try:
        filename = generate_filename(Test_case, str(device_ID))
        return filename
    except:
        pass

def stop_adb_log(Device_ID, testcasename):
    try:
        log_stop_command = f"adb -s " + str(Device_ID) + " logcat -d > " + testcasename
        process = subprocess.Popen(log_stop_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        time.sleep(0.1)
    except:
        pass