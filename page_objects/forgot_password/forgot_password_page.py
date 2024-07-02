import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys
from page_objects.utility import Utility
import re

class ForgotPassword(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def click_on_search_gmail(self, mail):
        search_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.google.android.googlequicksearchbox:id/googleapp_search_box"]')
        time.sleep(5)
        search_btn.send_keys(mail)
        time.sleep(5)
        self.driver.press_keycode(66)
        time.sleep(10)
        return self

    def accept_continue(self):
        accept = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.android.chrome:id/terms_accept"]')
        accept.click()
        time.sleep(5)
        return self

    def yes_in(self):
        self.driver.find_element(by=AppiumBy.XPATH,value='//*[@resource-id="com.android.chrome:id/positive_button"]').click()
        time.sleep(5)
        return self

    def select_gmail(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.android.chrome:id/recycler_view"]/android.widget.LinearLayout[1]/android.widget.LinearLayout').click()
        time.sleep(5)
        return self

    def gmail(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(5)
        return self


    def click_searchBar(self):
        self.driver.tap([(278,544)], 1)
        time.sleep(5)
        return self


    def code_verification_code_in_Gmail(self):
        code = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Unread. イロドキ サポート 【サクラクレパス イロドキ】パスワードの再設定用確認コードの送信"]')
        code.click()
        time.sleep(5)
        return self

    def get_verify_code(self):
        paragraph_text = self.driver.find_element(by=AppiumBy.XPATH, value="//*[(@bounds='[49,1548][1031,1609]')]")
        verification_code = paragraph_text.text
        time.sleep(3)
        print(f"The text of the element is: {verification_code}")
        return self

    def paste_verification_code(self, verification_code):
        input_code = self.driver.find_element(by=AppiumBy, value='//*[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]')
        input_code.click()
        time.sleep(5)
        input_code.send_keys(verification_code)
        time.sleep(5)
        return self

    def gmail_for_forgetPassword(self, user_gmail):
        gmail = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
        gmail.click()
        time.sleep(3)
        gmail.send_keys(user_gmail)
        time.sleep(5)
        return self

    def confirm_button(self):
        confirm_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="確認"]')
        confirm_btn.click()
        time.sleep(5)
        return self