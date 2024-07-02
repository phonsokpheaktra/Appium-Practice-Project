import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from page_objects.home.home_page import HomePage

class PhotoPreviewPage(HomePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def set_photo_as_favorite(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "お気に入り")]').click()
        time.sleep(3)
        return self