# Created by svetlanalevinsohn at 4/27/19
Feature: HW2: Amazon tests

  Scenario: Prime page displays 4 benefits cards
    Given Open Amazon page
    When Click on 'Try Prime' from Amazon logo
    Then 4 prime benefits cards are shown

  Scenario: Ad feedback form can be opened
    Given Open Amazon page
    When Click on 'Ad feedback'
    Then Ad feedback form is opened

  Scenario: An item can be added to the cart
    Given Open page for product B077JFMVGP
    When Click Add to cart button
    Then Item has been added to the cart