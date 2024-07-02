from appium.webdriver import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility


class ResetPassword(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def click_forget_password(self):
        forgot_pw = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="ログインID/パスワードが不明な方"]')
        forgot_pw.is_displayed()
        forgot_pw.click()
        time.sleep(5)
        return self

    def input_new_password(self):
        new_pw = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
        new_pw.is_enabled()
        new_pw.click()
        time.sleep(3)
        new_pw.send_keys('Test123')
        time.sleep(5)
        return self

    def confirm_new_password(self):
        new_pw = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="確認"]')
        new_pw.is_clickable()
        new_pw.click()
        time.sleep(5)
        return self