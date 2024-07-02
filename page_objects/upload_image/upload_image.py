import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility


class UploadImage(Utility):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def click_storage(self):
        # tap sdk_gphone_x86 storage
        device_name_link = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="android:id/title" and @text="sdk_gphone_x86"]')
        device_name_link.is_displayed()
        device_name_link.click()
        time.sleep(5)
        return self

    def tap_pic_category(self):
        # tap Pictures category
        pictures_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="android:id/title" and @text="Pictures"]')
        pictures_btn.is_displayed()
        pictures_btn.click()
        time.sleep(5)
        return self

    def tap_pic_display_top_left(self):
        # tap picture displayed at top-left
        picture_thumbnail = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@resource-id="com.google.android.documentsui:id/icon_mime_lg"]')
        picture_thumbnail.is_displayed()
        picture_thumbnail.click()
        time.sleep(3)
        return self

