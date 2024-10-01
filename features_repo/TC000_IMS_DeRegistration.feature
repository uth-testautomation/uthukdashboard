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
And check if device is Deregistrated from 5G

Examples:
| NetworkType | subscriber_A |
#|          4G |  07944532088 |

#RFCR81KHXCY-07944531930 - M2
#RFCR81KKYTD-07581045780 - M1
#RFCR81KL0JT-07944532088 - M3