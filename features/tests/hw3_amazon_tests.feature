# Created by svetlanalevinsohn at 5/8/19
Feature: HW3: Amazon test
  # Enter feature description here

  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Shopping Cart is empty.' text present