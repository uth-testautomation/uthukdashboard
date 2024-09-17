import subprocess
import time

import allure


def enable_airplane_mode(ue_device_id):
    try:
        time.sleep(4)

        subprocess.call(["adb", "-s", ue_device_id, "shell", "input", "keyevent", "4"], shell=True)
        # Enable the Airplane Mode
        if (subprocess.call(["adb", "-s", ue_device_id, "shell", "settings", "get", "global", "airplane_mode_on"],
                            shell=True)) == 1:
            pass
        else:
            subprocess.call(["adb", "-s", ue_device_id, "shell", "cmd", "connectivity", "airplane-mode", "enable"],
                            shell=True)

        time.sleep(4)

    except Exception as e:
        print(f"Exception: {e}")


def disable_airplane_mode(ue_device_id):
    try:
        time.sleep(4)

        # Disable the Airplane Mode

        subprocess.call(["adb", "-s", ue_device_id, "shell", "cmd", "connectivity", "airplane-mode", "disable"],
                        shell=True)

        time.sleep(4)

    except Exception as e:
        print(f"Exception: {e}")


def initiate_call(mo_device_id, phone_number):
    try:
        time.sleep(4)

        # Initiate the call
        subprocess.call(
            ["adb", "-s", mo_device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
             "tel:" + phone_number],
            shell=True)

        time.sleep(4)

    except Exception as e:
        print(f"Exception: {e}")


def establish_call(mt_device_id):
    try:
        # Answer the call
        with allure.step("MT device ID: " + mt_device_id):
            pass
        subprocess.call(["adb", "-s", mt_device_id, "shell", "input", "keyevent", "5"], shell=True)

    except Exception as e:
        print(f"Exception: {e}")


def disconnect_call(device_id):
    try:
        # Terminate the call

        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "KEYCODE_ENDCALL"], shell=True)

    except Exception as e:
        print(f"Exception: {e}")


#
# device_id = "pzai454lguqkbapb"
# CFNA = "*67*"
# mobile_number = "07788422741"
# ussd_code = CFNA + mobile_number + chr(35)
#
# print(ussd_code)

def call_forwarding(device_id, ussd_code):
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + ussd_code],
                    shell=True)

    time.sleep(5)

    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)


def CFNA_enable(device_id, fwd_num):
    CFNA_perfix = "*61*"

    ussd_code = CFNA_perfix + fwd_num
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + ussd_code + '%23'],
                    shell=True)

    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)

def send_USSD_code(device_id, USSD_code):

    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + USSD_code],
                    shell=True)

    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)

def CFNA_disable(device_id):
    CFNA_disable_ussd = "61"
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + '%23' + CFNA_disable_ussd + '%23'],
                    shell=True)
    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)


def CFB_enable(device_id, fwd_num):
    CFB_enable_ussd = "*67*"

    ussd_code = CFB_enable_ussd + fwd_num
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + ussd_code + '%23'],
                    shell=True)

    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)


def CFB_disable(device_id):
    CFB_disable_ussd = "67"
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + '%23' + CFB_disable_ussd + '%23'],
                    shell=True)
    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)


def CFU_enable(device_id, fwd_num):
    CFU_enable_ussd = "*21*"

    ussd_code = CFU_enable_ussd + fwd_num
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + ussd_code + '%23'],
                    shell=True)

    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)


def CFU_disable(device_id):
    CFU_disable_ussd = "21"
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + '%23' + CFU_disable_ussd + '%23'],
                    shell=True)
    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)


def call_waiting_enable(device_id, ussd_code):
    call_waiting_ussd = "*" + ussd_code
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" + call_waiting_ussd + '%23'],
                    shell=True)
    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)


def call_waiting_disable(device_id):
    ussd_code = "43"
    subprocess.call(["adb", "-s", device_id, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
                     "tel:" '%23' + ussd_code + '%23'],
                    shell=True)
    time.sleep(5)
    subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "4"], shell=True)


def send_sms(device_id, phone_number):
    try:

        subprocess.call(["adb", "-s", str(device_id), "shell", "input", "keyevent", "3"], shell=True)
        time.sleep(0.3)

        subprocess.Popen(
            ["adb", "-s", str(device_id), "shell", "am", "start", "-a", "android.intent.action.SENDTO", "-d",
             "sms:" + phone_number, "--es", "sms_body", "'Test'", "--ez", "exit_on_sent", "true"],
            shell=True)
        time.sleep(4)

        # Press Tab
        subprocess.Popen(["adb", "-s", str(device_id), "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        # Press Tab
        subprocess.Popen(["adb", "-s", str(device_id), "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        # Press Enter
        subprocess.Popen(["adb", "-s", str(device_id), "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(1.2)

    except Exception as e:
        print(f"Exception: {e}")


# import subprocess, time
#
#
# def make_a_call(MO_device_ID, MT_phone_number):
#
#     try:
#         # Initiate call
#         subprocess.call(
#             ["adb", "-s", MO_device_ID, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
#              "tel:" + MT_phone_number],
#             shell=True)
#     except Exception as e:
#         print(f"Exception: {e}")
#
#     call = make_a_call
#
#
# def call_123(MO_device_ID):
#
#     try:
#         # Initiate a 123 call
#         subprocess.call(
#             ["adb", "-s", MO_device_ID, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
#              "tel:123"], shell=True)
#     except Exception as e:
#         print(f"Exception: {e}")
#
#
# def call_recieve(MT_device_ID):
#
#     try:
#         subprocess.call(["adb", "-s", MT_device_ID, "shell", "input", "keyevent", "5"], shell=True)
#     except Exception as e:
#         print(f"Exception: {e}")
#
#     receieve_call = call_recieve
#
#
# def end_call(device_ID):
#
#     try:
#         subprocess.call(["adb", "-s", device_ID, "shell", "input", "keyevent", "KEYCODE_ENDCALL"], shell=True)
#     except Exception as e:
#         print(f"Exception: {e}")
#
#     call_end = disconnect = call_disconnect = call_terminate = End_call = end_call

def hold_and_resume(device_id, duration):
    try:
        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1)
        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1)
        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1)
        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1)
        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1)
        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1)

        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(10)
        subprocess.call(["adb", "-s", device_id, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(1)
    except Exception as e:
        print(f"Exception: {e}")

