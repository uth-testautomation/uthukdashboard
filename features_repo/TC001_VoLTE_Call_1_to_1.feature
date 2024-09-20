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
