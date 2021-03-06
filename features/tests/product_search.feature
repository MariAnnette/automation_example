# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input dress into search field
#    And Click on search icon
#    Then Product results for dress are shown
#    And First result contains dress

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input dress into Amazon search field
    And Click on Amazon search icon
    Then Amazon product results for dress are shown

  Scenario: User can see 5 popular items upon search
    Given Open Amazon page
    When Input dress into Amazon search field
    And Click on Amazon search icon
    Then Verify 5 popular items are displayed
    