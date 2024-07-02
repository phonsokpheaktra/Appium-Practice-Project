import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from page_objects.utility import Utility

class EditName(Utility):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def tap_edit_name_btn(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "会員情報")]').click()
        time.sleep(5)
        return self

    def tap_edit_name(self):
        edit_name_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[2]')
        edit_name_btn.is_displayed()
        edit_name_btn.click()
        time.sleep(5)
        return self

    def edit_surname(self):
        surname = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phon"]')
        surname.is_displayed()
        surname.click()
        time.sleep(2)
        surname.send_keys("Phon")
        time.sleep(5)
        return self

    def edit_name(self):
        name = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Sokpheak"]')
        name.is_displayed()
        name.click()
        time.sleep(2)
        name.send_keys("Hana")
        time.sleep(5)
        return self

    def edit_surname_kata(self):
        surname_kata = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="フォン"]')
        surname_kata.is_displayed()
        surname_kata.click()
        time.sleep(2)
        surname_kata.send_keys("x2")
        time.sleep(5)
        self.driver.swipe(511, 972, 603, 362)
        time.sleep(3)
        return self

    def edit_name_kata(self):
        name_kata = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="ソフェクトラ"]')
        name_kata.is_displayed()
        name_kata.click()
        time.sleep(5)
        name_kata.send_keys("x2")
        time.sleep(3)
        return self

    def change_name_btn(self):
        change_name_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="名前を変更する"]')
        change_name_btn.is_displayed()
        change_name_btn.click()
        time.sleep(5)
        return self

    def edit_surname_revert(self):
        surname = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="PhonPhon"]')
        surname.is_displayed()
        surname.click()
        time.sleep(2)
        surname.clear()
        time.sleep(2)
        surname.send_keys("Phon")
        time.sleep(5)
        return self

    def edit_name_revert(self):
        name = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="SokpheakHana"]')
        name.is_displayed()
        name.click()
        time.sleep(2)
        name.clear()
        time.sleep(2)
        name.send_keys("Sokpheak")
        time.sleep(5)
        return self

    def edit_surname_kata_revert(self):
        surname_kata = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="フォンx2"]')
        surname_kata.is_displayed()
        surname_kata.click()
        time.sleep(2)
        surname_kata.clear()
        time.sleep(2)
        surname_kata.send_keys("フォン")
        time.sleep(5)
        self.driver.swipe(511, 972, 603, 362)
        time.sleep(3)
        return self

    def edit_name_kata_revert(self):
        name_kata = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="ソフェクトラx2"]')
        name_kata.is_displayed()
        name_kata.click()
        time.sleep(5)
        name_kata.clear()
        time.sleep(2)
        name_kata.send_keys("ソフェクトラ")
        time.sleep(3)
        return self
