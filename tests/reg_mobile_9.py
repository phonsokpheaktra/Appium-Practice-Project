import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest
from page_objects.home.home_page import HomePage
from page_objects.setting.edit_child_name_page import EditChildName
from page_objects.setting.edit_child_name_preview import AssertChildNameChanged
from page_objects.setting.setting_upload_image import UploadImageSetting
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage
from page_objects.login_page import LoginPage

# Edit child information (Dsiplay Name)

class TestEditChildInformation(unittest.TestCase):
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Pixel 2 API 30',
        'appPackage': 'com.irodoki.sckp_client_app.stg',
        'appActivity': 'com.irodoki.sckp_client_app.MainActivity'
    }
    url = "http://127.0.0.1:4723/wd/hub"
    driver: webdriver

    def setUp(self):
        self.driver = webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.cap))
        time.sleep(5)

    def test_change_child_name(self):
        TopPage(self.driver).switchLanguage().get_started()

        LoginMenuPage(self.driver).select_login()

        LoginPage(self.driver).login('sokpheaktra@kirirom-digital.com', 'Test123%')

        UploadImageSetting(self.driver).Setting().tap_child_info_btn().tap_student_icon()

        EditChildName(self.driver).edit_child_name_btn().click_edit_child_name_btn().change_child_name()

        AssertChildNameChanged(self.driver).assert_that_child_name_change_successfully()

        EditChildName(self.driver).change_child_name()


    def tearDown(self):
        EditChildName(self.driver).edit_child_name_btn().click_edit_child_name_btn_revert().change_child_name()

        AssertChildNameChanged(self.driver).assert_that_child_name_change_successfully()

        EditChildName(self.driver).change_child_name().back_to_previous_page().back_to_previous_page()

        HomePage(self.driver).open_home_page().logout()

if __name__ == '__main__':
    unittest.main()


