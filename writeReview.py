import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from locators import LoginPageLocators,HomePageLocators,BrowseProduct
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
    driver.maximize_window()
    driver.get(login_url)
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL, '-')

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
    time.sleep(2)
    driver.refresh()
    driver.find_element(By.XPATH,HomePageLocators.NAVBAR_TAG%str('Products')).click()
    category = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[3]/div[2]/form/div/select[1]")))
    category.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, BrowseProduct.SELECT_CATEGORY % str("cooking")))).click()
    brand = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div[3]/div[2]/form/div/select[2]")))
    brand.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, BrowseProduct.SELECT_CATEGORY % str("Wiley")))).click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, BrowseProduct.SELECT_CATEGORY % str("class-button")))).click()
    
    driver.find_element(By.XPATH,BrowseProduct.SELECT_PRODUCT).click()
    yield driver

def test_check_all_modules_available(selenium):
    assert "Home" in selenium.find_element(By.XPATH,HomePageLocators.NAVBAR_TAG%str('Home')).text
    assert "Products" in selenium.find_element(By.XPATH,HomePageLocators.NAVBAR_TAG%str('Products')).text
    assert "Search" in selenium.find_element(By.XPATH,HomePageLocators.NAVBAR_TAG%str('Search')).text
    assert "Search" in selenium.find_element(By.XPATH,HomePageLocators.NAVBAR_TAG%str('CLICK')).text
   
 
