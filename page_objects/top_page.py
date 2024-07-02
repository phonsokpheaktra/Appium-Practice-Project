import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility

class TopPage(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def switchLanguage(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Get Started"]').is_displayed()
        self.driver.swipe(574, 1356, 577, 797)
        time.sleep(2)
        language = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="日本語"]')
        language.click()
        time.sleep(2)
        return self

    def get_started(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="はじめる"]').click()
        time.sleep(2)
        return self
