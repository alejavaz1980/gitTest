from selenium import webdriver
from utilities.BaseClass import BaseClass
from pageObjects.home import Home
import time


class TestOne(BaseClass):

    def test_e2e1(self):
        log = self.getLogger()
        homepage = Home(self.driver)
        shoppage = homepage.clickShop()
        log.info("Get card titles")
        shoppage.selectPhone('Huawei')
        checkpage = shoppage.pressCheckOut()
        checkpage.clickCheckout().click()
        checkpage.findCountry().send_keys('uni')
        self.lookElement("United Kingdom")
        checkpage.selectCounty("United Kingdom")
        checkpage.clickAgreement().click()
        checkpage.clickPurchase().click()
        checkpage.validatePurchase()
