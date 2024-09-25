import logging
import re
from glob import glob

import allure
from behave import *
import subprocess
import os
import time
import shutil

from utils import XCAL_Logs, kill_adb, call_func, common_call
# from utils import kill
from utils.device import function
from utils.local_cache import Caching
from utils import device_service as dev_funct
from utils import adb_log_function as adb

current_working_dir = os.getcwd()
xcal_log_path = os.path.join(current_working_dir, "XCAL_Logs")
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
xcal_log_directory = os.path.join(desktop_path, "XCAL_Logs")

caching = Caching()
device = function()

def get_XCAL_Filename():
    try:

        filename = None
        list_of_files = os.listdir(xcal_log_directory)

        for file in list_of_files:
            filenam = os.path.join(xcal_log_directory, file)
            with open(filenam, 'r') as files:
                lines = files.readlines()
            for line in lines:
                if str(caching.get_mophonenumber()) in line:
                    deviceName = extracting_filename(filenam)
                    caching.set_modevicename(deviceName)
                if str(caching.get_mtphonenumber()) in line:
                    deviceName = extracting_filename(filenam)
                    caching.set_mtdevicename(deviceName)
                if str(caching.get_mfphonenumber()) in line:
                    deviceName = extracting_filename(filenam)
                    caching.set_mfdevicename(deviceName)

        filename = None
        numb = {
            caching.get_mophonenumber(): caching.get_modeviceName(),
            caching.get_mtphonenumber(): caching.get_mtdeviceName(),
            caching.get_mfphonenumber(): caching.get_mfdeviceName()
        }
        list_of_files = os.listdir(xcal_log_directory)

        for file in list_of_files:
            # with allure.step(file):
            #     pass
            # with allure.step(numb[caching.get_mophonenumber()]):
            #     pass
            if (file.startswith(caching.get_testcase())) and (numb[caching.get_mophonenumber()] in file) and (
            file.endswith(".aof")):
                filename = os.path.join(xcal_log_directory, file)

        return filename

    except Exception as e:
        print(e)

def extracting_filename(path: str):
    # directory, filename = os.path.split(path)
    match = re.search(r'M\d+', path)

    if match:
        return match.group(0)
    else:
        return None


@given(u'the user wants to register the device "{MO}" on "{networkType}"')
def registration_of_device(context, MO: str, networkType: str):
    caching.set_noOfDevice('1')
    moDeviceID, moPhonenumber = device.get_single_device_details(MO)
    caching.set_modeviceid(moDeviceID)
    moPhonenumber = int(moPhonenumber) % (10 ** 10)
    # moPhonenumber = "+44" + str(moPhonenumber)
    caching.set_mophonenumber(moPhonenumber)
    caching.set_networktype(networkType)

@given(u'the user wants to execute "{testcase}" test case')
def user_execution_test_case(context, testcase: str):
    caching.set_testcase(testcase)
    list_of_files = os.listdir(os.getcwd())
    for file in list_of_files:
        # with allure.step(str(file)): pass
        if file.startswith(caching.get_testcase()) and file.endswith('.txt'):
            os.remove(file)

@then(u'the user disconnects from the network')
def disconnect_from_network(context):
    try:
        # Enabling the Airplane Mode
        subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "cmd", "connectivity", "airplane-mode", "enable"],
                        shell=True)
        time.sleep(20)

    except Exception as e:
        print(f"Exception: {e}")

@then(u'starts capturing XCAL and adb logs')
def start_xcalandadb_logging(context):
    try:
        context.MO_filename = device.start_XCAL_N_adb(caching.get_modeviceid(), caching.get_testcase())
        caching.set_adbfilename(str(context.MO_filename))
        if (str(caching.get_noOfDevice()) == '2' or str(caching.get_noOfDevice()) == '3'):
            context.MT_filename = device.start_XCAL_N_adb(caching.get_mtdeviceid(), caching.get_testcase())
            caching.set_mtadbfilename(str(context.MT_filename))
            if (str(caching.get_noOfDevice()) == '3'):
                context.MF_filename = device.start_XCAL_N_adb(caching.get_mfdeviceid(), caching.get_testcase())
                caching.set_mfadbfilename(str(context.MF_filename))
        time.sleep(10)
    except Exception as e:
        print(f'Exception: {e}')

@then(u'connects to the network')
def network_connection(context):
    try:
        # Disable the Airplane Mode
        subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "cmd", "connectivity", "airplane-mode", "disable"],
                        shell=True)
        time.sleep(10)

    except Exception as e:
        print(f"Exception: {e}")

@then(u'then stops the XCAL log')
def stops_xcal_logs(context):
    try:
        xcalfilename = XCAL_Logs.Stop_Logging(xcal_log_directory, caching.get_testcase())
        caching.set_xcalfilename(xcalfilename)

    except Exception as e:
        print(e)

@then(u'then stop the adb logs')
def stop_adp_logs(context):
    try:
        adb.stop_adb_log(caching.get_modeviceid(), caching.get_adbfilename())
        if (str(caching.get_noOfDevice()) == '2' or str(caching.get_noOfDevice()) == '3'):
            adb.stop_adb_log(caching.get_mtdeviceid(), caching.get_mtadbfilename())
            if (str(caching.get_noOfDevice()) == '3'):
                adb.stop_adb_log(caching.get_mfdeviceid(), caching.get_mfadbfilename())
        time.sleep(2)
        logging.info(caching.get_adbfilename())
        currentadplog = os.path.join(str(os.getcwd()), caching.get_adbfilename())
        shutil.copy(currentadplog, caching.get_cwdWorkingDir())
    except:
        pass

@then(u'the user makes a call from "{MO}" to "{MT}"')
def setting_up_calling(context, MO: str, MT: str):
    caching.set_noOfDevice('2')
    moDeviceID, moPhonenumber, mtDeviceID, mtPhonenumber = device.get_device_details(MO, MT)
    caching.set_modeviceid(moDeviceID)
    moPhonenumber = int(moPhonenumber) % (10 ** 10)
    # moPhonenumber = "+44" + str(moPhonenumber)
    caching.set_mophonenumber(moPhonenumber)
    # caching.set_networktype(NetworkType)
    caching.set_mtdeviceid(mtDeviceID)
    mtPhonenumber = int(mtPhonenumber) % (10 ** 10)
    # mtPhonenumber = "+44" + str(mtPhonenumber)
    caching.set_mtphonenumber(mtPhonenumber)

@then(u'the user initiates the call from "{MO}" to {MT}')
def call_initiation(context, MO: str, MT: str):
    try:
        common_call.initiate_call(caching.get_modeviceid(), MT)
        time.sleep(6.5)
        common_call.establish_call(caching.get_mtdeviceid())
    except Exception as e:
        print(f"Exception: {e}")

@then(u'the user initiates the call up from "{MO}" to "{MT}"')
def call_forward_initiation(context, MO: str, MT: str):
    try:
        if (MO == 'subscriber_A'):
            device_id = caching.get_modeviceid()
        elif (MO == 'subscriber_B'):
            device_id = caching.get_mtdeviceid()
        elif (MO == 'subscriber_C'):
            device_id = caching.get_mfdeviceid()
        common_call.initiate_call(device_id, MT)
        time.sleep(2)
    except Exception as e:
        print(f"Exception: {e}")

@then(u'the user initiates the third party call from "{MO}" to {MT}')
def call_initiation(context, MO: str, MT: str):
    try:
        common_call.initiate_call(caching.get_modeviceid(), MT)
        time.sleep(6.5)
        common_call.establish_call(caching.get_mfdeviceid())
    except Exception as e:
        print(f"Exception: {e}")

@then(u'user terminates the call from "{MO}" after "{call_duration}" seconds')
def terminating_the_call(context, MO: str, call_duration):
     # End call
    time.sleep(int(call_duration))
    with allure.step("device name: " + str(MO)): pass
    if (MO == 'subscriber_A'):
        common_call.disconnect_call(caching.get_modeviceid())
    elif (MO == 'subscriber_B'):
        common_call.disconnect_call(caching.get_mtdeviceid())
    elif (MO == 'subscriber_C'):
        common_call.disconnect_call(caching.get_mfdeviceid())
    time.sleep(2)

@then(u'the user wants to sends a sms from "{MO}" to "{MT}"')
def setting_up_sms(context, MO: str, MT: str):
    caching.set_noOfDevice('2')
    time.sleep(10)
    moDeviceID, moPhonenumber, mtDeviceID, mtPhonenumber = device.get_device_details(MO, MT)
    caching.set_modeviceid(moDeviceID)
    moPhonenumber = int(moPhonenumber) % (10 ** 10)
    # moPhonenumber = "+44" + str(moPhonenumber)
    caching.set_mophonenumber(moPhonenumber)
    caching.set_mtdeviceid(mtDeviceID)
    mtPhonenumber = int(mtPhonenumber) % (10 ** 10)
    # mtPhonenumber = "+44" + str(mtPhonenumber)
    caching.set_mtphonenumber(mtPhonenumber)

@then(u'the user sends the SMS from "{MO}" to "{MT}"')
def sending_the_sms(context, MO: str, MT: str):
    caching.set_noOfDevice('2')
    try:
        dev_funct.click_homeButton(caching.get_modeviceid())
        dev_funct.click_homeButton(caching.get_mtdeviceid())
        time.sleep(0.3)
        dev_funct.send_an_sms(caching.get_modeviceid(), caching.get_mtphonenumber())
        time.sleep(2)
        dev_funct.click_homeButton(caching.get_modeviceid())
        dev_funct.click_homeButton(caching.get_mtdeviceid())

    except Exception as e:
        print(f"Exception: {e}")

@given(u'the user connects the devices "{subA}", "{subB}" and "{subC}" on the network')
def connecting_three_devices(context, subA: str, subB: str, subC: str):
    caching.set_noOfDevice('3')
    moDeviceID, moPhonenumber, mtDeviceID, mtPhonenumber, mfDeviceID, mfPhonenumber = device.get_three_devices_details(subA, subB, subC)
    caching.set_modeviceid(moDeviceID)
    moPhonenumber = int(moPhonenumber) % (10 ** 10)
    # moPhonenumber = "+44" + str(moPhonenumber)
    caching.set_mophonenumber(moPhonenumber)
    caching.set_mtdeviceid(mtDeviceID)
    mtPhonenumber = int(mtPhonenumber) % (10 ** 10)
    # mtPhonenumber = "+44" + str(mtPhonenumber)
    caching.set_mtphonenumber(mtPhonenumber)
    caching.set_mfdeviceid(mfDeviceID)
    mfPhonenumber = int(mfPhonenumber) % (10 ** 10)
    # mfPhonenumber = "+44" + str(mfPhonenumber)
    caching.set_mfphonenumber(mfPhonenumber)

@then(u'the user connects the devices "{subA}" and "{subB}" to the network')
def connecting_two_devices(context, subA, subB):
    caching.set_noOfDevice('2')
    moDeviceID, moPhonenumber, mtDeviceID, mtPhonenumber = (device.get_device_details(subA, subB))
    caching.set_modeviceid(moDeviceID)
    moPhonenumber = int(moPhonenumber) % (10 ** 10)
    # moPhonenumber = "+44" + str(moPhonenumber)
    caching.set_mophonenumber(moPhonenumber)
    caching.set_mtdeviceid(mtDeviceID)
    mtPhonenumber = int(mtPhonenumber) % (10 ** 10)
    # mtPhonenumber = "+44" + str(mtPhonenumber)
    caching.set_mtphonenumber(mtPhonenumber)

@then(u'the user "{status}" call forwarding to "{callForwardTo}" by sending "{ussd_code}" on "{MT}"')
def setting_the_ussd(context,status:str,callForwardTo, ussd_code: int, MT: str):
    if (MT == 'subscriber_A'):
        device_id = caching.get_modeviceid()
    elif (MT == 'subscriber_B'):
        device_id = caching.get_mtdeviceid()
    elif (MT == 'subscriber_C'):
        device_id = caching.get_mfdeviceid()
    if (status == 'enables'):
        try:
            time.sleep(1.2)
            dial_code = "*" + ussd_code + "*" + callForwardTo + "%23"
            common_call.send_USSD_code(device_id, dial_code)
            time.sleep(6)

        except Exception as e:
            print(f'Exception: {e}')
    else :
        try:
            dial_code = "%23" + ussd_code + "%23"
            common_call.send_USSD_code(device_id, dial_code)
            time.sleep(6)
        except Exception as e:
            print(f'Exception: {e}')

@then(u'the call gets forwarded to the "{subC}"')
def call_forwading(context, subC: int):
    try:
        time.sleep(16)
        if (subC == 'VoiceMail'):
            time.sleep(2)
            wavFile = os.path.join(os.getcwd() + "/voLTE/Test_Audio.wav")
            os.system(f'start /min "MyApp" ' + wavFile)
            # os.system(f'start /min "MyApp" "C:\\Users\\admin\\Desktop\\pythonProject\\pythonProject\\Test_Audio.wav"')
    except Exception as e:
        print(f'Exception: {e}')

@then(u'"{subC}" answers the call and the call is established between "{subA}" and "{subC}"')
def answering_the_call(context, subC, subA):
    try:
        time.sleep(3)
        common_call.establish_call(caching.get_mfdeviceid())
        time.sleep(10)
    except Exception as e:
        print(f'Exception: {e}')

@then(u'"{subA}" holds the call for "{callDuration}" and then resumes it')
def call_resume_and_hold(context, subA, callDuration):
    try:
        common_call.hold_and_resume(caching.get_modeviceid(), callDuration)
        time.sleep(int(callDuration))
    except Exception as e:
        print(f'Exception: {e}')

@then(u'then the user "{status}" "{callFormat}" on "{MT}" by dialing the "{ussd_code}"')
def setting_the_ussd_code(context, status, callFormat, MT, ussd_code):
    try:
        if (MT == 'subscriber_A'):
            device_id = caching.get_modeviceid()
        elif (MT == 'subscriber_B'):
            device_id = caching.get_mtdeviceid()
        elif (MT == 'subscriber_C'):
            device_id = caching.get_mfdeviceid()
        if (status == 'enables'):
            dial_code = "%23" + '61' + "%23"
            common_call.send_USSD_code(device_id, dial_code)
            dial_code = "*" + ussd_code + "%23"
            common_call.send_USSD_code(device_id, dial_code)
        else:
            time.sleep(5)
            dial_code = "%23" + ussd_code + "%23"
            common_call.send_USSD_code(device_id, dial_code)
    except Exception as e:
            print(f'Exception: {e}')

@then(u'the call is not established and gets disconnected after announcement')
def call_disconnect_after_announcement(context):
    try:
        time.sleep(3)
    except Exception as e:
        print(f'Exception: {e}')

@then(u'the user "{status}" WiFi calling on "{subscriber}"')
def wifi_calling_status(context, status, subscriber):
    try:
        if (subscriber == 'subscriber_A'):
            wifi_calling_command = f"adb -s " + caching.get_modeviceid() + " shell \"svc wifi "+ status + "\""
            process = subprocess.Popen(wifi_calling_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            common_call.changeStatusofWifiCalling(caching.get_modeviceid())
        elif (subscriber == 'subscriber_B'):
            wifi_calling_command = f"adb -s " + caching.get_mtdeviceid() + " shell \"svc wifi "+ status + "\""
            process = subprocess.Popen(wifi_calling_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            common_call.changeStatusofWifiCalling(caching.get_mtdeviceid())
        elif (subscriber == 'subscriber_C'):
            wifi_calling_command = f"adb -s " + caching.get_mfdeviceid() + " shell \"svc wifi "+ status + "\""
            process = subprocess.Popen(wifi_calling_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            common_call.changeStatusofWifiCalling(caching.get_mfdeviceid())
    except Exception as e:
        print(e)

@then(u'the user adds the other number to the call')
def adding_the_other_device(context):
    time.sleep(10)
    # subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    # subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    # subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    # subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    # subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    # subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "66"], shell=True)
    time.sleep(0.2)

@then(u'the user merges the call')
def merge_the_call(context):
    subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    time.sleep(0.2)
    subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    time.sleep(0.2)
    subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    time.sleep(0.2)
    subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "61"], shell=True)
    time.sleep(0.2)
    subprocess.call(["adb", "-s", caching.get_modeviceid(), "shell", "input", "keyevent", "66"], shell=True)
    time.sleep(0.2)

@then(u'the user sends an SMS containing a picture')
def sending_sms_containing_picture(context):
    try:
        dev_funct.click_homeButton(caching.get_modeviceid())
        dev_funct.click_homeButton(caching.get_mtdeviceid())
        time.sleep(0.3)
        dev_funct.send_a_picture_sms(caching.get_modeviceid(), caching.get_mtphonenumber())
        time.sleep(2)
        dev_funct.click_homeButton(caching.get_modeviceid())
        dev_funct.click_homeButton(caching.get_mtdeviceid())
    except Exception as e:
        with allure.step('Failed to send the sms containing photo'):
            assert False, "Failed to send the sms containing photo"

@then(u'the user sends an SMS attaching a photo from the camera')
def sending_sms_after_taking_photo(context):
    try:
        dev_funct.click_homeButton(caching.get_modeviceid())
        dev_funct.click_homeButton(caching.get_mtdeviceid())
        time.sleep(0.3)
        dev_funct.capture_photo_and_send_as_sms(caching.get_modeviceid(), caching.get_mtphonenumber())
        time.sleep(2)
        dev_funct.click_homeButton(caching.get_modeviceid())
        dev_funct.click_homeButton(caching.get_mtdeviceid())
    except Exception as e:
        with allure.step('Failed to send the sms containing photo'):
            assert False, "Failed to send the sms containing photo"

def adblogfilename(device: str):
    try:
        if (device == 'subA'):
            adbfile = caching.get_adbfilename()
        elif (device == 'subB'):
            adbfile = caching.get_mtadbfilename()
        elif (device == 'subC'):
            adbfile = caching.get_mfadbfilename()

        list_of_files = os.listdir(os.getcwd())
        # with allure.step(".     =====> Enter  <==========" + list_of_files): pass


        # with allure.step(str(list_of_files)): pass

        for file in list_of_files:
            # with allure.step(str(file)): pass
            if file.startswith(adbfile):
                filename = os.path.join(os.getcwd(), file)

        return filename
    except Exception as e:
        print(e)

def xcallogfilename():
    try:
        list_of_files = os.listdir(xcal_log_directory)

        for file in list_of_files:
            # with allure.step(str(file)): pass
            if file.startswith(caching.get_testcase()):
                xcalfilename = os.path.join(xcal_log_directory, file)

        Subscriber_A = caching.get_mophonenumber()
        filename = str(get_XCAL_Filename(Subscriber_A))

        return filename

    except Exception as e:
        print(e)