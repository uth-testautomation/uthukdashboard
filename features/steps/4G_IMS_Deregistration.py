import allure
from behave import *
import os
import common_util

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()

@then(u'the user Analyzes the traces for 4G Deregistration')
def analysing_traces_for_4G_deregistration(context):

    with allure.step(".     =====> ADB-Log Starts here <=========="): pass

    filename = common_util.adblogfilename('subA')
    patterns = {
        "[-->] REGISTER": "sip_register_1",
        "[<--] SIP/2.0 200 OK": "SIP_200_OK_1",
        "[<--] NOTIFY si": "SIP_NOTIFY",
        "[-->] SIP/2.0 200 OK": "SIP_200_OK_2"
    }

    log.analyze_log(context, filename, patterns)
    with allure.step(".     =====> ADB-Log Ends here <==========\n"): pass

    with allure.step(".     =====> XCAL-Log Starts here <==========\n"): pass

    filename = common_util.get_XCAL_Filename()
    patterns = {
        "|Deactivate EPS bearer context request": "XCAL_1",
        "|Deactivate EPS bearer context accept": "XCAL_2",
        "|Detach request": "XCAL_3"
        # "Attach complete - Activate default EPS bearer context accept": "XCAL_4"
    }

    log.XCAL_log(context, filename, patterns)

    with allure.step(".     =====> XCAL-Log Ends here <==========\n"): pass


@then(u'check if device is Deregistrated from 4G')
def validating_4G_IMS_deregistered(context):
    try:
        if context.sip_register_1 & context.SIP_200_OK_1 & context.SIP_NOTIFY & context.SIP_200_OK_2:
            with allure.step('IMS DE REGISTRATION:PASS'):
                pass
        else:
            with allure.step('IMS DE REGISTRATION:FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        assert False, "Test Failed"