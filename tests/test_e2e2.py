import time

import pytest

from utilities.BaseClass import BaseClass
from pageObjects.home import Home


class TestTwo(BaseClass):

    def test_e2e2(self, getData):
        homepage = Home(self.driver)
        homepage.sendName().send_keys(getData[0])
        homepage.sendEmail().send_keys(getData[1])
        homepage.sendPassword().send_keys(getData[2])
        homepage.checkIceBtn().click()
        homepage.selectGender(getData[3])
        homepage.selectEmployment(getData[4])
        homepage.sendForm().click()
        self.driver.refresh()

    @pytest.fixture(params=[('Alex', 'a_vazquez_d@yahoo.com', '12345', 'Male', 'Student'),
                            ('Alma', 'almad@yahoo.com', '67890', 'Female', 'Employed'),
                            ('Hector', 'hector@yahoo.com', '85795', 'Male', 'Student')])
    def getData(self, request):
        return request.param
