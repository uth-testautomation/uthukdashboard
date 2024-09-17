import os
import pyautogui
import cv2
import numpy as np
import time
import ctypes
import pygetwindow as gw

Check_for_launch_Icon = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Check_for_launch_Icon.png'))

First_PopUpWindow = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\First_PopUp_that_is_Information_popUp.png'))
First_PopUpWindow_OK_Button = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\First_PopUp_OK_Button.png'))
Second_PopUpWindow = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Second_PopUp_that_is_Logging_File_Type_popUp.png'))
Second_PopUpWindow_OK_Button = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Second_PopUp_OK_Button.png'))


License_Error = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\License_Error__.png'))
License_Error_Click_OK = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\License_Error_Click_OK.png'))
Error_Confirmation = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Error_Confirmation.png'))
Error_Confirmation_No = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Error_Confirmation_No.png'))

application = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Dashboard.png'))
Dashboard_second_reference = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Dashboard_second_reference.png'))
Dashboard_third_reference = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Dashboard_third_reference.png'))
Dashboard_fourth_reference = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Dashboard_fourth_reference.png'))

App_Maximize = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\App_Maximize.png'))

Device_not_connected_error = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Device_not_connected_error.png'))

Logging = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Logging.png'))
filename = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Send_Filename.png'))
save_button = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Save_Button.png'))
Stop_Logging = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Stop_Logging.png'))
Stop_Logging_Button = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Stop_Logging_Button.png'))
Exit = str(os.path.join(str(os.getcwd()).replace("utils",""), 'reference_images\\Exit.png'))

def click_on(locator_path):
    try:
        time.sleep(1.2)
        image_location = pyautogui.locateOnScreen(locator_path)
        # print(f"Image located at {image_location}.")
        time.sleep(1.2)
        if image_location is not None:

            image_x, image_y = pyautogui.center(image_location)

            time.sleep(0.2)
            pyautogui.click(image_x, image_y, duration=0.2)
            pyautogui.click(locator_path)
            pyautogui.press('left-mouse')
            time.sleep(0.1)
            print(f"Clicked at {image_x},{image_y}.")
            return True
        else:
            # print("Image not found on the screen.")
            os.system('cls')
            filename_without_extension = os.path.splitext(os.path.basename(locator_path))[0]
            print(f"{str(filename_without_extension)} not found on the screen. Waiting to load...")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


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


def wait_and_click(locator_path, threshold=0.8, timeout=60):
    start_time = time.time()
    template = cv2.imread(locator_path, cv2.IMREAD_UNCHANGED)

    while time.time() - start_time < timeout:

        screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)

        template = cv2.cvtColor(template, cv2.COLOR_BGR2BGRA)  # Convert template to BGRA
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2BGRA)  # Convert screenshot to BGRA

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val >= threshold:
            click_on(locator_path)
            return True
        time.sleep(0.5)

    return False


def launch_application(application_location_path):

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    try:
        if is_admin():
            os.startfile(application_location_path)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", "start_application.py", None, 1)
    except Exception as e:
        raise Exception(f"Unable to start {str(application_location_path)} due to: \n{str(e)}")


def start_application(application_location_path):
    # launch_application(application_location_path=u"C:\\Program Files (x86)\\Accuver\\XCAL-M\\XCAL-M.exe")
    launch_application(str(application_location_path))
    check_point = None
    time.sleep(1.2)
    pyautogui.hotkey('win', 'd')
    try:
        for i in range(30):
            try:
                response = wait_for(First_PopUpWindow, threshold=0.6, timeout=1)
                if response:
                    check_point = "Found"
            except:pass
            try:
                response = wait_for(License_Error, threshold=0.6, timeout=1)
                if response:
                    check_point = "Error"
            except:pass
            time.sleep(1)
            if check_point is not None:
                break
    except Exception as outer_exception:
        print("Outer Exception : ", outer_exception)  # Print the exception for better debugging

    try:
        if check_point == "Found":
            wait_and_click(First_PopUpWindow_OK_Button, threshold=0.5, timeout=3)
            wait_for(Second_PopUpWindow, threshold=0.6, timeout=30)
            time.sleep(1.2)
            try:
                wait_and_click(Second_PopUpWindow_OK_Button, threshold=0.5, timeout=3)
            except Exception as e:
                print(e)

            try:
                for i in range(60):
                    try:
                        dash_load_response = wait_for(application, threshold=0.5, timeout=1)
                        if dash_load_response:
                            break
                    except:
                        pass
                    try:
                        dash_load_response = wait_for(Dashboard_second_reference, threshold=0.5, timeout=1)
                        if dash_load_response:
                            break
                    except:
                        pass
                    try:
                        dash_load_response = wait_for(Dashboard_third_reference, threshold=0.5, timeout=1)
                        if dash_load_response:
                            break
                    except:
                        pass
                    try:
                        dash_load_response = wait_for(Dashboard_fourth_reference, threshold=0.5, timeout=1)
                        if dash_load_response:
                            break
                    except:
                        pass
            except:
                pass

            try:
                time.sleep(4)
                window = gw.getWindowsWithTitle(u"XCAL-M")[0]
                window.maximize()
            except:
                pass

            try:
                wait_and_click(App_Maximize, threshold=0.5, timeout=3)
            except Exception as e:
                print(e)

            try:
                Dev_is_not_connected = wait_for(Device_not_connected_error, threshold=0.5, timeout=5)
                if Dev_is_not_connected:
                    raise Exception
                else:
                    pass
            except Exception as e:
                raise Exception("Device is not connected")
        else:
            raise Exception

        return True
        # wait_and_click(Logging, threshold=0.6, timeout=3)
    except Exception as e:
        try:
            if Dev_is_not_connected:
                raise Exception(f"No device cooneted to X-CAL due to:\n{str(e)}")
            else:
                wait_and_click(License_Error_Click_OK, threshold=0.5, timeout=2)
                wait_for(Error_Confirmation, threshold=0.6, timeout=5)
                time.sleep(1.2)
                wait_and_click(Error_Confirmation_No, threshold=0.5, timeout=3)
                return False
        except:
            pass
        raise Exception(f"No License found. So, unable to start {str(application_location_path)} due to:\n{str(e)}")

def start_logging(logs_directory='"C:\\XCAL_Logs\\Trial"'):

    # if not os.path.exists(str(logs_directory).replace("\"", "").replace("\Trial", "")):
    #     # Create a new directory because it does not exist
    #     os.makedirs(str(logs_directory).replace("\"", "").replace("\Trial", ""))
    #     print(f"There is new directory is created and X-CAL logs stored here:\n{str(logs_directory)}")

    wait_and_click(Logging, threshold=0.6, timeout=10)
    # wait_and_click(filename, threshold=0.5, timeout=5)
    time.sleep(3)
    pyautogui.write(logs_directory)
    time.sleep(3)
    wait_and_click(save_button, threshold=0.6, timeout=4)
    return True

def stop_logging():

    wait_and_click(Stop_Logging_Button, threshold=0.5, timeout=5)
    time.sleep(3)
    pyautogui.press('enter')
    return True

if  __name__ == "__main__":
    start_application(application_location_path = u"C:\\Program Files (x86)\\Accuver\\XCAL-M\\XCAL-M.exe")
    start_logging()
    time.sleep(4)
    stop_logging()