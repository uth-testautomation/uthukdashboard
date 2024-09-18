Feature: User Busy

@4G @callBusy @all
Scenario Outline:  User gets busy tone when it is calling a subscriber who is on another call

    Given the user wants to execute "Call_Busy" test case
    And the user connects the devices "<subscriber_A>", "<subscriber_B>" and "<subscriber_C>" on the network
    Then starts capturing XCAL and adb logs
    And the user initiates the call from "<subscriber_A>" to "<subscriber_B>"
    Then the user initiates the call up from "subscriber_C" to "<subscriber_A>"
    Then user terminates the call from "subscriber_B" after "<Call_duration>" seconds
    And user terminates the call from "subscriber_C" after "<Call_duration>" seconds
    And then stops the XCAL log
    And then stop the adb logs
    And Analyze the traces for call busy
    Then validate the test Outcome for call busy

    Examples:
    | subscriber_A    |  subscriber_B   | subscriber_C | Call_duration |
#    | 07944531930     |  07581045780    |   07944532088 |	10         |

