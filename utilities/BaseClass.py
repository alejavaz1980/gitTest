import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("config")
class BaseClass:

    def lookElement(self, text):
        wait = WebDriverWait(self.driver, 8)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, text)))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s : %(message)s')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        #if logger.hasHandlers():
        #    logger.handlers.clear()
        logger.setLevel(logging.DEBUG)
        return logger


