Feature: Call Waiting

@4G @callWaiting @btdemo
Scenario Outline:  User gets notified about second call, when it is on call

    Given the user wants to execute "Call_Waiting" test case
    And the user connects the devices "<subscriber_A>", "<subscriber_B>" and "<subscriber_C>" on the network
    Then starts capturing XCAL and adb logs
    And then the user "enables" "call_waiting" on "subscriber_A" by dialing the "<USSD_codes>"
    And the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
    Then the user initiates the call up from "subscriber_C" to "<subscriber_A>"
    Then user terminates the call from "subscriber_B" after "<Call_duration>" seconds
    And user terminates the call from "subscriber_C" after "<Call_duration>" seconds
    And then the user "disables" "call_waiting" on "subscriber_A" by dialing the "<USSD_codes>"
    And then stops the XCAL log
    And then stop the adb logs
    And Analyze the traces for call waiting
    Then validate the test Outcome for call waiting

    Examples:
    | subscriber_A    |  subscriber_B   | subscriber_C | Call_duration | USSD_codes |
#    | 07944531930     |  07581045780    | 07944532088  | 10            |43          |