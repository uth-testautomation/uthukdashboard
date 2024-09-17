import allure
from behave import *
import common_util
import re

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'the user analyzes the call forward not answered traces')
def analysing_traces_for_cfna(context):
    try:
        with allure.step(".     =====> ADB-Log Starts here <==========\n"): pass
        with allure.step(".     =====> Log  <========== Subscriber A"): pass

        filename = common_util.adblogfilename('subA')

        # Define flag names and corresponding log messages
        flag_messages = {
            # "Flag_INVITE": "SIPMSG[0]: [-->] INVITE",
            # "Flag_100_Trying": "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 1 INVITE]",
            # "Flag_183_Session_in_Progress": "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]",
            # "Flag_PRACK": "SIPMSG[0]: [-->] PRACK",
            # "Flag_200_OK": "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]",
            # "Flag_180_Ringing": "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]",
            # "Flag_181_call_forwarded": "SIPMSG[0]: [<--] SIP/2.0 181 Call Is Being Forwarded [CSeq: 1 INVITE]",
            # "Flag_183_Session_in_Progress_2": "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]",
            # "Flag_PRACK_2": "SIPMSG[0]: [-->] PRACK",
            # "Flag_200_OK_2": "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]",
            # "Flag_180_Ringing_2": "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]",
            # "Flag_200_0k_4": "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 1 INVITE]",
            # "Flag_ACK_3": "SIPMSG[0]: [-->] ACK",
            # "Flag_Bye": "SIPMSG[0]: [-->] BYE sip",
            # "Flag_200_OK_Bye": "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 3 BYE]"
            "SIPMSG[0]: [-->] INVITE": "FlagA_INVITE",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 1 INVITE]": "FlagA_100_Trying",
            "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]": "FlagA_183_Session_in_Progress",
            "SIPMSG[0]: [-->] PRACK": "FlagA_PRACK",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]": "FlagA_200_OK",
            "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]": "FlagA_180_Ringing",
            "SIPMSG[0]: [<--] SIP/2.0 181 Call Is Being Forwarded [CSeq: 1 INVITE]": "FlagA_181_call_forwarded",
            "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]": "FlagA_183_Session_in_Progress_2",
            "SIPMSG[0]: [-->] PRACK": "FlagA_PRACK_2",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]": "FlagA_200_OK_2",
            "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]": "FlagA_180_Ringing_2",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 1 INVITE]": "FlagA_200_0k_4",
            "SIPMSG[0]: [-->] ACK": "FlagA_ACK_3",
            "SIPMSG[0]: [-->] BYE sip": "FlagA_Bye",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 3 BYE]": "FlagA_200_OK_Bye"
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
        # context.CFNA_to_third_party_Sub_A = flags["Flag_200_OK_Bye"]

        with allure.step(".     =====> Log  <========== Subscriber B"): pass

        # Define log file path
        filename = common_util.adblogfilename('subB')
        # Define flag names and corresponding log messages
        flag_messages = {
            # "Flag_CF_Not_answer": "updateCallForward {cfType = Unanswered, action = Registration, ssClass = ALL, noReplyTimer = 0, number = xxxxx} {Success}",
            # "Flag_INVITE": "SIPMSG[0]: [<--] INVITE",
            # "Flag_183_Session_in_Progress": "SIPMSG[0]: [-->] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]",
            # "Flag_PRACK": "SIPMSG[0]: [<--] PRACK",
            # "Flag_PRACK_200_ok": "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 2 PRACK]",
            # "Flag_180_Ringing": "SIPMSG[0]: [-->] SIP/2.0 180 Ringing [CSeq: 1 INVITE]",
            # "Flag_CANCEL": "SIPMSG[0]: [<--] CANCEL",
            # "Flag_200_ok_Cancel": "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 1 CANCEL]",
            # "Flag_request_terminated": "SIPMSG[0]: [-->] SIP/2.0 487 Request Terminated [CSeq: 1 INVITE]"
            "updateCallForward {cfType = Unanswered, action = Registration, ssClass = ALL, noReplyTimer = 0, number = xxxxx} {Success}": "FlagB_CF_Not_answer",
            "SIPMSG[0]: [<--] INVITE": "FlagB_INVITE",
            "SIPMSG[0]: [-->] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]": "FlagB_183_Session_in_Progress",
            "SIPMSG[0]: [<--] PRACK": "FlagB_PRACK",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 2 PRACK]": "FlagB_PRACK_200_ok",
            "SIPMSG[0]: [-->] SIP/2.0 180 Ringing [CSeq: 1 INVITE]": "FlagB_180_Ringing",
            "SIPMSG[0]: [<--] CANCEL": "FlagB_CANCEL",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 1 CANCEL]": "FlagB_200_ok_Cancel",
            "SIPMSG[0]: [-->] SIP/2.0 487 Request Terminated [CSeq: 1 INVITE]": "FlagB_request_terminated"
        }

        log.analyze_log(context, filename, flag_messages)
        #
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
        # context.CFB_to_third_party_Sub_B = flags["Flag_request_terminated"]

        with allure.step(".     ==========> ADB-Log Ends here <=========="): pass

        with allure.step(".     =====> XCAL-Log Starts here <==========\n"):
            pass

        filename = common_util.get_XCAL_Filename()

        # Subscriber_B = '02'
        # get_XCAL_Filename(Subscriber_B, context.testCase_name)
        patterns = {
            "|Activate dedicated EPS bearer context request": "XCAL_1",
            "|Activate dedicated EPS bearer context accept": "XCAL_2",
            "|Deactivate EPS bearer context request": "XCAL_3",
            "|Deactivate EPS bearer context accept": "XCAL_4"
        }

        log.XCAL_log(context, filename, patterns)

        with allure.step(".     =====> XCAL-Log Ends here <==========\n"):
            pass

    except Exception as e:
        print(f"Exception: {e}")

@then(u'then the CFNA to third party is validated')
def validation_of_log_for_CFNA(context):
    try:
        with allure.step(context.Flag_180_Ringing):
            pass
        with allure.step(context.Flag_181_call_forwarded):
            pass
        with allure.step(context.Flag_180_Ringing_2):
            pass
        with allure.step(context.FlagB_183_Session_in_Progress):
            pass
        with allure.step(context.FlagB_CANCEL):
            pass
        with allure.step(context.FlagB_request_terminated):
            pass
        if context.Flag_180_Ringing and context.Flag_181_call_forwarded and context.Flag_180_Ringing_2 and context.FlagB_183_Session_in_Progress and context.FlagB_CANCEL and context.FlagB_request_terminated:
            with allure.step('CFNA to third party: PASS'):
                pass
        else:
            with allure.step('CFNA to third party: FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        print(f"Exception: {e}")