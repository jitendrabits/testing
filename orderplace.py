import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from locators import LoginPageLocators,HomePageLocators,OrderPlaceLocators
@pytest.fixture(scope="module")
def driver():
    # Initialize WebDriver
    global driver
    driver_path = ChromeDriverManager().install()
    # Extension Name
    extension_path = 'redux.crx'
    options = webdriver.ChromeOptions()
    options.add_extension(extension_path)

    # Driver Open
    s = ChromeService(driver_path)
    driver = webdriver.Chrome(service=s, options=options)

    yield driver
    # Teardown
    driver.quit()

@pytest.fixture(scope="function")
def selenium(driver,login_url):
    # Login
    driver.get(login_url)
    # driver.execute_script("document.body.style.zoom='90%'")

    time.sleep(5)
    login_page = driver.find_element(By.XPATH,LoginPageLocators.LOGIN_PAGE)
    login_page.click()
    username_input = driver.find_element(By.XPATH,LoginPageLocators.USERNAME_INPUT)
    username_input.clear()
    username_input.send_keys("admin@gmail.com")
    password_input = driver.find_element(By.XPATH,LoginPageLocators.PASSWORD_INPUT)
    password_input.clear()
    password_input.send_keys("admin")
    login_button = driver.find_element(By.XPATH,LoginPageLocators.LOGIN_BUTTON)
    login_button.click()

    driver.find_element(By.XPATH,OrderPlaceLocators.PRODUCT_PAGE).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.SELECT_BOOK).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.PRODUCT_PAGE).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.ADD_TO_CART).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.CHECKOUT_BUTTON).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.SELECT_ADDRESS).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.PROCESS_TO_PAYMENT).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.PAYMENT_METHOD).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.CONFIRM_ORDER).click()
    driver.find_element(By.XPATH,OrderPlaceLocators.ORDER_DETAILS).click()





    

    time.sleep(2)
    driver.refresh()
    homepage_header = driver.find_element(By.XPATH,HomePageLocators.USER_NAME)
    assert "admin" in homepage_header.text
    yield driver

def test_check_all_modules_available(selenium):
    assert "Home" in selenium.find_element(By.XPATH,HomePageLocators.NAVBAR_TAG).text
    assert "Products" in selenium.find_element(By.XPATH,HomePageLocators.NAVBAR_TAG).text
    assert "Search" in selenium.find_element(By.XPATH,HomePageLocators.NAVBAR_TAG).text
   
 