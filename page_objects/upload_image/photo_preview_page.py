from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import unittest
from page_objects.utility import Utility

class PhotoUploadPage(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver


    def assert_that_photo_upload_is_displayed(self):
        favorite_photo_thumbnail = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView')
        unittest.TestCase.assertTrue(favorite_photo_thumbnail.is_displayed(), 'Upload Photo is displayed')
        return self



