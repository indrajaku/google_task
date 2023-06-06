Feature: Fetch Hotel Details
  Scenario: Search for hotels in a nearby loaction and retrieve their details
    Given Indraja opens google search and searchs for google maps
    When she clicks on the google maps link
    And she searches for the hotels in Bangalore
    And she retrieves the details of the 5 hotels
    Then she saves the hotel names