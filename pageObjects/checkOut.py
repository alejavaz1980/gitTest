from selenium.webdriver.common.by import By


class CheckOut:

    checkButton = (By.CSS_SELECTOR, 'button[class*="btn btn-success"]')
    country = (By.ID, 'country')
    countries = (By.CSS_SELECTOR, 'div[class*="suggestions"]')
    agreements = (By.CSS_SELECTOR, 'div[class="checkbox checkbox-primary"]')
    purchaseBtn = (By.CSS_SELECTOR, 'input[class="btn btn-success btn-lg"]')
    successP = (By.XPATH, '//strong[text()="Success!"]')

    def __init__(self, driver):
        self.driver = driver

    def clickCheckout(self):
        return self.driver.find_element(*CheckOut.checkButton)

    def findCountry(self):
        return self.driver.find_element(*CheckOut.country)

    def selectCounty(self, location):
        countries = self.driver.find_elements(*CheckOut.countries)
        for country in countries:
            if country.find_element_by_link_text(location):
                country.click()

    def clickAgreement(self):
        return self.driver.find_element(*CheckOut.agreements)

    def clickPurchase(self):
        return self.driver.find_element(*CheckOut.purchaseBtn)

    def validatePurchase(self):
        message = "Success!"
        assert self.driver.find_element(*CheckOut.successP).text == "Nel"


