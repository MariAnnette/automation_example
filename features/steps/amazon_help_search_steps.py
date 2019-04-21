from behave import when, then
from selenium.webdriver.common.by import By

HELP_SEARCH_FIELD = (By.ID, 'helpsearch')
HELP_SEARCH_GO = (By.ID, 'helpSearchSubmit')
SEARCH_RESULT_HEADER = (By.XPATH, "//div[@class='help-content']/h1")


@when('Search help for {search_phrase}')
def search_help(context, search_phrase):
    el = context.driver.find_element(*HELP_SEARCH_FIELD)
    el.clear()
    el.send_keys(search_phrase)
    context.driver.find_element(*HELP_SEARCH_GO).click()


@then('Search result {expected_result} is shown')
def verify_search_help_result(context, expected_result):
    assert expected_result == context.driver.find_element(*SEARCH_RESULT_HEADER).text