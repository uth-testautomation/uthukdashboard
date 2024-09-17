import os
import time


def sevendaysCron(local: str):
    # allure_history_path = os.path.join(str(os.getcwd()), "server\\templates\\allure-report-history")
    allure_history_path = local

    # N is the number of days for which
    # we have to check whether the file
    # is older than the specified days or not
    N = 7

    # changing the current working directory
    # to the folder specified
    os.chdir(os.path.join(os.getcwd(), allure_history_path))

    # get a list of files present in the given folder
    list_of_files = os.listdir(allure_history_path)

    # get the current time
    current_time = time.time()

    # "day" is the number of seconds in a day
    day = 86400

    # loop over all the files
    for file in list_of_files:
        # get the location of the file
        file_location = os.path.join(allure_history_path, file)
        # file_time is the time when the file is modified
        file_time = os.stat(file_location).st_mtime

        # if a file is modified before N days then delete it 
        if (file_time < current_time - day * N):
            print(f" Delete : {file}")
            os.remove(file_location) 