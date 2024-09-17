import time
import pyautogui
import ctypes
import os
import sys

import cv2
import numpy as np
import pyautogui
import time

def wait_for(locator_path, threshold=0.8, timeout=60):
    start_time = time.time()
    template = cv2.imread(locator_path, cv2.IMREAD_UNCHANGED)

    while time.time() - start_time < timeout:

        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)

        template = cv2.cvtColor(template, cv2.COLOR_BGR2BGRA)  # Convert template to BGRA
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2BGRA)  # Convert screenshot to BGRA

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val >= threshold:
            return True
        time.sleep(0.5)

    return False

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def start_application():
    if is_admin():
        os.startfile(u"C:\\Program Files (x86)\\Accuver\\XCAL-M\\XCAL-M.exe")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def main():
    # Call the function to start the application
    start_application()

    # The rest of your automation code from script_to_XCAL_app.py
    print("Staart")
    # locator_path = "C:\\Users\\TRDEVHOST020\\PycharmProjects\\pythonProject\\reference_images\\work\\IM_1.png"
    # wait_for(locator_path, threshold=0.5, timeout=35)
    time.sleep(32)
    print("End")

    # locator_path = "C:\\Users\\TRDEVHOST020\\PycharmProjects\\pythonProject\\reference_images\\work\\IM_6.png"
    # wait_for(locator_path, threshold=0.5, timeout=35)
    pyautogui.moveTo(525, 270)
    pyautogui.click(2039, 168)
    print("Click-1")
    time.sleep(0.8)
    pyautogui.click(338, 185)
    print("Click-2")
    time.sleep(0.8)
    pyautogui.moveTo(1200, 745)
    pyautogui.click(1200, 745)
    pyautogui.press('enter')
    print("Click-3")
    time.sleep(4)
    pyautogui.moveTo(1250, 716)
    pyautogui.click(1250, 716)
    print("Click-4")
    pyautogui.press('enter')

    

if __name__ == "__main__":
    main()