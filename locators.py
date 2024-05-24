class RegisterPageLocators:
        CLICK_TO_REGISTER="//a[contains(text(),'Click to Create')]"
        USER_NAME="//input[@type='name']"
        USER_EMAIL="//input[@type='email' and @placeholder='Enter Email']"
        USER_MOBILE_NUMBER="//input[@type='mobileNumber' ]"
        PASSWORD_INPUT = "//input[@type='password']"
class LoginPageLocators:
        LOGIN_PAGE="//div//a[text()='Login']"
        USERNAME_INPUT = "//input[@placeholder='Enter Email or Mobile Number']"
        PASSWORD_INPUT = "//input[@type='password']"
        LOGIN_BUTTON = "//button[@value='login']"
#home page
class HomePageLocators:
        NAVBAR_TAG="//label[text()='%s']"

#update account 

#Place Order
class OrderPlaceLocators:
        PRODUCT_PAGE="//li//label[text()='Products']"
        ADD_MORE_ITEMS=""
        SELECT_BOOK="//h3[@class='product-heading' and text()='%s']"
        ADD_TO_CART="//span[text()='Add To Cart']"
        CHECKOUT_BUTTON="//button[@class='btn-checkout']"
        SELECT_ADDRESS="//input[@type='checkbox']"
        PROCESS_TO_PAYMENT="//div//a[@type='button']"
        PAYMENT_METHOD="//input[@id='Cash On Delivery']"
        CONFIRM_ORDER="//button[text()='Confirm Order']"
        ORDER_DETAILS="//input[@name='dateOfBirth']"




#Search Product
class SearchProduct:
        SEARCH_PRODUCT

#Browse Product
class BrowseProduct:
        SELECT_CATEGORY="//option[text()='%s']"
        SELECT_BRAND="//option[text()='%s']"
        SELECT_PRODUCT="//div[@class='card-body']//h3[text()='jdf']"




#AccountManagement

class AccountManagement:
        NAME="//input[@name='name']"
        DOB=""
        MOBILE_NUMBER="//input[@name='contact']"
        SELECT_GENDER="//option[@value='Male']"
        AlTERNATE_NUMBER="//input[@name='alternateNumber']"


#review 


#Admin Dashboard
class AdminBrandLocators:
        #add product
        ADD_BRAND_NAME="//input[@name='name']"
        # ADD_CATEGORY_NAME="//input[@name='categorySlug']"
        SHOW_IN_FRONT="//option[@value='%s']" #true/false
        ADD_BRAND_IMAGE="//input[@name='brand_image']"
        ADD_BRAND="//button[@type='submit']"
class AdminCategoryLocators:
        #add product
        ADD_CATEGORY_NAME="//input[@name='name']"
        # ADD_CATEGORY_NAME="//input[@name='categorySlug']"
        SHOW_IN_FRONT="//option[@value='%s']"
        ADD_CATEGORY_IMAGE="//input[@name='categoryImage']"
        ADD_CATEGORY="//button[@type='submit']"
        


class AdminProductLocators:
        PRODUCT_NAME="//input[@name='name']"
        SHOW_IN_FRONT="//option[text()='%s']"
        SELECT_BRAND="//option[text()='Wiley']"
        SLECT_CATEGORY="//option[text()='Autobiography']"
        PRODUCT_RATING="//option[@value='3']"
        TOTAL_PAGE="//input[@name='sizeVariation']"
        SELLER="//input[@name='seller']"
        PRODUCT_MRP="//input[@name='productMrp']"
        PRODUCT_PRICE="//input[@name='productPrice']"
        PRODUCT_AVAILABLE_QTY='//input[@name="availableQty"]'
        SMALL_DESCRIPTION="//textarea[@name='productSmallDescription']"
        PRODUCT_VIDEO="//input[@name='productVideo']"
        PRODUCT_DESCRIPTION="//textarea[@name='productDescription']"
        PRODUCT_IMAGE="//input[@type='file' and @name='productMainImage']"
        ADD_PRODUCT="//button[@type='submit']"


class AdminList:
        USER_LIST=""
        BRAND_LIST=""
        CATEGORY_LIST=""
        PRODUCT_LIST=""
        ORDER_LIST=""




 
        

        
