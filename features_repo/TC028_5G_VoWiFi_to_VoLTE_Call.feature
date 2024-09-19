Feature: VoWiFi-to-VoLTE Calling

@5G @5G_Call @VoWiFitoVoLTECall @btdemo
Scenario Outline:  When user makes a 5G VoWiFi to VoLTE Call Test

Given the user wants to execute "5G_VoWiFi_To_VoLTE_Call" test case
Then the user makes a call from "<subscriber_A>" to "<subscriber_B>"
Then the user "enable" WiFi calling on "subscriber_A"
And starts capturing XCAL and adb logs
Then the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
And user terminates the call from "subscriber_B" after "<Call-duration>" seconds
And then stops the XCAL log
And then stop the adb logs
Then the user "disable" WiFi calling on "subscriber_A"
Then the user analyze the 5G VoWiFi to VoLTE Call trace
And then the user validates the VoWiFi to VoLTE logs

Examples:
| subscriber_A     |  subscriber_B   | Call-duration |
|    07944532088   |  07581045780    |    10         |