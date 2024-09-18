import os.path
import sys
# sys.path.insert(0,os.path.abspath('C:\\UTH\\App\\voLTE\\utils\\dist'))
import time
# from dist.pyarmor_runtime_000000 import __pyarmor__
from utils import kill_adb
from behave import fixture
from voLTE.utils import XCAL_Logs, env_functionality
from voLTE.utils import move_device

@fixture
def before_all(context):
    try:
        kill_adb.kill_adb()
        XCAL_Logs.Stop_XCAL()
        time.sleep(5)
        XCAL_Logs.Launch_XCAL()
        time.sleep(2)
        kill_adb.kill_adb()
        env_functionality.view_all_devices()
        env_functionality.clear_all_devices()
        move_device.left(750)
        move_device.left(340)
        move_device.right()
    # sevendays_cron.sevendaysCron()
    except Exception as e:
        print(e)

@fixture
def after_all(context):
    kill_adb.kill_adb()
    XCAL_Logs.Stop_XCAL()