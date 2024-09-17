import allure
from behave import *
import common_util
import re

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'Analyze the traces for call waiting')
def analysing_traces_for_call_waiting(context):
    try:
        with allure.step(".     =====> ADB-Log Starts here <==========\n"):
            pass
        with allure.step(".     =====> Log  <========== Subscriber A"):
            pass

        filename = common_util.adblogfilename('subA')

        # Define flag names and corresponding log messages
        flag_messages = {
            "updateCallWaiting {enable = Activated, ssClass = ALL} {Success}" : "FlagA_call_waiting",
            "SIPMSG[0]: [-->] INVITE" : "FlagA_INVITE",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 1 INVITE]" : "FlagA_100_Trying",
            "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "FlagA_183_Session_in_Progress",
            "SIPMSG[0]: [-->] PRACK" : "FlagA_PRACK",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "FlagA_200_OK",
            "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]" : "FlagA_180_Ringing",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 1 INVITE]" : "FlagA_200_OK_2",
            "SIPMSG[0]: [-->] ACK" : "FlagA_ACK",
            "SIPMSG[0]: [<--] INVITE" : "FlagA_INVITE_2",
            "SIPMSG[0]: [-->] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "FlagA_183_Session_in_Progress_2",
            "SIPMSG[0]: [<--] PRACK " : "FlagA_PRACK_2",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "FlagA_200_OK_3",
            "SIPMSG[0]: [-->] SIP/2.0 180 Ringing [CSeq: 1 INVITE]" : "FlagA_180_Ringing_2",
            "SIPMSG[0]: [<--] BYE" : "FlagA_Bye",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 2 BYE]" : "FlagA_200_OK_Bye",
            "SIPMSG[0]: [<--] CANCEL" : "FlagA_CANCEL",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 1 CANCEL]" : "FlagA_200_OK_4",
            "SIPMSG[0]: [-->] SIP/2.0 487 Request Terminated [CSeq: 1 INVITE]" : "FlagA_487",

        }

        log.analyze_log(context, filename, flag_messages)

        # Initialize flags
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
        # context.call_waiting_A = flags["Flag_487"]

        with allure.step(".     =====> Log  <========== Subscriber C"):
            pass

        # Define log file path
        filename = common_util.adblogfilename('subC')

        # Define flag names and corresponding log messages
        flag_messages = {

            "SIPMSG[0]: [-->] INVITE" : "FlagC_INVITE",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 1 INVITE]" : "FlagC_100_Trying",
            "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "FlagC_183_Session_in_Progress",
            "SIPMSG[0]: [-->] PRACK" : "FlagC_PRACK",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "FlagC_PRACK_200_ok",
            "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]" : "FlagC_180_Ringing",
            "SIPMSG[0]: [-->] CANCEL" : "FlagC_CANCEL",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 1 CANCEL]" : "FlagC_Cancel_200_OK",
            "SIPMSG[0]: [<--] SIP/2.0 487 Request Terminated [CSeq: 1 INVITE]" : "FlagC_487",
        }
        
        log.analyze_log(context, filename, flag_messages)

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
        # context.call_waiting_C = flags["Flag_487"]

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

@then(u'validate the test Outcome for call waiting')
def validation_of_log_for_call_waiting(context):
    try:
        if context.FlagA_call_waiting and context.FlagA_183_Session_in_Progress and context.FlagA_180_Ringing_2 and context.FlagA_487 and context.FlagC_180_Ringing and context.FlagC_487:
            with allure.step('Call Waiting: PASS'):
                pass
        else:
            with allure.step('Call Waiting: FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        print(f"Exception: {e}")