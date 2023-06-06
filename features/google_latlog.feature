Feature: Retrieve latitude and longitude from google map
  Scenario Outline: get the latitude and longitude from google map
   Given Indraja is on the google search page
   When she searches for "<company>"
    And she sees the company card
   Then she retrieves the latitude and logitude

  Examples:
  |company|
  |actualize|











