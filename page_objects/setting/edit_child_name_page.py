import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility

class EditChildName(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def edit_child_name_btn(self):
        edit_child_name = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[2]')
        edit_child_name.is_displayed()
        edit_child_name.click()
        time.sleep(5)
        return self

    def click_edit_child_name_btn(self):
        tap_edit_child_name_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Name"]')
        tap_edit_child_name_btn.is_displayed()
        tap_edit_child_name_btn.click()
        time.sleep(3)
        tap_edit_child_name_btn.send_keys('x2')
        time.sleep(5)
        return self

    def click_edit_child_name_btn_revert(self):
        tap_edit_child_name_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Namex2"]')
        tap_edit_child_name_btn.is_displayed()
        tap_edit_child_name_btn.click()
        time.sleep(2)
        tap_edit_child_name_btn.clear()
        time.sleep(2)
        tap_edit_child_name_btn.send_keys('Name')
        time.sleep(5)
        return self

    def change_child_name(self):
        change_child_name = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="確認する"]')
        change_child_name.is_displayed()
        change_child_name.click()
        time.sleep(5)
        return self