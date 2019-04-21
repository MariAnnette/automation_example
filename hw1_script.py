from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome('drivers/chromedriver')

# open the url
driver.get('https://www.amazon.com/')
driver.maximize_window()

# enter Help search phrase
driver.find_element(By.XPATH, "//a[contains(@href,'nav_cs_help')]").click()
el = driver.find_element(By.ID, 'helpsearch')
el.clear()
el.send_keys('Cancel order')

# click Go btn
driver.find_element(By.ID, 'helpSearchSubmit').click()

assert 'Cancel Items or Orders' == driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

driver.quit()