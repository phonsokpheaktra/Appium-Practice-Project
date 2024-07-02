import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import unittest
from page_objects.utility import Utility

class LoginMenuPage(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def select_login(self):
        login = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="ログイン"]')
        login.click()
        time.sleep(5)
        return self

    def login_unsuccessful(self):
        login = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="入力情報が正しくありません"]')
        unittest.TestCase.assertTrue(login.is_displayed(), 'Login Unsuccessful')
        return self

    def forgot_password(self):
        forgot_pw = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="ログインID/パスワードが不明な方"]')
        forgot_pw.click()
        time.sleep(5)
        return self
