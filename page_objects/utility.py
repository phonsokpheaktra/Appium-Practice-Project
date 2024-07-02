import time
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
import unittest


class Utility():
    def __init__(self, driver: webdriver):
        self.driver = driver

    def back_to_previous_page(self):
        time.sleep(5)
        self.driver.back()
        return self

    def open_favorite_page(self):
        fav_btn: WebElement = self.driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "お気に入り")]')
        unittest.TestCase.assertTrue(fav_btn.is_displayed(), '"お気に入り" icon is not displayed')
        fav_btn.click()
        time.sleep(5)
        return self

    def open_home_page(self):
        home_icon = self.driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "ホーム")]')
        home_icon.click()
        time.sleep(5)
        return self

    def save_btn_uploadImage(self):
        # tap Save button
        save_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Save"]')
        save_btn.is_displayed()
        save_btn.click()
        time.sleep(5)
        return self

    def tap_your_pic_tab(self):
        # tap Your pictures tab
        existing_training_photo_tab = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[contains(@content-desc, "過去に登録した写真")]')
        existing_training_photo_tab.is_displayed()
        existing_training_photo_tab.click()
        time.sleep(5)
        return self


    def tap_next_btn(self):
        next_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.google.android.apps.photos:id/welcomescreens_next_button"]')
        next_btn.click()
        time.sleep(2)
        next_btn.click()
        time.sleep(2)
        next_btn.click()
        time.sleep(2)
        return self

    def tap_delete_photo_btn(self):
        delete_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Delete"]')
        delete_btn.click()
        time.sleep(5)
        return self

    def view_photo(self):
        got_it_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]')
        got_it_btn.click()
        time.sleep(5)
        return self

    def delete_download_photo(self):
        move_to_trash = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@resource-id="com.google.android.apps.photos:id/move_to_trash"]')
        move_to_trash.click()
        time.sleep(2)
        self.driver.press_keycode(3)
        self.driver.quit()
        return self

    def back_btn(self):
        # back_btn = self.driver.find_element(by=AppiumBy, value='//*[contains(@content-desc, "戻る")]')
        self.driver.tap([(460,1111)],1)
        time.sleep(5)
        return self




