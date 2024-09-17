import allure
from behave import *
import common_util
import re

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'the user analyze the 5G Call trace')
def analysing_traces_for_5G_call(context):

    with allure.step(".     =====> ADB-Log Starts here <=========="): pass
    with allure.step(".     =====> Log  <========== Subscriber A"): pass
    filename  = common_util.adblogfilename('subA')

    flag_messages = {
            "SIPMSG[0]: [-->] INVITE" : "Flag_INVITE",
            "SIPMSG[0]: [<--] SIP/2.0 100 Trying [CSeq: 1 INVITE]" : "Flag_100_Trying",
            "SIPMSG[0]: [<--] SIP/2.0 183 Session Progress [CSeq: 1 INVITE]" : "Flag_183_Session_in_Progress",
            "SIPMSG[0]: [-->] PRACK" : "Flag_PRACK",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 2 PRACK]" : "Flag_200_OK",
            "SIPMSG[0]: [<--] SIP/2.0 180 Ringing [CSeq: 1 INVITE]" : "Flag_180_Ringing",
            "SIPMSG[0]: [<--] SIP/2.0 200 OK [CSeq: 1 INVITE]" : "Flag_200_OK_2",
            "SIPMSG[0]: [-->] ACK" : "Flag_ACK",
            "SIPMSG[0]: [<--] BYE" : "Flag_Bye",
            "SIPMSG[0]: [-->] SIP/2.0 200 OK [CSeq: 2 BYE]" : "Flag_Bye_200_OK",
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
    # context.VoLTE_1_to_1_call = flags["Flag_Bye_200_OK"]
    with allure.step(".     =====> ADB-Log Ends here <==========\n"): pass

    with allure.step(".     =====> XCAL-Log Starts here <==========\n"): pass

    filename = common_util.get_XCAL_Filename()

    patterns = {
        "|Service request": "XCAL_1",
        "|Activate dedicated EPS bearer context request": "XCAL_2",
        "|Activate dedicated EPS bearer context accept": "XCAL_3",
        "|Deactivate EPS bearer context request": "XCAL_4",
        "|Deactivate EPS bearer context accept": "XCAL_5"
    }

    log.XCAL_log(context, filename, patterns)

    with allure.step(".     =====> XCAL-Log Ends here <==========\n"): pass

@then(u'then the user validates the logs')
def validation_of_log_for_5G_call(context):

    try:
        if context.Flag_183_Session_in_Progress and context.Flag_180_Ringing and context.Flag_Bye_200_OK:
            with allure.step('VoNR CALL : PASS'):pass
        else:
            with allure.step('VoNR CALL : FAIL'):
                assert False, "Test Failed_"
    except Exception as e:
        assert False, "Test Failed__"