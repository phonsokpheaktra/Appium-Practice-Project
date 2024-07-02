import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.home.home_page import HomePage

class PhotoThumbnailPage(HomePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def tap_top_left_photo_thumbnail(self):
        img1 = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[1]')
        img1.click()
        time.sleep(2)
        return self

    def tap_download_photo(self):
        download_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="ダウンロード"]')
        download_btn.click()
        time.sleep(5)
        return self

    def tap_class_photo(self):
        class_photo_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc,"クラス写真")]')
        class_photo_btn.click()
        time.sleep(5)
        return self