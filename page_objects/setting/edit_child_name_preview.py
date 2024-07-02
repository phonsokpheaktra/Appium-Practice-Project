import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility

class AssertChildNameChanged(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_child_name_change_successfully(self):
        change_successfully = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="お子様の名前は正常に変更されました"]')
        unittest.TestCase.assertTrue(change_successfully.is_displayed(), 'Child\'s name has been changed successfully')
        time.sleep(3)
        return self