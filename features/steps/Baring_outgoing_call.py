import allure
from behave import *
import common_util
import re

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'the user analyzes the baring outgoing call traces')
def analysing_traces_for_outgoing_call_baring(context):
    try:
        with allure.step(".     =====> ADB-Log Starts here <==========\n"):
            pass
        with allure.step(".     =====> Log  <========== Subscriber A"):
            pass

        filename = common_util.adblogfilename('subA')

        # Define flag names and corresponding log messages
        flag_messages = {
            "updateCallBarring {cbType = All outgoing calls, action = Activation, ssClass = ALL, password = null} {Success}" : "Flag_call_barring_activate",
            "updateCallBarring {cbType = All outgoing calls, action = Deactivation, ssClass = ALL, password = null} {Success}" : "Flag_call_barring_deactivate",
        }

        log.analyze_log(context, filename, flag_messages)
        #
        # # Initialize flags
        # flags = {flag: False for flag in flag_messages}
        #
        # with open(filename, 'r', encoding="latin-1") as file:
        #     lines = file.readlines()
        #
        # # Iterate over lines in the log file
        # for line in lines:
        #     for flag, message in flag_messages.items():
        #         if not flags[flag] and message in line:
        #             flags[flag] = True
        #             pattern = r"\.\d+\s+\d+\s+\d+\s+I\s+"
        #             string_cleaned = re.sub(pattern, " ", line)
        #             with allure.step('Log ' + string_cleaned):
        #                 pass
        #             break
        #
        # # Check if all flags are set
        # for flag, flag_set in flags.items():
        #     if not flag_set:
        #         with allure.step(flag_messages[flag] + ' not found'):
        #             assert False, "Test Failed"
        #
        # # Set context variables based on flag conditions
        # context.All_Outgoing_calls_barring = flags["Flag_487_request_terminated"]

        
        with allure.step(".     ==========> ADB-Log Ends here <=========="):
            pass

        with allure.step(".     =====> XCAL-Log Starts here <==========\n"):
            pass

        filename = common_util.get_XCAL_Filename()

        # Subscriber_B = '02'
        # get_XCAL_Filename(Subscriber_B, context.testCase_name)
        patterns = {
            "|Activate default EPS bearer context request": "XCAL_1",
            "|Activate default EPS bearer context accept": "XCAL_2",
            "|Deactivate EPS bearer context request": "XCAL_3",
            "|Deactivate EPS bearer context accept": "XCAL_4"
        }

        log.XCAL_log(context, filename, patterns)

        with allure.step(".     =====> XCAL-Log Ends here <==========\n"):
            pass
        with allure.step(context.All_Outgoing_calls_barring):
            pass

    except Exception as e:
        print(f"Exception: {e}")

@then(u'then validate the baring the outgoing call traces')
def validation_of_log_for_outgoing_call_baring(context):
    try:
        if context.Flag_call_barring_activate and context.Flag_call_barring_deactivate:
            with allure.step('All Outgoing Call Barring: PASS'):
                pass
        else:
            with allure.step('All Outgoing Call Barring: FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        assert False, "Test Failed"