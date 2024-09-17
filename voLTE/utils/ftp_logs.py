import os
import shutil
import json
from http.client import HTTPException

import allure


def ftp_logs():
    os.chdir("..")
    report_loc = os.path.join(os.getcwd(),"traces")
    # report_loc = os.path.join(os.getcwd())
    file = os.listdir(str(report_loc))
    # files = file.sort(key=os.path.getctime(behave_report_loc))
    report_zip_file = str(file[-1])
    print('Logfile name: ' + report_zip_file)
    zipfileloc = os.path.join(report_loc,report_zip_file)
    # json_file_path = os.path.join(os.path.dirname(__file__), 'config', 'Config.json')
    json_file_path = os.path.join(os.getcwd(), '_internal\\config', 'Config.json')

    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        print('Copying the log files to upload to the FTP server')

        if 'serverDetails' in data:
            server_details = data['serverDetails']
            required_keys = ['serverUserName', 'serverPassword', 'folderName', 'serverUrl']
            # print('required key value:' + required_keys)
            if all(key in server_details and server_details[key] for key in required_keys):
                print('serverDetails exists and contains all required non-empty values')
                # log_file_draft = f"templates/file-upload-drafts/behave_{timestamp}.log"
                # Copy the file
                # log_file = f"server/templates/file-upload-drafts"
                log_file_draft = os.path.join(os.getcwd(), 'templates\\file-upload-drafts')
                print('log_file_draft:' + log_file_draft)
                print('zipfileloc:' + zipfileloc)
                try:
                    shutil.copy(zipfileloc, log_file_draft)
                    print("Copied " + zipfileloc + " to " + log_file_draft)
                except Exception as e:
                    raise HTTPException(status_code=500, detail=f"Error copying file to files_draft: {str(e)}")
            else:
                print('serverDetails exists but does not contain all required non-empty values')

        else:
            print('serverDetails does not exist')

    except Exception as e:
        print('The file was not copied for the upload to the FTP server')

    # os.chdir("..")
    # adb_log_file = os.listdir(os.getcwd())
    # for file in adb_log_file:
    #     # with allure.step(str(file)): pass
    #     if file.__contains__("Date") and file.__contains__("Time"):
    #         os.remove(file)