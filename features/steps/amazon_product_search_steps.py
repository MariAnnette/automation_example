from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH, "//input[@type='submit' and @class='nav-input']")
RESULTS_INFO_BAR = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")

POPULAR_ITEMS = (By.CSS_SELECTOR, 'div#anonCarousel1 li')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@given('Open page for product {product_id}')
def open_amazon_product(context, product_id):
    context.driver.get('https://www.amazon.com/dp/{}'.format(product_id))


@when('Input {word} into Amazon search field')
def input_query(context, word):
    el = context.driver.find_element(*SEARCH_FIELD)
    el.clear()
    el.send_keys(word)


@when('Click on Amazon search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then('Amazon product results for {word} are shown')
def verify_result_present(context, word):
    assert word in context.driver.find_element(*RESULTS_INFO_BAR).text


@then('Verify 5 popular items are displayed')
def verify_popular_items(context):
    items = context.driver.find_elements(*POPULAR_ITEMS)
    print('\n', items)
    assert len(items) == 5, 'Expected items amount is 5, but get {}'.format(len(items))
