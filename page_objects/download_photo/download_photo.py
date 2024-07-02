import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.utility import Utility


class DownloadPhotoPreviewPage(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def get_started_btn(self):
        get_started_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.google.android.apps.photos:id/onboarding_action_button"]')
        get_started_btn.click()
        time.sleep(5)
        return self

    def tap_library(self):
        library_folder_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.google.android.apps.photos:id/tab_library"]')
        library_folder_btn.click()
        time.sleep(5)
        return self

    def click_on_cover_photo(self):
        cover_pic_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.google.android.apps.photos:id/album_cover_view"]')
        cover_pic_btn.click()
        time.sleep(5)
        self.driver.tap([(142,694)],1)
        time.sleep(5)
        return self


