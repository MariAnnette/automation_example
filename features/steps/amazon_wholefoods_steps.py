from behave import then
from selenium.webdriver.common.by import By

ALL_PRODUCTS = (By.CSS_SELECTOR, 'div.a-text-center li.s-result-item')
PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name.a-text-bold')


@then("Every product on the page has 'Regular' text")
def verify_regular_text(context):
    products = context.driver.find_elements(*ALL_PRODUCTS)
    for product in products:
        print('\nChecking:', product.text)
        assert 'Regular ' in product.text, "Expected 'Regular $' to be in product test, but got {}".format(product.text)


@then("Every product on the page has a product name")
def verify_product_name(context):
    """
    Finds ALL Product elements and searches for a name element inside each product element

    Example:
    # Get a product's element, it has html =>
    product1_element = context.driver.find_elements(*ALL_PRODUCTS)[1]
    print(product1_element)
    html = product1_element.get_attribute('innerHTML')
    print(html)
    # Search inside product1_element:
    name = product1_element.find_element(*PRODUCT_NAME)
    print('\n', name.text)

    """
    products = context.driver.find_elements(*ALL_PRODUCTS)
    for product in products:
        print('\nProduct element: ', product)
        product.find_element(*PRODUCT_NAME)
