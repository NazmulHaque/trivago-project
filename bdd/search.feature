Feature: Search in trivago

  Scenario: User search for hotel in Canada
    Given user is in home page
    When click on search icon
    Then search box appears
    And user types Canada in the search box
    When press ENTER
    Then user can see search results for Canada location only

