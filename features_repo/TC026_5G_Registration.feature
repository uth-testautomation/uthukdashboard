Feature: 5G Registration

  @5G @5GRegistration @Registration @all
  Scenario Outline: When user makes a 5G Registration Test
    Given the user wants to execute "5G_Registration" test case
    And the user wants to register the device "<subscriber_A>" on "<NetworkType>"
    Then the user disconnects from the network
    And starts capturing XCAL and adb logs
    Then connects to the network
    And then stops the XCAL log
    And then stop the adb logs
    Then the user Analyzes the traces for 5G Registration
    And check if device has registrated to 5G

    Examples:
      | NetworkType | subscriber_A |
