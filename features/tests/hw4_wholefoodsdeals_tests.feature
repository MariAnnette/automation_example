# Created by svetlanalevinsohn at 5/14/19
Feature: HW4: Wholefoods deals tests

  Scenario: Every product on the page has a 'Regular' text and a product name
    Given Open Amazon /wholefoodsdeals page
    Then Every product on the page has 'Regular' text
    And Every product on the page has a product name
