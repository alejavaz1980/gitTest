import time

import pytest

from utilities.BaseClass import BaseClass
from pageObjects.home import Home
from TestData.HomePageData import HomePageData


class TestTwo(BaseClass):

    def test_e2e2(self, getData):
        log = self.getLogger()
        homepage = Home(self.driver)
        log.info(f'Name provided: {getData["firstname"]}')
        homepage.sendName().send_keys(getData['firstname'])
        homepage.sendEmail().send_keys(getData['email'])
        homepage.sendPassword().send_keys(getData['password'])
        homepage.checkIceBtn().click()
        homepage.selectGender(getData['gender'])
        homepage.selectEmployment(getData['type'])
        homepage.sendForm().click()
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData('testcase2'))
    def getData(self, request):
        return request.param
