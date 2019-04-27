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


@given('Click on Orders navigation link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()


@given('Click on Help navigation link')
def click_help_link(context):
    context.driver.find_element(*HELP_LINK).click()


@when('Click Hamburger menu icon')
def click_hamburger_menu(context):
    context.driver.find_element(*HAMBURGER_MENU).click()


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


@then('Amazon Prime page is opened')
def verify_on_prime_page(context):
    context.driver.find_element(*TRY_PRIME_CTA_BTN)
