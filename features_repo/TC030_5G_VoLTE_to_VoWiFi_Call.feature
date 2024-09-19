Feature: VoLTE-to-VoWiFi Calling

@5G @5G_Call @VoLTEtoVoWiFiCall @btdemo
Scenario Outline:  When user makes a 5G VoLTE to VoWiFi Call Test

Given the user wants to execute "5G_VoLTE_To_VoWiFi_Call" test case
Then the user makes a call from "<subscriber_A>" to "<subscriber_B>"
Then the user "enable" WiFi calling on "subscriber_B"
And starts capturing XCAL and adb logs
Then the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
And user terminates the call from "subscriber_B" after "<Call-duration>" seconds
And then stops the XCAL log
And then stop the adb logs
Then the user "disable" WiFi calling on "subscriber_B"
Then the user analyze the 5G VoLTE to VoWiFi Call trace
And then the user validates the VoLTE to VoWiFi logs

Examples:
| subscriber_A     |  subscriber_B   | Call-duration |
|    07944532088   |  07581045780    |    10         |
