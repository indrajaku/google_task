Feature: Hotel Search
  Scenario: Search for nearby hotels  and extract data
    Given Indraja on google homepage search for google maps
    When  she click on google maps link
    Then  she search for hotels,extract the hotel and save the hotel names
#    Then she extract the hotel date and save it to a csv file
