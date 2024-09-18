Feature: VoLTE Call

@4G @4G_Call @VoLTECall @all
Scenario Outline:  When user makes a VoLTE Call Test

Given the user wants to execute "IMS_VoLTE_Call" test case
Then the user makes a call from "<subscriber_A>" to "<subscriber_B>"
And starts capturing XCAL and adb logs
Then the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
And user terminates the call from "subscriber_B" after "<Call-duration>" seconds
And then stops the XCAL log
And then stop the adb logs
Then the user analyze the VoLTE Call trace
And then the user validates the VoLTE logs

Examples:
| subscriber_A     |  subscriber_B   | Call-duration |
#|    07944532088   |  07581045780    |    10         |
#RFCR81KHXCY-07944531930 - M2
#RFCR81KKYTD-07581045780 - M1
#RFCR81KL0JT-07944532088 - M3
#| 07390059695                   |  07390059686                 |    10         |