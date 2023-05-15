Feature: Hotel Search
  Scenario: Extract hotel names from google search
    Given Indraja is on google homepage
    And   she opens the google maps link
    When  she searches for hotels
    Then  she saves the list of hotel names in the search result
#    Then she extract the hotel date and save it to a csv file
