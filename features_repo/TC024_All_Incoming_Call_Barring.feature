Feature: All Incoming Calls Barring

@4G @BaringIncomingCall @all
Scenario Outline:  All incoming calls are barred for user

    Given the user wants to execute "All_incoming_calls_bared" test case
    Then the user connects the devices "<subscriber_A>" and "<subscriber_B>" to the network
    Then starts capturing XCAL and adb logs
    And then the user "enables" "baring_incoming_call" on "subscriber_B" by dialing the "<USSD_Code>"
    Then the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
    And the call is not established and gets disconnected after announcement 
    And then the user "disables" "baring_incoming_call" on "subscriber_B" by dialing the "<USSD_Code>"
    And then stops the XCAL log
    And then stop the adb logs
    Then the user analyzes the baring incoming call traces
    And then validate the baring the incoming call traces

    Examples:
    | subscriber_A    |  subscriber_B   | USSD_Code |
#    | 07944531930     |  07581045780    | 35       |