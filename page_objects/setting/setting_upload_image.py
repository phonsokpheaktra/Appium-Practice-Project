import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from page_objects.utility import Utility


class UploadImageSetting(Utility):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver


    def Setting(self):
        # tap setting icon
        setting_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "設定")]')
        setting_btn.is_displayed()
        setting_btn.click()
        time.sleep(5)
        return self


    def tap_child_info_btn(self):
        # tap Child information button
        student_information_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="お子さま情報"]')
        student_information_btn.is_displayed()
        student_information_btn.click()
        time.sleep(5)
        return self

    def tap_add_traning_image_btn(self):
        # tap Add training images button
        add_training_photo_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="参考画像を追加する"]')
        add_training_photo_btn.is_displayed()
        add_training_photo_btn.click()
        time.sleep(5)
        return self

    def tap_student_icon(self):
        # tap student's icon
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
        x = 75
        y = 296
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(5)
        return self

    def tap_plus_icon(self):
        # tap "+" icon
        add_training_photo_icon = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
        add_training_photo_icon.is_displayed()
        add_training_photo_icon.click()
        time.sleep(5)
        return self

    def tap_hamburger_menu(self):
        # tap hamburger menu
        hamburger_menu_icon = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Show roots"]')
        hamburger_menu_icon.is_displayed()
        hamburger_menu_icon.click()
        time.sleep(5)
        return self

    def tap_X_icon_on_the_photo(self):
        # tap X icon on the photo
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
        x = 350
        y = 1020
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(5)
        return self

    def comfirm_btn_on_ModalWindow(self):
        # tap confirmation button on the modal window
        confirmation_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="確認する"]')
        confirmation_btn.is_displayed()
        confirmation_btn.click()
        time.sleep(5)
        return self


