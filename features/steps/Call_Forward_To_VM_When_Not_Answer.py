import time

import allure
from behave import *
import common_util
import re

from utils import log_analyzer as log

@then(u'the user analyzes the call forward not answered to Voice Mail traces')
def analysing_traces_for_cfna_to_VM(context):
    try:
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
            "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]" : "FlagA_180_Ringing",
            "SIPMSG[0]: [<--] SIP/2.0 181 Call Is Being Forwarded [CSeq: 1 INVITE]" : "FlagA_181_call_forwarded",
            "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "FlagA_183_Session_in_Progress_2",
            "SIPMSG[0]: [-->] PRACK" : "FlagA_PRACK_2",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "FlagA_200_OK_2",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 1 INVITE]" : "FlagA_200_OK_3",
            "SIPMSG[0]: [-->] ACK" : "FlagA_ACK",
            "SIPMSG[0]: [-->] BYE sip" : "FlagA_Bye",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 3 BYE]" : "FlagA_200_OK_Bye",
        }

        log.analyze_log(context, filename, flag_messages)

        with allure.step(".     =====> Log  <========== Subscriber B"):
            pass

        # Define log file path
        filename = common_util.adblogfilename('subB')
        # Define flag names and corresponding log messages
        flag_messages = {
            "updateCallForward {cfType = Unanswered, action = Registration, ssClass = ALL, noReplyTimer = 0, number = xxxxx} {Success}" : "FlagB_CF_Not_answer",
            "SIPMSG[0]: [<--] INVITE" : "FlagB_INVITE",
            "SIPMSG[0]: [-->] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "FlagB_183_Session_in_Progress",
            "SIPMSG[0]: [<--] PRACK" : "FlagB_PRACK",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "FlagB_PRACK_200_ok",
            "SIPMSG[0]: [-->] SIP/2.0 180 Ringing [CSeq: 1 INVITE]" : "FlagB_180_Ringing",
            "SIPMSG[0]: [<--] CANCEL sip" : "FlagB_Cancel",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 1 CANCEL]" : "FlagB_Cancel_200_ok",
            "SIPMSG[0]: [-->] SIP/2.0 487 Request Terminated" : "FlagB_487_req_terminated",
            # "SIPMSG[0]: [<--] MESSAGE sip" : "FlagB_Message",
            # "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 1 MESSAGE]" : "FlagB_200_ok_message",
            # "SIPMSG[0]: [-->] MESSAGE sip" : "FlagB_Message_2",
            # "SIPMSG[0]: [<--] SIP/2.0 202 Accepted [CSeq: 1 MESSAGE]" : "FlagB_202_Accepted",
        }

        log.analyze_log(context, filename, flag_messages)


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

        with allure.step(".     =====> XCAL-Log Ends here <==========\n"): pass

    except Exception as e:
        print(f"Exception: {e}")

@then(u'then the CFNA to Voice Mail is validated')
def validation_of_log_for_CFNA_to_VM(context):
    # try:
    # with allure.step(context.FlagA_183_Session_in_Progress): pass
    # with allure.step(context.FlagA_181_call_forwarded): pass
    # with allure.step(context.FlagA_200_OK_Bye): pass
    # with allure.step(context.FlagB_487_req_terminated): pass
    if context.FlagA_200_OK_Bye and context.FlagB_487_req_terminated:
        with allure.step('Voice Mail Deposit:PASS'):
            pass
    else:
        with allure.step('Voice Mail Deposit:FAIL'):
            assert False, "Test Failed"
    # except Exception as e:
    #     assert False, "Test Failed"