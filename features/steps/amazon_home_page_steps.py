from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

HELP_LINK = (By.XPATH, "//a[contains(@href,'nav_cs_help')]")
ORDERS_LINK = (By.ID, "nav-orders")

HAMBURGER_MENU = (By.ID, 'nav-hamburger-menu')
SHOP_BY_CATEGORY = (By.XPATH, "//ul[@class='hmenu  hmenu-visible']/li[1]/div[@class='hmenu-item hmenu-title']")
HAMBURGER_MENU_X = (By.XPATH, "//div[@class='nav-sprite hmenu-close-icon']")
LOGO_TRY_PRIME_LINK = (By.XPATH, "//div[@id='nav-logo']/a[contains(@href, 'prime')]")
TRY_PRIME_CTA_BTN = (By.ID, 'prime-header-CTA')
PRIME_BENEFITS_CARDS = (By.CSS_SELECTOR, 'div#prime-benefit-cards div.card-category')

AD_FEEDBACK = (By.ID, 'ad-feedback-text-right-2')
SEND_FEEDBACK_BTN = (By.ID, 'da-feedback-send-feedback-button')

ADD_CART_BTN = (By.ID, 'add-to-cart-button')
CART_CONFIRM_TEXT = (By.ID, 'confirm-text')
CART_COUNT = (By.ID, 'nav-cart-count')
CART = (By.ID, 'nav-cart')
CART_EMPTY_HEADER = (By.CSS_SELECTOR ,'div.sc-cart-header h1')


@given('Click on Orders navigation link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()


@given('Click on Help navigation link')
def click_help_link(context):
    context.driver.find_element(*HELP_LINK).click()


@when('Click Hamburger menu icon')
def click_hamburger_menu(context):
    context.driver.find_element(*HAMBURGER_MENU).click()


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART).click()


@then("'Shop by category' text is present")
def verify_shop_category_txt(context):
    assert 'SHOP BY CATEGORY' == context.driver.find_element(*SHOP_BY_CATEGORY).text


@when('Click on closing X of the side menu')
def click_x(context):
    context.driver.find_element(*HAMBURGER_MENU_X).click()
    context.driver.wait.until(EC.invisibility_of_element_located(HAMBURGER_MENU_X))


@when("Click on 'Try Prime' from Amazon logo")
def click_try_prime(context):
    context.driver.wait.until(EC.element_to_be_clickable(LOGO_TRY_PRIME_LINK))
    context.driver.find_element(*LOGO_TRY_PRIME_LINK).click()


@when("Click on 'Ad feedback'")
def click_ad_feedback(context):
    context.driver.find_element(*AD_FEEDBACK).click()


@when('Click Add to cart button')
def add_to_cart(context):
    context.driver.find_element(*ADD_CART_BTN).click()


@then('Amazon Prime page is opened')
def verify_on_prime_page(context):
    context.driver.find_element(*TRY_PRIME_CTA_BTN)


@then('{amount} prime benefits cards are shown')
def verify_prime_benefits_cards(context, amount):
    benefits_cards = context.driver.find_elements(*PRIME_BENEFITS_CARDS)
    # print(type(amount))
    assert len(benefits_cards) == int(amount), 'Expected 4 prime benefits cards but got {}'.format(len(benefits_cards))


@then('Ad feedback form is opened')
def verify_ad_feedback_opened(context):
    context.driver.wait.until(EC.visibility_of_element_located(AD_FEEDBACK))


@then('Item has been added to the cart')
def verify_item_added(context):
    context.driver.wait.until(EC.presence_of_element_located(CART_CONFIRM_TEXT))
    assert context.driver.find_element(*CART_COUNT).text == '1'


@then("Verify '{expected_text}' text present")
def verify_cart_empty_text(context, expected_text):
    assert expected_text == context.driver.wait.until(EC.presence_of_element_located(CART_EMPTY_HEADER)).text