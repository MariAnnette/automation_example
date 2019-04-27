# Created by svetlanalevinsohn at 4/20/19
Feature: DEMO: Amazon tests

  Scenario: Search Help returns correct result
    Given Open Amazon page
    And Click on Help navigation link
    When Search help for Cancel order
    Then Search result Cancel Items or Orders is shown

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    And Click on Orders navigation link
    Then Sign in page is opened

  Scenario: Hamburger menu can be opened and closed
    Given Open Amazon page
    When Click Hamburger menu icon
    Then 'Shop by category' text is present
    When Click on closing X of the side menu
    And Click on 'Try Prime' from Amazon logo
    Then Amazon Prime page is opened