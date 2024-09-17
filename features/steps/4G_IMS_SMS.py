import allure
from behave import *
import os
import common_util

from utils import log_analyzer as log
from utils.local_cache import Caching

caching = Caching()


@then(u'the user analyzes the SMS traces')
def analysing_traces_for_4G_IMS_sms(context):

    filename  = common_util.adblogfilename('subA')
    patterns = {
        "[-->] MESSAGE sip:": "invite_flag_1",
        "SIP/2.0 202 Accepted": "accept_flag_1",
        "[<--] MESSAGE sip:" : "invite_flag_2",
        "SIP/2.0 200 OK" : "accept_flag_2"
    }

    log.analyze_log(context, filename, patterns)

@then(u'validate the logs for the SMS test outcome')
def validation_of_log_for_4G_sms(context):
    try:
        if context.invite_flag_1 & context.accept_flag_1 & context.invite_flag_2 & context.accept_flag_2:
            with allure.step('VOLTE SMS:PASS'):
                pass
        else:
            with allure.step('VOLTE SMS:FAIL'):
                assert False, "Test Failed"
    except Exception as e:
        assert False, "Test Failed"