import pyautogui
import time

def left(x_position):
    print(pyautogui.size())
    print("Width :", round((pyautogui.size().width)/2))
    print("Height :", pyautogui.size().height)

    x = round((pyautogui.size().width)/2)
    y = 58

    try:
        time.sleep(4)
        pyautogui.mouseDown(x,y, button="left")
        x=x + x_position
        pyautogui.moveTo(x,y, duration=0.2)
        pyautogui.mouseUp()
        time.sleep(0.3)
    except:
        pass

def right():
    print(pyautogui.size())
    print("Width :", round((pyautogui.size().width)/2))
    print("Height :", pyautogui.size().height)

    x = round((pyautogui.size().width)/2)
    y = 58

    try:
        time.sleep(2)
        pyautogui.mouseDown(x,y, button="left")
        x=x - 70
        pyautogui.moveTo(x,y, duration=0.2)
        pyautogui.mouseUp()
        time.sleep(0.3)
    except:
        pass

# time.sleep(4)
# left()

# while True:
#     x,y = pyautogui.position()
#     print(x,y)

    # 960,58