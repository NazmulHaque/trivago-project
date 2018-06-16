Feature: Newsletter subscription

  Scenario: User subscribe for newsletter
    Given user is in home page
    When scroll to subscription section
    Then user type email in the input box
    And tick the checkbox to receive newsletters
    When click on submit button
    Then user can see successful message
