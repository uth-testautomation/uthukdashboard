Feature: PS SMS

@4G @SMS @IMS @all @photosms
Scenario Outline:  When user makes a VoLTE SMS Test

    Given the user wants to execute "IMS_VoLTE_SMS" test case
    Then the user wants to sends a sms from "<subscriber_A>" to "<subscriber_B>"
    And starts capturing XCAL and adb logs
    Then the user sends an SMS attaching a photo from the camera
    And then stops the XCAL log
    And then stop the adb logs
    Then the user analyzes the SMS traces
    And validate the logs for the SMS test outcome

    Examples:
    | subscriber_A     |  subscriber_B   |
    |    07944532088   |  07581045780    |
