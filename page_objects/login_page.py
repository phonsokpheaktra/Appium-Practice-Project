import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility

class LoginPage(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def login(self, user_id: str, password: str):
        login_id = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.widget.EditText[1]')
        login_id.click()
        time.sleep(3)
        login_id.send_keys(user_id)

        login_pw = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.widget.EditText[2]')
        login_pw.click()
        time.sleep(3)
        login_pw.send_keys(password)

        login1 = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="ログイン"]')
        login1.is_enabled()
        login1.click()
        time.sleep(6)
        return self

    def unable_to_login(self):
        self.driver.tap([(504, 475)], 1)
        time.sleep(5)
        dismiss_msg = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button')
        dismiss_msg.click()
        return self

