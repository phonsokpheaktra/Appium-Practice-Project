import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from page_objects.utility import Utility


class AssertNameChangeSuccessfully(Utility):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver


    def assert_that_change_name_successfully(self):
        name_change_successfully = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="名前が正常に変更されました"]')
        unittest.TestCase.assertTrue(name_change_successfully.is_displayed(), 'Name has been changed successfully')
        time.sleep(5)
        self.driver.tap([(430, 1600)], 1)
        time.sleep(5)
        return self



