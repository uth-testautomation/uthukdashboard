import allure
import re
def analyze_log(context, filename, patterns):
    # with allure.step('adblogf : ' + filename): pass
    with open(filename, 'r', encoding="latin-1") as file:
        lines = file.readlines()

    for line in lines:
        for pattern, flag_name in patterns.items():
            if pattern in line and "StackIF" not in line:
                setattr(context, flag_name, True)
                pattern = r"\.\d+\s+\d+\s+\d+\s+I\s+"
                string_cleaned = re.sub(pattern, " ", line)
                with allure.step('Log : ' + string_cleaned):
                    pass
            # else:
            #     with allure.step('Log : ' + string_cleaned):
            #         assert False

def XCAL_log(context, filename, patterns):
    with open(filename, 'r', encoding="latin-1") as file:
        lines = file.readlines()
    for line in lines:
        for pattern, flag_name in patterns.items():
            if pattern in line and "StackIF" not in line:
                setattr(context, flag_name, True)
                sub_string = pattern
                pattern = r"\.\d+\s+\d+\s+\d+\s+I\s+"
                string_cleaned = re.sub(pattern, " ", line)

                position = string_cleaned.find(pattern)
                string_cleaned = string_cleaned[:position+len(pattern)]
                string_cleaned = string_cleaned +" "+sub_string
                with allure.step('Log : ' + string_cleaned):
                    pass