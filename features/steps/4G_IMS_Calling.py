import allure
from behave import *
import re
import common_util

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'the user analyze the VoLTE Call trace')
def analysing_traces_for_4G_IMS_call(context):

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

    with allure.step(".     =====> ADB-Log Ends here <==========\n"): pass

    with allure.step(".     =====> XCAL-Log Starts here <==========\n"): pass

    filename = common_util.get_XCAL_Filename()

    patterns = {
        "|Activate dedicated EPS bearer context request": "XCAL_1",
        "|Activate dedicated EPS bearer context accept": "XCAL_2",
        "|Deactivate EPS bearer context request": "XCAL_3",
        "|Deactivate EPS bearer context accept": "XCAL_4"
    }

    log.XCAL_log(context, filename, patterns)

    with allure.step(".     =====> XCAL-Log Ends here <==========\n"): pass

@then(u'then the user validates the VoLTE logs')
def validation_of_log_for_4G_IMS_call(context):

    try:
        if context.Flag_200_OK_2 and context.XCAL_4:
            with allure.step('VoLTE CALL : PASS'):pass
        else:
            with allure.step('VoLTE CALL : FAIL'):
                assert False, "Test Failed_"
    except Exception as e:
        assert False, "Test Failed__"