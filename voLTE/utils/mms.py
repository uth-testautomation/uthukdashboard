import subprocess,time

MO_device_ID = "RFCR81KHXCY"
MT_phone_number = "07581045780"

time.sleep(4)
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