import subprocess
import os
import time
import datetime
import allure

from utils import XCAL_Logs

# from utils import XCAL_Logs
from utils import adb_log_function as adb
from utils import common_call as lb
from utils.local_cache import Caching

caching = Caching()


class function:

    # def __init__(self, context):
    #     self.context = context
    def __init__(self):
        pass

    def fetch_connected_deviceList(self):
        # Retrieve the devices id

        adb_device_list = []
        adb_device_list.clear()
        abd_dev = subprocess.check_output("adb devices").splitlines()
        for line in abd_dev:
            device_line = str(line)
            if "device'" in device_line:
                device = device_line.split("'")
                d = device[1].rstrip("\\tdevice")
                adb_device_list.append(d)
        # print(adb_device_list)
        return adb_device_list

    def fetch_connected_phone_numbers(self, abd_device_list):

        devices_mobile_number = []
        print("cwd: " + os.getcwd())
        with open(os.path.join(os.getcwd(),"voLTE", "Devices.txt"), 'r') as file:
            for device_data in file:
                devices_mobile_number.append(device_data.rstrip('\n'))
        # print("devices_mobile_number")
        # print(devices_mobile_number)

        connected_phone_numbers = []
        for device in devices_mobile_number:
            for adb in abd_device_list:
                if adb in device:
                    connected_phone_numbers.append(device.rstrip('\n'))

        # print(connected_phone_numbers)
        return connected_phone_numbers

    def generate_filename(self, test_case, device_id):

        current_time = datetime.datetime.now()
        time_stamp = current_time.timestamp()
        date_time = datetime.datetime.fromtimestamp(time_stamp)
        str_date_time = date_time.strftime("%d_%m_%Y_Time_%H_%M_%S")
        Test_caseName = test_case + device_id + "_"
        filename = Test_caseName + "log_Date_" + str_date_time + ".txt"
        return filename

    def adb_device_list(self):

        adb_device_list = []
        adb_device_list.clear()
        abd_dev = subprocess.check_output("adb devices").splitlines()
        for line in abd_dev:
            device_line = str(line)
            if "device'" in device_line:
                device = device_line.split("'")
                d = device[1].rstrip("\\tdevice")
                adb_device_list.append(d)
        # print(adb_device_list)
        return adb_device_list

    def start_XCAL_N_adb(self, MO_device_ID, MO_Filename):

        # Start XCAL-Logs
        XCAL_Logs.Start_Logging()

        # Clear ADB logs from the devices
        adb.clear_adb_logs(MO_device_ID)
        # adb.clear_adb_logs(MT_device_ID)

        # Run adb logcat and redirect output to file
        filename = adb.create_log_file(MO_device_ID, MO_Filename)
        # MT_filename, MT_process = adb.create_log_file(MT_device_ID, MT_Filename)

        return str(filename)

    def get_device_details(self, MO, MT):

        # If there are no devices connected then we are stopping the execution here
        if self.adb_device_list() is not None:
            pass
        else:
            with allure.step("Failed : No devices are connected to system"):
                assert False, "Failed : No devices are connected to system"

        connected_device_List = self.fetch_connected_deviceList()
        fetch_phone_number = self.fetch_connected_phone_numbers(connected_device_List)

        set = False
        for phone in fetch_phone_number:
            if str(MO) in phone:

                MO_input_msg = f"Mobile originating device with device-ID : {str(phone).split("-")[0]} is connected with phone-number : {str(phone).split("-")[1]}"
                print(MO_input_msg)
                with allure.step(MO_input_msg):
                    pass
                MO_device_ID = str(phone).split("-")[0]
                MO_phone_number = str(phone).split("-")[1]
                fetch_phone_number = [l for l in fetch_phone_number if str(phone) not in l]
                set = False
                break
            else:
                set = True
        if set:
            MO_fail_msg = f"Mobile originating device with device-ID : {str(phone).split("-")[0]} is not connected to the system"
            print(MO_fail_msg)
            with allure.step(MO_fail_msg): pass

        if fetch_phone_number is not None:
            set = False
            for phone in fetch_phone_number:
                if str(MT) in phone:
                    MT_input_msg = f"Mobile terminating device with device-ID : {str(phone).split("-")[0]} is connected with phone-number : {str(phone).split("-")[1]}"
                    print(MT_input_msg)
                    with allure.step(MT_input_msg):
                        pass
                    MT_device_ID = str(phone).split("-")[0]
                    MT_phone_number = str(phone).split("-")[1]
                    fetch_phone_number = [l for l in fetch_phone_number if str(phone) not in l]
                    set = False
                    break
                else:
                    set = True
            if set:
                MT_fail_msg = f"Mobile Terminating device with device-ID : {str(phone).split("-")[0]} is not connected to the system"
                print(MT_fail_msg)
                with allure.step(MT_fail_msg): pass
        else:
            state = "Just one device is connected"
            MT_device_availability = None
            print(state)
            with allure.step(state):
                pass

        return MO_device_ID, MO_phone_number, MT_device_ID, MT_phone_number

    def get_three_devices_details(self, subscriber_A, subscriber_B, subscriber_C):

        if self.adb_device_list() is not None:
            pass
        else:
            with allure.step("Failed : No devices are connected to system"):
                assert False, "Failed : No devices are connected to system"

        connected_device_List = self.fetch_connected_deviceList()
        fetch_phone_number = self.fetch_connected_phone_numbers(connected_device_List)

        Flag_sub_A = False
        Flag_sub_B = False
        Flag_sub_C = False

        set = 0
        for phone in fetch_phone_number:
            if not Flag_sub_A:
                if str(subscriber_A) in phone:
                    subscriber_A_input_msg = f"Mobile device with device-ID : {str(phone).split('-')[0]} is connected with phone-number : {str(phone).split('-')[1]}"
                    print(subscriber_A_input_msg)
                    with allure.step(subscriber_A_input_msg):
                        pass
                    subscriber_A_device_ID = str(phone).split('-')[0]
                    print(subscriber_A_device_ID)
                    # lb.enable_airplane_mode(subscriber_A_device_ID)

                    subscriber_A_phone_number = str(phone).split('-')[1]
                    fetch_phone_number = [l for l in fetch_phone_number if str(phone) not in l]
                    set = set + 1
                    Flag_sub_A = True
                    continue

            if fetch_phone_number is not None:
                if not Flag_sub_B:
                    if str(subscriber_B) in phone:
                        subscriber_B_input_msg = f"Mobile device with device-ID : {str(phone).split('-')[0]} is connected with phone-number : {str(phone).split('-')[1]}"
                        print(subscriber_B_input_msg)
                        with allure.step(subscriber_B_input_msg):
                            pass
                        subscriber_B_device_ID = str(phone).split('-')[0]
                        print(subscriber_B_device_ID)
                        # lb.enable_airplane_mode(subscriber_B_device_ID)

                        subscriber_B_phone_number = str(phone).split('-')[1]
                        fetch_phone_number = [l for l in fetch_phone_number if str(phone) not in l]
                        set = set + 1
                        Flag_sub_B = True
                        continue

            if fetch_phone_number is not None:
                set = False
                if not Flag_sub_C:
                    if str(subscriber_C) in phone:
                        subscriber_C_input_msg = f"Mobile device with device-ID : {str(phone).split('-')[0]} is connected with phone-number : {str(phone).split('-')[1]}"
                        print(subscriber_C_input_msg)
                        with allure.step(subscriber_C_input_msg):
                            pass
                        subscriber_C_device_ID = str(phone).split('-')[0]
                        print(subscriber_C_device_ID)

                        subscriber_C_phone_number = str(phone).split('-')[1]
                        fetch_phone_number = [l for l in fetch_phone_number if str(phone) not in l]
                        set = set + 1
                        Flag_sub_C = True
                        continue

        return subscriber_A_device_ID, subscriber_A_phone_number, subscriber_B_device_ID, subscriber_B_phone_number, subscriber_C_device_ID, subscriber_C_phone_number

    def get_single_device_details(self, MO):

        if self.adb_device_list() is not None:
            pass
        else:
            with allure.step("Failed : No devices are connected to system"):
                assert False, "Failed : No devices are connected to system"

        connected_device_List = self.fetch_connected_deviceList()
        fetch_phone_number = self.fetch_connected_phone_numbers(connected_device_List)

        for phone in fetch_phone_number:
            if str(MO) in phone:
                MO_input_msg = f"Mobile originating device with device-ID : {str(phone).split('-')[0]} is connected with phone-number : {str(phone).split('-')[1]}"
                print(MO_input_msg)
                with allure.step(MO_input_msg):
                    pass
                MO_device_ID = str(phone).split('-')[0]
                MO_phone_number = str(phone).split('-')[1]
                break

        return MO_device_ID, MO_phone_number
