Feature: Voice Mail CFNA

@4G @VM @CFNAVM @btdemo
Scenario Outline:  Voice mail deposit when user doesnt answer

    Given the user wants to execute "Call_Forward_To_VM_When_Not_Answered" test case
    Then the user connects the devices "<subscriber_A>" and "<subscriber_B>" to the network
    Then starts capturing XCAL and adb logs
    And the user "enables" call forwarding to "<VoiceMail>" by sending "<USSD_codes>" on "subscriber_B"
    Then the user initiates the call up from "subscriber_A" to "<subscriber_B>"
    Then the call gets forwarded to the "VoiceMail"
    Then user terminates the call from "subscriber_A" after "<Call_duration>" seconds
    And the user "disables" call forwarding to "<VoiceMail>" by sending "<USSD_codes>" on "subscriber_B"
    And then stops the XCAL log
    And then stop the adb logs
    Then the user analyzes the call forward not answered to Voice Mail traces
    And then the CFNA to Voice Mail is validated

    Examples:
    | subscriber_A    |  subscriber_B   | Call_duration |USSD_codes| VoiceMail  |
#    | 07944531930     |  07581045780    | 10            | 61       |07953222222 |



    #RFCR81KHXCY-07944531930 - M2
    #RFCR81KKYTD-07581045780 - M1
    #RFCR81KL0JT-07944532088 - M3