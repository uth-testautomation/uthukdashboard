import os
import shutil
import time
import subprocess

def clear(id):

    subprocess.call(["adb", "-s", str(id), "shell", "input", "keyevent", "3"], shell=True)
    time.sleep(1)
    subprocess.call(["adb", "-s", str(id), "shell", "input", "keyevent", "187"], shell=True)
    time.sleep(1.5)
    subprocess.call(["adb", "-s", str(id), "shell", "input", "tap", "520 1880"], shell=True)
    time.sleep(1)

    subprocess.call(["adb", "-s", str(id), "shell", "input", "keyevent", "3"], shell=True)

def clear_all_devices():
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
    for i in adb_device_list:
        clear(i)


def view_all_devices():
    adb_device_list = []
    adb_device_list.clear()
    print(os.getcwd())
    deviceFile = os.path.join(os.getcwd(), 'Devices.txt')
    with open(deviceFile, 'w'):
        pass
    abd_dev = subprocess.check_output("adb devices").splitlines()
    for line in abd_dev:
        device_line = str(line)
        if "device'" in device_line:
            device = device_line.split("'")
            d = device[1].rstrip("\\tdevice")
            adb_device_list.append(d)
            deviceDetails = subprocess.check_output("adb -s " + d + " shell \"service call iphonesubinfo 15\"")
            n = 0
            phoneNumber = ''
            for entry in str(deviceDetails).split("'"):
                entry = str(entry.encode('utf-8')).replace('\\x00', '').replace('.', '').replace('\'', '').replace('b',
                                                                                                                   '')
                n = n + 1
                if (n % 2 == 0):
                    phoneNumber = phoneNumber + entry
            ph = int(phoneNumber) % (10 ** 10)
            with open(deviceFile, 'a') as details:
                details.writelines(d + '-0' + str(ph) + '\n')
    shutil.copy2(deviceFile, os.path.join(os.getcwd(), "voLTE"))
    # print(adb_device_list)
    for i in adb_device_list:
        path = "./voLTE/scrcpy-win64-v2.3.1/scrcpy.exe" + " -s " + i
        subprocess.Popen(path)
        time.sleep(4)