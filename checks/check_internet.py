import shutil

from fastapi import FastAPI, HTTPException,Body
import time
import requests
from ftplib import FTP
import glob
from datetime import datetime
import os
import json
import base64
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment, FileContent, FileName, FileType, Disposition

file_uploads_directory = 'templates/file-upload-drafts/*.zip'
emails_directory = 'templates/report-drafts/*.html'
reports_directory = 'templates/report-drafts'

# authConfig
auth_config_dir = os.path.join(os.path.dirname(__file__), 'config', "authConfig.json")

# config Dir
auth_config_dir = os.path.join(os.path.dirname(__file__), 'config', "Config.json")

def upload_log_files(local_file_path, server_details):

    # Check if the log file exists and has content
    # if not os.path.exists(local_file_path) or os.path.getsize(local_file_path) == 0:
    #     raise HTTPException(status_code=500, detail="Log file does not exist or is empty.")

    # FTP the log file
    try:
        print(f"Connecting to FTP server at {datetime.now()}")
        host = server_details['serverUrl']
        username = server_details['serverUserName']
        password = decrypt_password(server_details['serverPassword'])
        remote_directory = server_details['folderName']

        # Connect to the FTP server
        ftp = FTP(host)
        print(f"Connected to FTP server {host}")

        # print("=========================password", password)

        # Login to the FTP server
        ftp.login(user=username, passwd=password)
        # ftp.set_pasv(True)
        print(f"Logged in to FTP server")

        # Change to the specified directory 
        ftp.cwd(remote_directory)
        print(f"Changed to remote directory: {remote_directory}")
        print("local_file_path", local_file_path)
        print("os.path.basename(local_file_path)", os.path.basename(local_file_path))

        # Open the local file
        with open(local_file_path, 'rb') as local_file:
            # Upload the file
            ftp.storbinary(f'STOR {os.path.basename(local_file_path)}', local_file)
            print(f"File uploaded successfully to {remote_directory}/{os.path.basename(local_file_path)}")

        # Quit the FTP session
        ftp.quit()
        print(f"FTP session closed at {datetime.now()}")\

        # Delete the local file after successful upload
        os.remove(local_file_path)
        print(f"Deleted local file: {local_file_path}")

    except Exception as ftp_error:
        print(f"Error uploading log file to FTP: {str(ftp_error)}")
        raise HTTPException(status_code=500, detail=f"Error uploading log file to FTP: {str(ftp_error)}")

def decrypt_password(encoded_password: str) -> str:
    return base64.b64decode(encoded_password.encode('utf-8')).decode('utf-8')

def fetch_server_details():
    try:
        with open(auth_config_dir, 'r') as file:
            data = json.load(file)
        
        server_details = data.get('serverDetails', {})
        required_keys = ['serverUserName', 'serverPassword', 'folderName', 'serverUrl']
        
        if all(key in server_details for key in required_keys):
            print("Server Details:", server_details)
            return server_details
        else:
            missing_keys = [key for key in required_keys if key not in server_details]
            print("Server details not found or missing keys:", missing_keys)
            return None
    except FileNotFoundError:
        print("Config file not found")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON from the config file")
        return None

def fetch_email_ids():
    try:
        with open(auth_config_dir, 'r') as file:
            data = json.load(file)
        
        email_ids = data.get('emailIds', [])
        if email_ids:
            print("email ids:", email_ids)
            return email_ids
        else:
            print("email ids not found")
            return None
    except FileNotFoundError:
        print("Config file not found")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON from the config file")
        return None

def delete_files(local_file_path):
    # Delete the local file after successful upload
    os.remove(local_file_path)
    print(f"Deleted local file: {local_file_path}")

def send_email_with_attachments(email_details, email_drafts):

    sendgrid_api_key = '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'
    from_email = 'report@uth-uk.com'
    # sendgrid_api_key = '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'
    # from_email = 'shilpa.rajashekar@rhibhus.com'
    subject = 'Testcase execution reports'

    # Initialize SendGrid client
    sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)

    # Loop through all files in the folder and send an email for each file
    for filename in os.listdir(reports_directory):
        file_path = os.path.join(reports_directory, filename)

        # Create the mail object
        from_email_obj = Email(from_email)
        to_email_obj = To(email_details[0])
        content_text = f"<html><body><p>Hello there,<br><br>Please find the attached report.<br><br>Regards,<br>Team UTH</p></body></html>"
        content = Content("text/html", content_text)
        mail = Mail(from_email_obj, to_email_obj, subject, content)

        # Add all recipients
        for recipient_email in email_details[1:]:
            mail.personalizations[0].add_to(Email(recipient_email))
        
        with open(file_path, 'rb') as f:
            data = f.read()

        encoded_file = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.file_content = FileContent(encoded_file)
        attachment.file_type = FileType('application/octet-stream')  # Use a general MIME type
        attachment.file_name = FileName(filename)
        attachment.disposition = Disposition('attachment')
        mail.add_attachment(attachment)
        
        # Send the email
        try:
            response = sg.client.mail.send.post(request_body=mail.get())
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.body}")
        except Exception as e:
            print(f"Error: {e}")

    # Delete all the files inside the folder
    for filename in os.listdir(reports_directory):
        file_path = os.path.join(reports_directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print(f'Successfully deleted {file_path}')
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f'Successfully deleted directory {file_path}')
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def check_internet():
    while True:
        try:
            response = requests.get('https://www.google.com', timeout=5)
            # response.status_code = 500
            if response.status_code == 200:
                print("Internet connection is active")

                # Upload Files
                search_pattern = file_uploads_directory
        
                # Get a list of all .log files in the directory
                log_drafts = glob.glob(search_pattern)
                print("log_drafts", log_drafts)

                # Fetch the server details
                server_details = fetch_server_details()

                # Upload each log file
                if server_details:
                    for log_file in log_drafts:
                        upload_log_files(log_file, server_details)
                else:
                    print("Server details not found, skipping log file upload")
                    # for log_file in log_drafts:
                    #     delete_files(log_file)

                # Share Emails
                search_pattern_email = emails_directory
        
                # Get a list of all .html files in the directory
                email_drafts = glob.glob(search_pattern_email)
                print("email_drafts", email_drafts)

                # Fetch the email Id details
                email_details = fetch_email_ids()

                # Share each html file
                if email_details:
                    if email_drafts:
                        send_email_with_attachments(email_details, email_drafts)
                    else:
                        print("Reports not found, skipping file sharing")
                else:
                    print("Email details not found, skipping file sharing")
                    # for report_file in email_drafts:
                    #     delete_files(report_file)

            else:
                print("Internet connection is not active")
        except requests.ConnectionError:
            print("No internet connection")
        time.sleep(10)

if __name__ == "__main__":
    check_internet()