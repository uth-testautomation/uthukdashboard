import subprocess, time, datetime

import allure


def send_an_sms(MO_device_ID, MT_phone_number):
    timestamp = datetime.datetime.now().timestamp()
    formatted_string = datetime.datetime.fromtimestamp(timestamp).strftime("Date %d-%m-%Y Time %H:%M:%S")
    formatted_string = '"' + formatted_string + '"'
    # print("Formatted Timestamp:", formatted_string)

    try:
        # Send SMS
        subprocess.Popen(
            ["adb", "-s", MO_device_ID, "shell", "am", "start", "-a", "android.intent.action.SENDTO", "-d",
             "sms:" + str(MT_phone_number), "--es", "sms_body", str(formatted_string), "--ez", "exit_on_sent", "true"],
            shell=True)
        time.sleep(4)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(15)
    except Exception as e:
        print(f"Exception: {e}")


def send_an_mms(MO_device_ID, MT_phone_number):

    try:
        # Send MMS
        subprocess.Popen(
            ["adb", "-s", MO_device_ID, "shell", "am", "start", "-a", "android.intent.action.SEND", "-d",
             "sms:" + MT_phone_number, "--ez", "exit_on_sent", "true"],
            shell=True)
        time.sleep(4)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "21"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "21"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "21"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "20"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "19"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(1.2)
        subprocess.Popen(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(15)
    except Exception as e:
        print(f"Exception: {e}")


def send_a_picture_sms(MO_device_ID, MT_phone_number):
    try:

        device_screenshot_path = "/sdcard/screenshot.jpg"

        subprocess.call(["adb", "-s", MO_device_ID, "shell", "screencap", "-p", device_screenshot_path], shell=True)
        time.sleep(1)

        # Send picture SMS
        subprocess.Popen(
            ["adb", "-s", MO_device_ID, "shell", "am", "start", "-a", "android.intent.action.SENDTO", "-d",
             "sms:" + str(MT_phone_number), "--ez", "exit_on_sent", "true"],
            shell=True)

        time.sleep(4)
        subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        time.sleep(0.1)
        subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "19"], shell=True)
        time.sleep(0.1)
        subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "19"], shell=True)
        time.sleep(0.1)
        for x in range(3):
            subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "21"], shell=True)
            time.sleep(0.1)
        subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(0.1)
        subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "20"], shell=True)
        time.sleep(0.1)
        subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(0.1)
        subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "19"], shell=True)
        time.sleep(0.1)
        for x in range(5):
            subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
            time.sleep(0.1)
        subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(10)

        subprocess.call(["adb", "-s", MO_device_ID, "shell", "rm", device_screenshot_path], shell=True)

    except Exception as e:
        print(f"Exception: {e}")

def capture_photo_and_send_as_sms(MO_device_ID, MT_phone_number):
    try:
        # Send picture SMS
        subprocess.Popen(
            ["adb", "-s", MO_device_ID, "shell", "am", "start", "-a", "android.intent.action.SENDTO", "-d",
             "sms:" + str(MT_phone_number), "--ez", "exit_on_sent", "true"],
            shell=True)

        time.sleep(4)
        process_call(MO_device_ID, 61)
        process_call(MO_device_ID, 19)
        process_call(MO_device_ID, 19)
        outs = subprocess.check_output(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        with allure.step(outs):pass
        time.sleep(0.1)
        # process_call(MO_device_ID, 21)
        process_call(MO_device_ID, 21)
        process_call(MO_device_ID, 66)
        process_call(MO_device_ID, 20)
        process_call(MO_device_ID, 66)
        process_call(MO_device_ID, 61)
        process_call(MO_device_ID, 66)
        process_call(MO_device_ID, 61)
        process_call(MO_device_ID, 61)
        process_call(MO_device_ID, 66)
        process_call(MO_device_ID, 61)
        process_call(MO_device_ID, 61)
        process_call(MO_device_ID, 66)

        # subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        # time.sleep(0.1)
        # subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "19"], shell=True)
        # time.sleep(0.1)
        # subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "19"], shell=True)
        # time.sleep(0.1)
        # for x in range(2):
        #     subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "21"], shell=True)
        #     time.sleep(0.1)
        # subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        # time.sleep(0.1)
        # subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "20"], shell=True)
        # time.sleep(0.1)
        # subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        # time.sleep(0.1)
        # subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "19"], shell=True)
        # time.sleep(0.1)
        # for x in range(5):
        #     subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "61"], shell=True)
        #     time.sleep(0.1)
        # subprocess.call(["adb", "-s", MO_device_ID, "shell", "input", "keyevent", "66"], shell=True)
        time.sleep(10)


    except Exception as e:
        print(f"Exception: {e}")

def click_homeButton(MO_device_ID):

    try:
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "keyevent", "3"], shell=True)
    except Exception as e:
        print(f"Exception: {e}")

def start_application(MO_device_ID, MT_device_ID, app_name, package_name):

    try:
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "am", "force-stop", app_name], shell=True)
        time.sleep(5)
        subprocess.call(["adb", "-s", str(MT_device_ID), "shell", "am", "force-stop", app_name], shell=True)

        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "am", "start", "-n" , package_name], shell=True)
        time.sleep(5)
        subprocess.call(["adb", "-s", str(MT_device_ID), "shell", "am", "start", "-n", package_name], shell=True)
    except Exception as e:
        print(f"Exception: {e}")

def process_call(device_id, keyevent):
    try:
        subprocess.call(["adb", "-s", str(device_id), "shell", "input", "keyevent", str(keyevent)], shell=True)
        time.sleep(0.1)
    except Exception as e:
        print(f"Exception: {e}")