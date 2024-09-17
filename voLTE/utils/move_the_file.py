import shutil
import os
import datetime

# file_location = "C:\\Users\\TRDEVHOST020\\Desktop\\XCAL_Logs"
# print(str(file_location).replace("\\","/"))
# Destination_directory = str(file_location).replace("\\","/") + "/Test_Case_Executed_on" + formatted_string

def move_file(source_file, destination_directory, new_file_name):

    os.makedirs(destination_directory, exist_ok=True)
    destination_file = os.path.join(destination_directory, new_file_name)
    shutil.move(source_file, destination_file)
    print(f"File moved from {source_file} to {destination_file}")

# for fi in os.listdir(file_location):
#     if fi.endswith(".aof"):
#         # file = str(file_location).replace("\\","/") + "/abc.aof"
#         # print(fi)
#         # file = fi
#         file = str(file_location).replace("\\", "/") + "/" + str(fi)


def move_file_(destination_directory, new_file_name):

    file_location = destination_directory

    timestamp = datetime.datetime.now().timestamp()
    formatted_string = datetime.datetime.fromtimestamp(timestamp).strftime("_Date_%Y_%m_%d_Time_%H_%M_%S")
    print("Formatted Timestamp:", formatted_string)

    new_file_name = str(new_file_name) + str(formatted_string) + str(".aof")

    for fi in os.listdir(destination_directory):
        if fi.endswith(".aof"):
            source_file = str(file_location).replace("\\", "/") + "/" + str(fi)

    destination_file = os.path.join(destination_directory, new_file_name)
    shutil.move(source_file, destination_file)
    print(f"File moved from {source_file} to {destination_file}")

move_file_("C:\\Users\\TRDEVHOST020\\Desktop\\XCAL_Logs", "TC001_VoLTE_Call")
