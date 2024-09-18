Feature: Call Forward User Busy

@4G @CFB @all
Scenario Outline:  Call forwarding to third party when user is busy

    Given the user wants to execute "Call_Forward_When_Busy" test case
    And the user connects the devices "<subscriber_A>", "<subscriber_B>" and "<subscriber_C>" on the network
    Then starts capturing XCAL and adb logs
    And the user "enables" call forwarding to "<subscriber_C>" by sending "<USSD_codes>" on "subscriber_B"
    Then the user initiates the call up from "subscriber_B" to "123"
    Then the user initiates the call up from "subscriber_A" to "<subscriber_B>"
    Then the call gets forwarded to the "<subscriber_C>"
    Then "<subscriber_C>" answers the call and the call is established between "<subscriber_A>" and "<subscriber_C>"
    Then user terminates the call from "subscriber_A" after "<Call_duration>" seconds
    Then user terminates the call from "subscriber_B" after "1" seconds
    And the user "disables" call forwarding to "<subscriber_C>" by sending "<USSD_codes>" on "subscriber_B"
    And then stops the XCAL log
    And then stop the adb logs
    Then the user analyzes the call forward when busy traces
    And then the CFB to third party traces are validated

    Examples:
    | subscriber_A    |  subscriber_B   | subscriber_C | Call_duration |USSD_codes|
#    | 07944531930     |  07581045780    | 07944532088  | 10            | 67           |


    #RFCR81KHXCY-07944531930 - M2
    #RFCR81KKYTD-07581045780 - M1
    #RFCR81KL0JT-07944532088 - M3