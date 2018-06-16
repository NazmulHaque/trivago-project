Feature: Featured Article

  Scenario: User can see featured article in home page
    When user go to home page
    Then user can see featured article in the top of the page
    And user can see "Read More" button
    When user click on the "Read More" button
    Then loads article details page
