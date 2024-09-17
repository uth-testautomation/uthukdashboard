import allure
from behave import *
import os
import common_util

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'the user Analyzes the traces for 5G Registration')
def analysing_traces_for_5G_registration(context):


    with allure.step(".     =====> ADB-Log Starts here <=========="):pass

    # filename  = str(os.path.join(str(os.getcwd()), str(caching.get_adbfilename()))).replace("\\","/")
    filename = common_util.adblogfilename('subA')

    patterns = {
        "[-->] REGISTER sip:gb.ee.rcs.telephony.goog SIP/2.0 [CSeq: 1 REGISTER]" : "sip_register_1",
        "[<--] SIP/2.0 401 Unauthorized [CSeq: 1 REGISTER]" :"SIP_401_1",
        "[-->] REGISTER sip:gb.ee.rcs.telephony.goog SIP/2.0 [CSeq: 2 REGISTER]" : "sip_register_2",
        "[-->] REGISTER sip:ims.mnc033.mcc234.3gppnetwork.org SIP/2.0 [CSeq: 1 REGISTER]" : "SIP_register_3",
        "[<--] SIP/2.0 200 OK [CSeq: 2 REGISTER]" : "SIP_200_OK_2",
        "[<--] SIP/2.0 401 Unauthorized" : "SIP_401_2",
        "[-->] REGISTER sip:ims.mnc033.mcc234.3gppnetwork.org SIP/2.0 [CSeq: 2 REGISTER]" : "SIP_register_4",
        "[<--] SIP/2.0 200 OK [CSeq: 2 REGISTER]" : "SIP_200_OK_3",
    }

    log.analyze_log(context, filename, patterns)

    with allure.step(".     =====> ADB-Log Ends here <==========\n"): pass

    with allure.step(".     =====> XCAL-Log Starts here <==========\n"): pass

    filename = common_util.get_XCAL_Filename()

    patterns = {
        "|Attach request": "XCAL_1",
        "|ESM information request": "XCAL_2",
        "|ESM information response": "XCAL_3",
        "|LTE securityModeCommand": "XCAL_4",
        "|LTE securityModeComplete": "XCAL_5",
        "|LTE ueCapabilityEnquiry": "XCAL_6",
        "|LTE ueCapabilityInformation": "XCAL_7",
        "|Attach accept": "XCAL_8",
        "|Attach complete": "XCAL_9",
        "|LTE rrcConnectionReconfiguration - [5G - NR RRC Data] RadiobearerConfig / [5G - NR RRC Data] RRCReconfiguration": "XCAL_10",
        "|LTE rrcConnectionReconfigurationComplete - [5G-NR RRC Data] RRCReconfigurationComplete": "XCAL_11"

    }

    log.XCAL_log(context, filename, patterns)

    with allure.step(".     =====> XCAL-Log Ends here <==========\n"): pass

@then(u'check if device has registrated to 5G')
def validating_5G_registered(context):

    try:
        if context.sip_register_1 and context.sip_register_2 and context.SIP_200_OK_3:
            with allure.step('IMS REGISTRATION:PASS'):
                pass
        else:
            with allure.step('IMS REGISTRATION:FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        assert False, "Test Failed"