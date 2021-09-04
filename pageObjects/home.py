from selenium.webdriver.common.by import By
from pageObjects.shop import Shop
from selenium.webdriver.support.select import Select


class Home:

    shopButton = (By.CSS_SELECTOR, 'a[href*="shop"]')
    name = (By.CSS_SELECTOR, 'input[minlength="2"]')
    email = (By.NAME, 'email')
    password = (By.CSS_SELECTOR, '#exampleInputPassword1')
    checkice = (By.CSS_SELECTOR, '#exampleCheck1')
    gender = (By.CSS_SELECTOR, '#exampleFormControlSelect1')
    employments =(By.CSS_SELECTOR, 'div[class="form-group"] div')
    btncomplete = (By.CSS_SELECTOR, '.btn')

    def __init__(self, driver):
        self.driver = driver

    def clickShop(self):
        self.driver.find_element(*Home.shopButton).click()
        shopPage = Shop(self.driver)
        return shopPage

    def sendName(self):
        return self.driver.find_element(*Home.name)

    def sendEmail(self):
        return self.driver.find_element(*Home.email)

    def sendPassword(self):
        return self.driver.find_element(*Home.password)

    def checkIceBtn(self):
        return self.driver.find_element(*Home.checkice)

    def selectGender(self, gender):
        genders = Select(self.driver.find_element(*Home.gender))
        genders.select_by_visible_text(gender)
        return

    def selectEmployment(self, employ):
        empl = []
        for employment in self.driver.find_elements(*Home.employments):
            if employment.find_element_by_css_selector('label').text == employ:
                empl.append(employment.find_element_by_css_selector('label').text)
                employment.find_element_by_css_selector('input').click()
        assert len(empl) == 1 and empl[0] == employ


    def sendForm(self):
        return self.driver.find_element(*Home.btncomplete)






