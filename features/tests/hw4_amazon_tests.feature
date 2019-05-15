# Created by svetlanalevinsohn at 5/14/19
Feature: HW4: Amazon tests
  # Enter feature description here

  Background:
    Given Open page for product B07BKGC9V3

  Scenario Outline: User can select jeans colors
    Examples:
      |color          |
      |Rinse          |
      |Medium Wash    |
      |Dark Wash      |
    When Click on color <color>
    Then Color is updated to <color>

  Scenario: User can loop through jeans colors
    Then Verify user can select jeans colors