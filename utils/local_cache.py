import datetime
import os
import json

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
xcal_log_directory = os.path.join(desktop_path, "XCAL_Logs")
desktopDirectory = xcal_log_directory

class Caching:

    def __init__(self):
        current_working_dir = os.getcwd()
        xcal_log_path = os.path.join(current_working_dir, "XCAL_Logs")
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        xcal_log_directory = os.path.join(desktop_path, "XCAL_Logs")
        current_time = datetime.datetime.now()
        time_stamp = current_time.timestamp()
        date_time = datetime.datetime.fromtimestamp(time_stamp)
        str_date_time = "Log_Date_" + date_time.strftime("%d_%m_%Y_Time_%H_%M_%S")
        self._modeviceid = "modeviceid"
        self._mophonenumber = 0
        self._mtdeviceid = "mtdeviceid"
        self._mtphonenumber = 0
        self._mfdeviceid = "mfdeviceid"
        self._mfphonenumber = 0
        self._testcase = "testcasename"
        self._cwdWorkingDir = xcal_log_path
        self._desktopDirectory = xcal_log_directory
        self._currentTime = str_date_time
        self._networkType = "4G"
        self._xcalfilename = "xcal_log_file"
        self._adbfilename = "adb_log_file"
        self._adbprocessid = 0
        self._mtadbfilename = "mtadb_log_file"
        self._mtadbprocessid = 0
        self._mfadbfilename = "mfadb_log_file"
        self._mfadbprocessid = 0
        self._deviceM1 = '07581045780'
        self._deviceM2 = '07944532088'
        self._deviceM3 = '07944531930'
        self._numberOfDevice = 1
        self._terminatingNumber2 = "terminalNumber"
        self._terminatingNumber3 = "terminalNumber"
        self._terminatingNumber4 = "terminalNumber"

        #configFileLocation = os.path.join(os.getcwd(), "config", "Config.json")
        #with open(configFileLocation, 'r') as configFile:
        #    configData = json.load(configFile)

        #self._callingNumber = configData['originNumber']
        #terminating_numbers = configData['terminationNumbers']
        #for index, terminating_number in enumerate(terminating_numbers):
        #    self._terminatingNumber2 = terminating_number

    def set_testcase(self, testcase: str):
        self._testcase = testcase

    def get_testcase(self):
        return self._testcase

    def get_cwdWorkingDir(self):
        return self._cwdWorkingDir

    def get_XcalLogs(self):
        return desktopDirectory
    
    def set_noOfDevice(self, noOfDevice: str):
        self._noOfDevice = noOfDevice

    def get_noOfDevice(self):
        return self._noOfDevice

    def get_timeFormat(self):
        current_time = datetime.datetime.now()
        time_stamp = current_time.timestamp()
        date_time = datetime.datetime.fromtimestamp(time_stamp)
        str_date_time = "Log_Date_" + date_time.strftime("%d_%m_%Y_Time_%H_%M_%S")
        print('time format:', str(str_date_time))
        return str(str_date_time)

    def set_modeviceid(self, modeviceid):
        self._modeviceid = modeviceid

    def get_modeviceid(self):
        return self._modeviceid

    def set_mophonenumber(self, mophonenumber):
        self._mophonenumber = mophonenumber

    def get_mophonenumber(self):
        return self._mophonenumber
    
    def set_mfdeviceid(self, mfdeviceid):
        self._mfdeviceid = mfdeviceid

    def get_mfdeviceid(self):
        return self._mfdeviceid

    def set_mfphonenumber(self, mfphonenumber):
        self._mfphonenumber = mfphonenumber

    def get_mfphonenumber(self):
        return self._mfphonenumber
    
    def set_mtdeviceid(self, mtdeviceid):
        self._mtdeviceid = mtdeviceid

    def get_mtdeviceid(self):
        return self._mtdeviceid

    def set_mtphonenumber(self, mtphonenumber):
        self._mtphonenumber = mtphonenumber

    def get_mtphonenumber(self):
        return self._mtphonenumber

    def set_networktype(self, networkType):
        self._networkType = networkType

    def get_networktype(self):
        return self._networkType
    
    def set_xcalfilename(self, xcalfilename):
        self._xcalfilename = xcalfilename

    def get_xcalfilename(self):
        return self._xcalfilename
    
    def set_adbfilename(self, adbfilename: str):
        self._adbfilename = adbfilename

    def get_adbfilename(self):
        return self._adbfilename
    
    def set_mtadbfilename(self, mtadbfilename: str):
        self._mtadbfilename = mtadbfilename

    def get_mtadbfilename(self):
        return self._mtadbfilename
    
    def set_mfadbfilename(self, mfadbfilename: str):
        self._mfadbfilename = mfadbfilename

    def get_mfadbfilename(self):
        return self._mfadbfilename
    
    def set_adbprocessid(self, adbprocessid):
        self._adbprocessid = adbprocessid

    def get_adbprocessid(self):
        return self._adbprocessid
    
    def set_mtadbprocessid(self, mtadbprocessid):
        self._mtadbprocessid = mtadbprocessid

    def get_mtadbprocessid(self):
        return self._mtadbprocessid
    
    def set_mfadbprocessid(self, mfadbprocessid):
        self._mfadbprocessid = mfadbprocessid

    def get_mfadbprocessid(self):
        return self._mfadbprocessid
    
    def get_devicem1details(self):
        return self._deviceM1
    
    def get_devicem2details(self):
        return self._deviceM2

    def get_devicem3details(self):
        return self._deviceM3
    
    def get_originNumber(self):
        return self._callingNumber
    
    def get_terminating_number2(self):
        return self._terminatingNumber2
    
    def get_terminating_number3(self):
        return self._terminatingNumber3
    
    def get_terminating_number4(self):
        return self._terminatingNumber4
    
