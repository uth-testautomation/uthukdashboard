Feature: IMS Registration

@volte @4G @Registration @all
Scenario Outline:  When user makes a IMS Registration Test
Given the user wants to execute "4G_IMS_Registration" test case
And the user wants to register the device "<subscriber_A>" on "<NetworkType>"
Then the user disconnects from the network
And starts capturing XCAL and adb logs
Then connects to the network
And then stops the XCAL log
And then stop the adb logs
Then the user Analyzes the traces for 4G Registration
And check if device has registrated to 4G

Examples:
| NetworkType | subscriber_A |
|          4G |  07581045780 |