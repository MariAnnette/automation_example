from behave import then
from selenium.webdriver.common.by import By

# ======================================== HW1 LOCATORS ============================================

# AMAZON_LOGO = (By.XPATH, "//i[@class='a-icon a-icon-logo']")
# EMAIL_FIELD = (By.ID, 'ap_email')
# PASSWORD_FIELD = (By.ID, 'ap_password')
# FORGOT_PASSWORD_LINK = (By.ID, 'auth-fpp-link-bottom')
# SIGN_IN_BTN = (By.ID, 'signInSubmit')
# KEEP_SIGNED_CHECKBOX = (By.NAME, 'rememberMe')
# DETAILS_LINK = (By.ID, 'remember_me_learn_more_link')
# CREATE_ACCOUNT_BTN = (By.ID, 'createAccountSubmit')
# COU_LINK = (By.XPATH, "//a[contains(@href,'ap_desktop_footer_cou')]")
# PRIVACY_NOTICE_LINK = (By.XPATH, "//a[contains(@href,'ap_desktop_footer_privacy_notice')]")

# ======================================== HW2 LOCATORS ============================================

AMAZON_LOGO = (By.CSS_SELECTOR, "a.a-link-nav-icon")
EMAIL_FIELD = (By.ID, 'ap_email')
PASSWORD_FIELD = (By.ID, 'ap_password')
FORGOT_PASSWORD_LINK = (By.ID, 'auth-fpp-link-bottom')
SIGN_IN_BTN = (By.ID, 'signInSubmit')
KEEP_SIGNED_CHECKBOX = (By.CSS_SELECTOR, "input[name='rememberMe']")
DETAILS_LINK = (By.ID, 'remember_me_learn_more_link')
CREATE_ACCOUNT_BTN = (By.ID, 'createAccountSubmit')
COU_LINK = (By.CSS_SELECTOR, "a[href*='ap_desktop_footer_cou']")
PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "a[href*='ap_desktop_footer_privacy_notice']")

# ==================================================================================================

@then('Sign in page is opened')
def verify_on_sign_in(context):
    """
    Searches for unique elements of Sign In page to verify it is opened
    """
    context.driver.find_element(*EMAIL_FIELD)
    context.driver.find_element(*SIGN_IN_BTN)
