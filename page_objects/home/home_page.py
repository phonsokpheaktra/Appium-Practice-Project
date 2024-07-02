import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility
import unittest

class HomePage(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def logout(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="ログアウト"]').click()
        time.sleep(5)
        unittest.TestCase.assertTrue(self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="はじめる"]').is_displayed(), 'failed to logout: "はじめる" button is not displayed')
        return self
