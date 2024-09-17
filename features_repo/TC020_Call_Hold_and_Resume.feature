Feature: Call Hold and Resume

@4G @CallnResume @btdemo
Scenario Outline:  User can put ongoing call on hold and resume it

    Given the user wants to execute "Call_Hold_and_Resume" test case
    Then the user connects the devices "<subscriber_A>" and "<subscriber_B>" to the network
    Then starts capturing XCAL and adb logs
    And the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
    Then "<subscriber_A>" holds the call for "<Call_duration>" and then resumes it
    Then user terminates the call from "subscriber_A" after "1" seconds
    And then stops the XCAL log
    And then stop the adb logs
    And Analyze the traces for call hold and resume
    Then validate the test Outcome for call hold and resume

    Examples:
    | subscriber_A    |  subscriber_B   | Call_duration |
#    | 07944531930     |  07581045780    | 10            |


    #RFCR81KHXCY-07944531930 - M2
    #RFCR81KKYTD-07581045780 - M1
    #RFCR81KL0JT-07944532088 - M3