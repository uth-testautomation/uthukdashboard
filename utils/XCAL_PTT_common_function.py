import subprocess
import time

def Device_Awake(Device_ID):

    subprocess.check_output('adb -s ' + str(Device_ID) + ' shell input keyevent "KEYCODE_WAKEUP"')
    Wake = Device_Awake


def Hold(Device_ID,  input_type, coordinates, duration=1000):

    if input_type == 'api':
        subprocess.check_output('adb -s ' + str(
            Device_ID) + ' shell am broadcast -a com.mcx.intent.action.mobileapinotify -e "PTTNotifyData" "API:PTT_DOWN"')
        # time.sleep(int(CallLength[1] / 1000))
    elif input_type == 'coordinates':
        try:
            subprocess.check_output('adb -s ' + str(Device_ID) + ' shell input touchscreen swipe ' + str(coordinates) + str(duration) )
        except:
            try:
                times = (duration)/5
                for i in range(times):
                    subprocess.check_output(
                        'adb -s ' + str(Device_ID) + ' shell input touchscreen swipe 730 1310 730 1310 5000')
            except:
                subprocess.check_output('adb -s ' + str(Device_ID) + ' shell input keyevent --longpress KEYCODE_L')
    press = PressNHold = tap = Hold


def hold_mic_button(device_id, coord_api):
    if coord_api == "coord":
        for i in range(5):
            subprocess.call(["adb", "-s", str(device_id), "shell", "input", "swipe", "730 1310 730 1310 5000"], shell=True)
    elif coord_api == "api":
        subprocess.check_output('adb -s ' + str(device_id) + ' shell am broadcast -a com.mcx.intent.action.mobileapinotify -e "PTTNotifyData" "API:PTT_DOWN"')


def release_mic_button(device_id,coord_api):
    try:
        if coord_api == "coord":
            for i in range(5):
                subprocess.call(["adb", "-s", str(device_id), "shell", "input", "swipe", "730 1310 730 1310 5000"], shell=True)
        elif coord_api == "api":
            subprocess.check_output('adb -s ' + str(device_id) + ' shell am broadcast -a com.mcx.intent.action.mobileapinotify -e "PTTNotifyData" "API:PTT_UP"')
    except:
        print("Failed to release the mic button")



def send_ptx_msg_(mo_device_id, mt_device_id, coord_api, DevNumber):
    try:
        if coord_api == "coord":
            time.sleep(30)
            subprocess.call(["adb", "-s", str(mo_device_id), "shell", "input", "swipe", "160 2431 160 2431 1000"],
                            shell=True)  # Message
            time.sleep(3)
            subprocess.call(["adb", "-s", str(mo_device_id), "shell", "input", "swipe", "650 2171 650 2171 1000"],
                            shell=True)  # Click center
            time.sleep(3)
            subprocess.call(["adb", "-s", str(mt_device_id), "shell", "input", "swipe", "160 2431 160 2431 1000"],
                            shell=True)

            time.sleep(3)
            # for i in range(3):
            subprocess.call(["adb", "-s", str(mo_device_id), "shell", "input", "text", "PTX"], shell=True)
            time.sleep(2)
            subprocess.call(["adb", "-s", str(mo_device_id), "shell", "input", "swipe", "1294 2163 1294 2163 1000"],
                            shell=True)
            time.sleep(3)
        elif coord_api == "api":

            subprocess.check_output('adb -s ' + str(mo_device_id) + ' shell am broadcast -a com.mcx.intent.action.mobileapinotify -e "PTTNotifyData" "API:SEND_1-1_PTX='
                                    + str(DevNumber[1].mdn) + '"')
    except:
        print('Failed to send message')

# Move all devices to whichever channel is supplied as input
def AllDevsGroupSwitch(channelNum, DevNumber):
    try:
        for i in range(len(DevNumber)):
            print("Switching to Test-Group " + str(channelNum), str(DevNumber[i].user))
            subprocess.check_output('adb -s ' + str(DevNumber[
                                                        i].user) + ' shell am broadcast -a com.mcx.intent.action.mobileapinotify -e "PTTNotifyData" "API:GrpSwitch=' + str(
                channelNum) + '"')
    except:
        pass


def force_stop(Device_ID, packageName):

    try:
        subprocess.call(["adb", "-s", str(Device_ID), "shell", "am", "force-stop", str(packageName)], shell=True)
    except:
        print("There is no such package : " + str(packageName))


def start_app(Device_ID, packageName):

    try:
        subprocess.call(["adb", "-s", str(Device_ID), "shell", "am", "start", "-n", str(packageName)], shell=True)
    except:
        print("There is no such package : " + str(packageName))

    start_application = start_app

def search_contact(Device_ID, phoneNumber):

    try:
        subprocess.call(["adb", "-s", str(Device_ID), "shell", "input", "swipe", "147 1315 147 1315 1000"], shell=True) #Contact
        time.sleep(3)
        subprocess.call(["adb", "-s", str(Device_ID), "shell", "input", "swipe", "336 637 336 637 1000"], shell=True) #Click search
        time.sleep(3)
        subprocess.call(["adb", "-s", str(Device_ID), "shell", "input", "text", str(phoneNumber)], shell=True)
    except:
        pass
