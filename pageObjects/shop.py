from selenium.webdriver.common.by import By
from pageObjects.checkOut import CheckOut
from utilities.BaseClass import BaseClass


class Shop:

    phoneCards = (By.XPATH, '//div[@class="card h-100"]')
    checkOutBtn = (By.XPATH, '//a[@class = "nav-link btn btn-primary"]')

    def __init__(self, driver):
        self.driver = driver

    def selectPhone(self, phoneSelected):
        phones = self.driver.find_elements(*Shop.phoneCards)
        for phone in phones:
            if phone.find_element_by_xpath('div/h4/a').text == phoneSelected:
                phone.find_element_by_xpath('div/button').click()


    def pressCheckOut(self):
        self.driver.find_element(*Shop.checkOutBtn).click()
        checkPage = CheckOut(self.driver)
        return checkPage

