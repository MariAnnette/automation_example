# Created by svetlanalevinsohn at 5/14/19
Feature: HW4: Amazon tests
  # Enter feature description here

  Scenario Outline: User can select jeans colors
    Given Open page for product B07BKGC9V3
    Examples:
      |color          |
      |Rinse          |
      |Medium Wash    |
      |Dark Wash      |
    When Click on color <color>
    Then Color is updated to <color>

  Scenario: User can loop through dress colors
    Given Open page for product B07BKGC9V3
    Then Verify user can select jeans colors