import subprocess, time


def make_a_call(MO_device_ID, MT_phone_number):

    try:
        # Initiate call
        subprocess.call(
            ["adb", "-s", MO_device_ID, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
             "tel:" + MT_phone_number],
            shell=True)
    except Exception as e:
        print(f"Exception: {e}")

    call = make_a_call


def call_123(MO_device_ID):

    try:
        # Initiate a 123 call
        subprocess.call(
            ["adb", "-s", MO_device_ID, "shell", "am", "start", "-a", "android.intent.action.CALL", "-d",
             "tel:123"], shell=True)
    except Exception as e:
        print(f"Exception: {e}")


def call_recieve(MT_device_ID):

    try:
        subprocess.call(["adb", "-s", MT_device_ID, "shell", "input", "keyevent", "5"], shell=True)
    except Exception as e:
        print(f"Exception: {e}")

    receieve_call = call_recieve


def end_call(device_ID):

    try:
        subprocess.call(["adb", "-s", device_ID, "shell", "input", "keyevent", "KEYCODE_ENDCALL"], shell=True)
    except Exception as e:
        print(f"Exception: {e}")

    call_end = disconnect = call_disconnect = call_terminate = End_call = end_call
