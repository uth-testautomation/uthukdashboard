Feature: EPS Fallback

@5G @5G_Call @VoNRCall @all
Scenario Outline:  When user makes a 5G VoNR Call Test

Given the user wants to execute "5G_VoNR_Call" test case
Then the user makes a call from "<subscriber_A>" to "<subscriber_B>"
And starts capturing XCAL and adb logs
Then the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
And user terminates the call from "subscriber_B" after "<Call-duration>" seconds
And then stops the XCAL log
And then stop the adb logs
Then the user analyze the 5G Call trace
And then the user validates the logs

Examples:
| subscriber_A     |  subscriber_B   | Call-duration |
