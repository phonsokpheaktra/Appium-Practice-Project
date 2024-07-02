import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility

class PhotoPreviewPage(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def tap_favorite_button(self):
        favorite_button = self.driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "お気に入り")]')
        favorite_button.click()
        time.sleep(5)
        return self

    def back_to_previous_page(self):
        # back_icon = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button')
        # back_icon.click()
        self.driver.back()
        time.sleep(5)
        return self
