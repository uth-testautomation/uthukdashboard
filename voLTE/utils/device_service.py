import subprocess, time, datetime


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
