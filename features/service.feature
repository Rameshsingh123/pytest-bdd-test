
Feature: Simple api test

  Scenario Outline: Basic API Query
    Given the API is queried with "<phrase>"
    Then the response status code is "200"
    And the response contains results for "<phrase>"



    Examples:
      | phrase   |
      | entries   |


