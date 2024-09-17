import allure
from behave import *
import common_util
import re

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'Analyze the traces for call hold and resume')
def analysing_traces_for_call_hold_and_resume(context):
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
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 1 INVITE]" : "FlagA_200_0k_Invite",
            "SIPMSG[0]: [-->] ACK" : "FlagA_ACK",
            "ImsCall : hold ::" : "FlagA_onhold",
            "SIPMSG[0]: [-->] INVITE" : "FlagA_INVITE_2",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 3 INVITE]" : "FlagA_100_Trying_2",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 3 INVITE]" : "FlagA_200_0k_3",
            "SIPMSG[0]: [-->] ACK" : "FlagA_ACK_2",
            "ImsCall : resume" : "FlagA_on_resume",
            "SIPMSG[0]: [-->] INVITE" : "FlagA_INVITE_3",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 4 INVITE]" : "FlagA_100_Trying_3",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 4 INVITE]" : "FlagA_200_0k_4",
            "SIPMSG[0]: [-->] ACK" : "FlagA_ACK_3",
            "SIPMSG[0]: [-->] BYE sip" : "FlagA_Bye",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 5 BYE]" : "FlagA_200_OK_Bye",
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
        # context.call_hold_and_resume_sub_A = flags["Flag_200_OK_Bye"]

        with allure.step(".     =====> Log  <========== Subscriber B"):
            pass

        # Define log file path
        filename = common_util.adblogfilename('subB')

        # Define flag names and corresponding log messages
        flag_messages = {
            "SIPMSG[0]: [<--] INVITE" : "FlagB_INVITE",
            "SIPMSG[0]: [-->] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "FlagB_183_Session_in_Progress",
            "SIPMSG[0]: [<--] PRACK" : "FlagB_PRACK",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "FlagB_PRACK_200_ok",
            "SIPMSG[0]: [-->] SIP/2.0 180 Ringing [CSeq: 1 INVITE]" : "FlagB_180_Ringing",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 1 INVITE]" : "FlagB_200_OK",
            "SIPMSG[0]: [<--] ACK" : "FlagB_ACK",
            "SIPMSG[0]: [<--] INVITE" : "FlagB_INVITE_2",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 3 INVITE]" : "FlagB_200_OK_2",
            "SIPMSG[0]: [<--] ACK" : "FlagB_ACK_2",
            "ImsCall : callSessionHoldReceived" :"FlagB_on_hold",
            "SIPMSG[0]: [<--] INVITE" : "FlagB_INVITE_3",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 4 INVITE]" : "FlagB_200_OK_3",
            "SIPMSG[0]: [<--] ACK" : "FlagB_ACK_3",
            "ImsCall : callSessionResumeReceived" : "FlagB_on_resume",
            "SIPMSG[0]: [<--] BYE" : "FlagB_Bye",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 5 BYE]" : "FlagB_200_OK_Bye",
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
        # context.call_hold_and_resume_sub_B = flags["Flag_200_OK_Bye"]

        with allure.step(".     ==========> ADB-Log Ends here <=========="):
            pass

        with allure.step(".     =====> XCAL-Log Starts here <==========\n"):
            pass

        filename = common_util.get_XCAL_Filename()

        # Subscriber_B = '02'
        # get_XCAL_Filename(Subscriber_B, context.testCase_name)
        patterns = {
            "|Activate dedicated EPS bearer context request": "XCAL_1",
            "|Activate dedicated EPS bearer context accept": "XCAL_2",
            "|Modify EPS bearer context request": "XCAL_3",
            "|Modify EPS bearer context accept": "XCAL_4",
            "Modify EPS bearer context request": "XCAL_5",
            "Modify EPS bearer context accept": "XCAL_6",
            "|Deactivate EPS bearer context request": "XCAL_7",
            "|Deactivate EPS bearer context accept": "XCAL_8"
        }

        log.XCAL_log(context, filename, patterns)

        with allure.step(".     =====> XCAL-Log Ends here <==========\n"):
            pass

    except Exception as e:
        print(f"Exception: {e}")

@then(u'validate the test Outcome for call hold and resume')
def validation_of_log_for_call_hold_and_resume(context):
    try:
        if context.FlagA_183_Session_in_Progress and context.FlagA_onhold and context.FlagA_200_OK_Bye and context.FlagB_on_resume and context.FlagB_200_OK_Bye:
            with allure.step('Call Hold and resume: PASS'):
                pass
        else:
            with allure.step('Call Hold and resume:  FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        print(f"Exception: {e}")