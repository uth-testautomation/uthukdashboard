import allure
from behave import *
import common_util
import re

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'Analyze the traces for call busy')
def analysing_traces_for_call_busy(context):
    try:
        with allure.step(".     =====> ADB-Log Starts here <==========\n"):
            pass
        with allure.step(".     =====> Log  <========== Subscriber A"):
            pass

        filename = common_util.adblogfilename('subA')

        # Define flag names and corresponding log messages
        flag_messages = {

            "SIPMSG[0]: [-->] INVITE" : "FlagA_INVITE",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 1 INVITE]" : "FlagA_100_Trying",
            "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "FlagA_183_Session_in_Progress",
            "SIPMSG[0]: [-->] PRACK" : "FlagA_PRACK",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "FlagA_200_OK",
            "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]" : "FlagA_180_Ringing",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 1 INVITE]" : "FlagA_200_OK_2",
            "SIPMSG[0]: [-->] ACK" : "FlagA_ACK",
            "SIPMSG[0]: [<--] INVITE" : "FlagA_INVITE_2",
            "SIPMSG[0]: [-->] SIP/2.0 486 Busy Here [CSeq: 1 INVITE]" : "FlagA_Busy_here"
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
        # context.call_busy_sub_A = flags["Flag_Busy_here"]

        with allure.step(".     =====> Log  <========== Subscriber C"): pass

        # Define log file path
        filenameC = common_util.adblogfilename('subC')
        # Define flag names and corresponding log messages
        flag_message = {
            "SIPMSG[0]: [-->] INVITE" : "FlagC_INVITE",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 1 INVITE]" : "FlagC_100_Trying",
            "SIPMSG[0]: [<--] SIP/2.0 486 Busy Here [CSeq: 1 INVITE]" : "FlagC_Busy_here",
        }

        log.analyze_log(context, filenameC, flag_message)

        # Initialize flags
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
        # context.call_busy_sub_C = flags["Flag_Busy_here"]

        with allure.step(".     ==========> ADB-Log Ends here <=========="):
            pass

        with allure.step(".     =====> XCAL-Log Starts here <==========\n"):
            pass

        filename = common_util.get_XCAL_Filename()

        patterns = {
            "|Activate default EPS bearer context request": "XCAL_1",
            "|Activate default EPS bearer context accept": "XCAL_2",
            "|Deactivate EPS bearer context request": "XCAL_3",
            "|Deactivate EPS bearer context accept": "XCAL_4"
        }

        log.XCAL_log(context, filename, patterns)

        with allure.step(".     =====> XCAL-Log Ends here <==========\n"):
            pass

    except Exception as e:
        print(f"Exception: {e}")

@then(u'validate the test Outcome for call busy')
def validation_of_log_for_call_busy(context):
    try:
        if context.FlagA_180_Ringing and context.FlagA_Busy_here and context.FlagC_100_Trying and context.FlagC_Busy_here:
            with allure.step('Call Busy: PASS'):
                pass
        else:
            with allure.step('Call Busy: FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        print(f"Exception: {e}")