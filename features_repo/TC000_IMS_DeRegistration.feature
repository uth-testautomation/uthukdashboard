Feature: IMS De-registration

@volte @4G @IMS @Deregistration @all
Scenario Outline:  When user makes a IMS DeRegistration Test

Given the user wants to execute "4G_IMS_Deregistration" test case
And the user wants to register the device "<subscriber_A>" on "<NetworkType>"
Then starts capturing XCAL and adb logs
Then the user disconnects from the network
And then stops the XCAL log
And then stop the adb logs
Then connects to the network
Then the user Analyzes the traces for 4G Deregistration
And check if device is Deregistrated from 4G

Examples:
| NetworkType | subscriber_A |
