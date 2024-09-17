Feature: Call Forward Unconditional

@4G @CFU @btdemo
Scenario Outline:  Call forwarding to third party when user enables unconditional forwarding

    Given the user wants to execute "Call_Forward_Unconditional" test case
    And the user connects the devices "<subscriber_A>", "<subscriber_B>" and "<subscriber_C>" on the network
    Then starts capturing XCAL and adb logs
    And the user "enables" call forwarding to "<subscriber_C>" by sending "<USSD_codes>" on "subscriber_B"
    Then the user initiates the call up from "subscriber_A" to "<subscriber_B>"
    Then the call gets forwarded to the "<subscriber_C>"
    Then "<subscriber_C>" answers the call and the call is established between "<subscriber_A>" and "<subscriber_C>"
    Then user terminates the call from "subscriber_A" after "<Call_duration>" seconds
    And the user "disables" call forwarding to "<subscriber_C>" by sending "<USSD_codes>" on "subscriber_B"
    And then stops the XCAL log
    And then stop the adb logs
    Then the user analyzes the call forward unconditional traces
    And then the CFU to third party traces are validated

    Examples:
    | subscriber_A    |  subscriber_B   | subscriber_C | Call_duration | USSD_codes |
#    | 07944531930     |  07581045780    |   07944532088| 10            | 21             |


    #RFCR81KHXCY-07944531930 - M2
    #RFCR81KKYTD-07581045780 - M1
    #RFCR81KL0JT-07944532088 - M3