Feature: Conference Calling

@5G @conferenceCall @btdemo
Scenario Outline:  When user makes a Conference Call Test

Given the user wants to execute "Conference_Call" test case
And the user connects the devices "<subscriber_A>", "<subscriber_B>" and "<subscriber_C>" on the network
Then starts capturing XCAL and adb logs
Then the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
And the user adds the other number to the call
Then the user initiates the third party call from "<subscriber_A>" to "<subscriber_C>"
Then the user merges the call
And user terminates the call from "subscriber_A" after "<Call-duration>" seconds
And then stops the XCAL log
And then stop the adb logs
#Then the user analyze the conference Call trace
#And then the user validates the conference call logs

Examples:
| subscriber_A     |  subscriber_B   | subscriber_C   | Call-duration |


|    07581045780   | 07944532088     |  07944531930   |    10         |
#RFCR81KHXCY-07944531930 - M2
#RFCR81KKYTD-07581045780 - M1
#RFCR81KL0JT-07944532088 - M3
#| 07390059695                   |  07390059686                 |    10         |
#| 07390059695                   |  123                         |    24         |