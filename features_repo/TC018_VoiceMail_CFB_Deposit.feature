Feature: Voice Mail CFB

@4G @CFBVM @VM @all
Scenario Outline:  Call forwarding to Voicemail when user is busy

    Given the user wants to execute "Call_Forward_To_VoiceMail_When_Busy" test case
    Then the user connects the devices "<subscriber_A>" and "<subscriber_B>" to the network
    Then starts capturing XCAL and adb logs
    And the user "enables" call forwarding to "<VoiceMail>" by sending "<USSD_codes>" on "subscriber_B"
    Then the user initiates the call up from "subscriber_B" to "123"
    Then the user initiates the call up from "subscriber_A" to "<subscriber_B>"
    Then the call gets forwarded to the "VoiceMail"
    Then user terminates the call from "subscriber_A" after "<Call_duration>" seconds
    Then user terminates the call from "subscriber_B" after "1" seconds
    And the user "disables" call forwarding to "<VoiceMail>" by sending "<USSD_codes>" on "subscriber_B"
    And then stops the XCAL log
    And then stop the adb logs
    Then the user analyzes the call forward to Voice Mail when busy traces
    And then the CFB to Voice Mail is validated

    Examples:
    | subscriber_A    |  subscriber_B   |   VoiceMail  | Call_duration |USSD_codes|
#    | 07944531930     |  07581045780    |  07953222222 | 40            | 67       |


    #RFCR81KHXCY-07944531930 - M2
    #RFCR81KKYTD-07581045780 - M1
    #RFCR81KL0JT-07944532088 - M3