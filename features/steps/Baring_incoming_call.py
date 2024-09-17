import allure
from behave import *
import common_util
import re, time

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'the user analyzes the baring incoming call traces')
def analysing_traces_for_incoming_call_baring(context):
    try:
        time.sleep(5)
        with allure.step(".     =====> ADB-Log Starts here <==========\n"): pass
        with allure.step(".     =====> Log  <========== Subscriber A"): pass

        filename = common_util.adblogfilename('subA')

        # Define flag names and corresponding log messages
        flag_messages = {
            "SIPMSG[0]: [-->] INVITE" : "FlagA_INVITE",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 1 INVITE]" : "FlagA_100_Trying",
            "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "FlagA_183_Session_in_Progress",
            "SIPMSG[0]: [-->] PRACK" : "FlagA_PRACK",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "FlagA_200_OK",
            "SIPMSG[0]: [<--] SIP/2.0 487 Request Terminated [CSeq: 1 INVITE]" : "FlagA_487_request_terminated",
        }

        log.analyze_log(context, filename, flag_messages)

        # Initialize flags
        # flags = {flag: False for flag in flag_messages}
        #
        # with open(filename, 'r', encoding="latin-1") as file:
        #     lines = file.readlines()
        # time.sleep(10)
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
        # context.All_Incoming_calls_barring_A = flags["Flag_487_request_terminated"]

        with allure.step(".     =====> Log  <========== Subscriber B"): pass


        # Define log file path
        filename = common_util.adblogfilename('subB')

        # Define flag names and corresponding log messages
        flag_messages = {
            "updateCallBarring {cbType = All incoming calls, action = Activation, ssClass = ALL, password = null} {Success}" : "FlagB_call_barring_activate",
        }

        log.analyze_log(context, filename, flag_messages)

        # # Initialize flags
        # flags = {flag: False for flag in flag_messages}
        #
        # # Process log file
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
        # # Set context variable based on flag conditions
        # context.All_Incoming_calls_barring_Ut = flags["Flag_call_barring_activate"]

        with allure.step(".     ==========> ADB-Log Ends here <=========="): pass

        with allure.step(".     =====> XCAL-Log Starts here <==========\n"):
            pass

        filename = common_util.get_XCAL_Filename()
        patterns = {
           "|Activate dedicated EPS bearer context request": "XCAL_1",
           "|Activate dedicated EPS bearer context accept": "XCAL_2"
           #"Attach accept - Activate default EPS bearer context request": "XCAL_3",
          # "Attach complete - Activate default EPS bearer context accept": "XCAL_4"
        }

        log.XCAL_log(context, filename, patterns)

        with allure.step(".     =====> XCAL-Log Ends here <==========\n"):
            pass

    except Exception as e:
        print(f"Exception: {e}")

@then(u'then validate the baring the incoming call traces')
def validation_of_log_for_incoming_call_baring(context):
    try:
        if context.FlagA_183_Session_in_Progress and context.FlagA_487_request_terminated and context.FlagB_call_barring_activate:
            with allure.step('All Incoming Call Barring: PASS'):
                pass
        else:
            with allure.step('All Incoming Call Barring: FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        assert False, "Test Failed"