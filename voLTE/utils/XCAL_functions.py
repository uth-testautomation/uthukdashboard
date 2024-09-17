import subprocess, time


def click_onMic_button(MO_device_ID, seconds):

    try:
        no_of_times = int(seconds/5)
        for i in range(no_of_times):
            subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "730 1310 730 1310 5000"], shell=True)
    except Exception as e:
        print(f"Exception: {e}")

def emergency_swipe(MO_device_ID):

    try:
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "1300 2450 1300 2450 5000"],
                        shell=True)
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "361 1438 1158 1438 2000"],
                        shell=True)
    except Exception as e:
        print(f"Exception: {e}")


def send_PTX_message(MO_device_ID, MT_device_ID, message):

    try:
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "160 2431 160 2431 1000"],
                        shell=True)  # Message
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "650 2171 650 2171 1000"],
                        shell=True)  # Click center
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MT_device_ID), "shell", "input", "swipe", "160 2431 160 2431 1000"],
                        shell=True)

        time.sleep(3)
        # for i in range(3):
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "text", str(message)], shell=True)
        time.sleep(2)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "1294 2163 1294 2163 1000"],
                        shell=True)
        time.sleep(3)

    except Exception as e:
        print(f"Exception: {e}")


def private_call(MO_device_ID, MT_device_ID, phoneNumber):

    try:
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "147 1315 147 1315 1000"],
                        shell=True)  # Contact
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "336 637 336 637 1000"],
                        shell=True)  # Click search
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "text", str(phoneNumber)], shell=True)
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "407 842 407 842 500"],
                        shell=True)
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "730 1310 730 1310 1000"],
                        shell=True)

        time.sleep(1.2)

        subprocess.call(["adb", "-s", str(MT_device_ID), "shell", "input", "swipe", "1075 2308 1075 2308 1500"],
                        shell=True)

    except Exception as e:
        print(f"Exception: {e}")


def call_disconnect(MO_device_ID):

    try:
        time.sleep(2)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "703 2075 703 2075 1000"],
                        shell=True)
        time.sleep(15)

    except Exception as e:
        print(f"Exception: {e}")


def select_broadcastGroup(MO_device_ID):

    try:

        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "169 1534 169 1534 1000"], shell=True)
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "709 1145 709 1145 500"], shell=True)
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "730 1310 730 1310 1000"], shell=True)
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "1188 1550 1188 1550 1000"], shell=True)
        time.sleep(1)

    except Exception as e:
        print(f"Exception: {e}")

def reset_talkGroup(MO_device_ID):

    try:
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "169 1534 169 1534 1000"],
                        shell=True)
        time.sleep(3)
        subprocess.call(["adb", "-s", str(MO_device_ID), "shell", "input", "swipe", "654 890 654 890 500"],
                        shell=True)
    except Exception as e:
        print(f"Exception: {e}")