import allure
from behave import *
import os
import common_util

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()

@then(u'the user Analyzes the traces for 4G Registration')
def analysing_traces_for_4G_registration(context):

    with allure.step(".     =====> ADB-Log Starts here <=========="):pass

    filename = common_util.adblogfilename('subA')
    patterns = {
        "[-->] REGISTER sip:ims.mnc033.mcc234.3gppnetwork.org SIP/2.0 [CSeq: 1 REGISTER]": "sip_register_1",
        "[<--] SIP/2.0 401 Unauthorized [CSeq: 1 REGISTER]": "SIP_200_OK_1",
        "[-->] REGISTER sip:ims.mnc033.mcc234.3gppnetwork.org SIP/2.0 [CSeq: 2 REGISTER]": "sip_register_2",
        "[<--] SIP/2.0 200 OK [CSeq: 2 REGISTER]": "SIP_200_OK_2"
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
        "|Attach complete": "XCAL_9"
    }

    log.XCAL_log(context, filename, patterns)

    with allure.step(".     =====> XCAL-Log Ends here <==========\n"): pass


@then(u'check if device has registrated to 4G')
def validating_4G_IMS_registered(context):

    try:
        if context.sip_register_1 and context.SIP_200_OK_1 and context.sip_register_2 and context.SIP_200_OK_2:
            with allure.step('IMS REGISTRATION:PASS'):
                pass
        else:
            with allure.step('IMS REGISTRATION:FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        assert False, "Test Failed"