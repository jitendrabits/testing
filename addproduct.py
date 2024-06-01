# Import
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
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
from locators import LoginPageLocators,HomePageLocators,AdminCategoryLocators,AdminList,AdminProductLocators,AdminBrandLocators


# Download Chromedriver
driver_path = ChromeDriverManager().install()

# Extension Name
extension_path = 'redux.crx'
options = webdriver.ChromeOptions()
options.add_extension(extension_path)

# Driver Open
s = ChromeService(driver_path)
driver = webdriver.Chrome(service=s, options=options)
email="//input[@name='email']"
pwd="//input[@name='password']"
btn="//button[text()='Login']"
# extension_page = 'http://localhost:3002'
extension_page = 'https://admin-lilac-five.vercel.app'

time.sleep(5)
driver.get(extension_page)
driver.maximize_window()

 
username_input = driver.find_element(By.XPATH,email)
username_input.clear()
username_input.send_keys("admin@gmail.com")
password_input = driver.find_element(By.XPATH,pwd)
password_input.clear()
password_input.send_keys("Test@123")
login_button = driver.find_element(By.XPATH,btn)
login_button.click()
time.sleep(5)
# driver.get("http://localhost:3002/products")
# dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='showHide']")))
# dropdown.click()
# yes="//option[text()='Yes']"

# driver.find_element(By.XPATH,"//input[@name='name']").send_keys("jitendra")
DIR="C:/devops-bookstore/bookstore/booksimg/cook.jpg"

def addBrand():
    driver.get("https://admin-lilac-five.vercel.app/brands")
    driver.find_element(By.XPATH, AdminBrandLocators.ADD_BRAND_NAME).send_keys("brandtest")
    front = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//select[@name='show_hide']")))
    front.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, AdminBrandLocators.SHOW_IN_FRONT % str("true")))).click()
    driver.find_element(By.XPATH,AdminBrandLocators.ADD_BRAND_IMAGE).send_keys(DIR)
    driver.find_element(By.XPATH,AdminBrandLocators.ADD_BRAND).click()


def addCategory():
    driver.get("https://admin-lilac-five.vercel.app/categorys")
    driver.find_element(By.XPATH, AdminCategoryLocators.ADD_CATEGORY_NAME).send_keys("categorytest")
    front = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//select[@name='showHide']")))
    front.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, AdminCategoryLocators.SHOW_IN_FRONT % str("true")))).click()
    driver.find_element(By.XPATH,AdminCategoryLocators.ADD_CATEGORY_IMAGE).send_keys(DIR)
    driver.find_element(By.XPATH,AdminCategoryLocators.ADD_CATEGORY).click()
    print("done")





def addproduct():
    driver.get("https://admin-lilac-five.vercel.app/products")
    driver.find_element(By.XPATH, AdminProductLocators.PRODUCT_NAME).send_keys("productA")
    front = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='showHide']")))
    front.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, AdminProductLocators.SHOW_IN_FRONT % str("Yes")))).click()

    brand = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='brand']")))
    brand.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, AdminProductLocators.SELECT_BRAND ))).click()

    category = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='category']")))
    category.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, AdminProductLocators.SLECT_CATEGORY ))).click()

    rating = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='rating']")))
    rating.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, AdminProductLocators.PRODUCT_RATING ))).click()

    driver.find_element(By.XPATH,AdminProductLocators.TOTAL_PAGE).send_keys("200")
    driver.find_element(By.XPATH,AdminProductLocators.SELLER).send_keys("Bookstore")
    driver.find_element(By.XPATH,AdminProductLocators.PRODUCT_MRP).send_keys("299")
    driver.find_element(By.XPATH,AdminProductLocators.PRODUCT_PRICE).send_keys("199")
    driver.find_element(By.XPATH,AdminProductLocators.PRODUCT_AVAILABLE_QTY).send_keys("39")
    driver.find_element(By.XPATH,AdminProductLocators.SMALL_DESCRIPTION).send_keys("Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since")
    driver.find_element(By.XPATH,AdminProductLocators.PRODUCT_VIDEO).send_keys("abc.com")
    driver.find_element(By.XPATH,AdminProductLocators.PRODUCT_DESCRIPTION).send_keys("Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever sinceIpsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since")
    driver.find_element(By.XPATH,AdminProductLocators.PRODUCT_IMAGE).send_keys(DIR)
    time.sleep(1)
    driver.find_element(By.XPATH,AdminProductLocators.ADD_PRODUCT).click()




table_data = []

def orderlist():
    driver.get("https://admin-lilac-five.vercel.app/orders/list")
    table = driver.find_element(By.CLASS_NAME, "table-md")

    rows = table.find_elements(By.XPATH, "//tbody/tr")

    table_data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        
        row_data = []
        
        for cell in cells:
            row_data.append(cell.text)
        
        table_data.append(row_data)

print(table_data,"table")




addBrand()
# addCategory()
# addproduct()
# orderlist()

# time.sleep(500)
driver.quit()