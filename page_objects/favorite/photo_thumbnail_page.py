import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import unittest
from page_objects.utility import Utility

class PhotoThumbnailPage(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_photo_thumbnail_is_displayed(self):
        favorite_photo_thumbnail = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView')
        unittest.TestCase.assertTrue(favorite_photo_thumbnail.is_displayed(), 'Favorite photo\'s thumbnail is not displayed')
        return self

    def assert_that_no_photo_thumbnails_are_displayed(self):
        no_photos_on_this_page_text = self.driver.find_elements(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="写真がありません。"]')
        unittest.TestCase.assertTrue(no_photos_on_this_page_text, 'Favorite photo\'s thumbnail is still displayed')
        return self

    def tap_top_left_photo_thumbnail(self):
        favorite_photo_thumbnail = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView')
        favorite_photo_thumbnail.click()
        time.sleep(3)
        return self

    def assert_that_download_photo_is_displayed(self):
        download_photo = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.google.android.apps.photos:id/video_player_controller_fragment_container"]')
        unittest.TestCase.assertTrue(download_photo.is_displayed(), 'Download photo is displayed')
        time.sleep(3)
        return self
