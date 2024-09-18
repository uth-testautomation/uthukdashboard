Feature: All Outgoing Calls Barring

@4G @BaringOutgoingCall @all
Scenario Outline:  Outgoing calls are barred for user

    Given the user wants to execute "All_outgoing_calls_bared" test case
    Then the user connects the devices "<subscriber_A>" and "<subscriber_B>" to the network
    Then starts capturing XCAL and adb logs
    And then the user "enables" "baring_outgoing_call" on "subscriber_A" by dialing the "<USSD_Code>"
    Then the user initiates the call up from "<subscriber_A>" to "<subscriber_B>"
    And the call is not established and gets disconnected after announcement 
    And then the user "disables" "baring_outgoing_call" on "subscriber_A" by dialing the "<USSD_Code>"
    And then stops the XCAL log
    And then stop the adb logs
    Then the user analyzes the baring outgoing call traces
    And then validate the baring the outgoing call traces

    Examples:
    | subscriber_A    |  subscriber_B   | USSD_Code |
#    | 07581045780     |  07944531930    | 33        |

    #RFCR81KHXCY-07944531930 - M2
    #RFCR81KKYTD-07581045780 - M1
    #RFCR81KL0JT-07944532088 - M3