# Created by svetlanalevinsohn at 5/14/19
Feature: Tests using Actions
  # Enter feature description here

  Scenario: User can SignIn from Account&Lists nav link
    Given Open Amazon page
    When Hover over Account&Lists link
    And Click on Account&Lists SignIn btn
    Then Sign in page is opened