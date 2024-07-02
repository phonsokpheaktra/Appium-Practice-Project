import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest

from page_objects.edit_name.edit_name import EditName
from page_objects.edit_name.edit_name_preview import AssertNameChangeSuccessfully
from page_objects.setting.setting_upload_image import UploadImageSetting
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage
from page_objects.login_page import LoginPage
from page_objects.home.home_page import HomePage

# Edit member information (Name)

class TestEditMemberInformation(unittest.TestCase):
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Pixel 2 API 30',
        'appPackage': 'com.irodoki.sckp_client_app.stg',
        'appActivity': 'com.irodoki.sckp_client_app.MainActivity'
    }
    url = "http://127.0.0.1:4723/wd/hub"
    driver: webdriver

    # as set-up process, launch driver
    def setUp(self):
        self.driver = webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.cap))
        time.sleep(5)

    def edit_member_information(self):
        TopPage(self.driver).switchLanguage().get_started()

        LoginMenuPage(self.driver).select_login()

        LoginPage(self.driver).login('sokpheaktra@kirirom-digital.com', 'Test123%')

        # tap setting icon
        UploadImageSetting(self.driver).Setting()

        EditName(self.driver).tap_edit_name_btn().tap_edit_name().edit_surname().edit_name().edit_surname_kata().edit_name_kata().change_name_btn()

        AssertNameChangeSuccessfully(self.driver).assert_that_change_name_successfully()

    def tearDown(self):
        EditName(self.driver).tap_edit_name().edit_surname_revert().edit_name_revert().edit_surname_kata_revert().edit_name_kata_revert().change_name_btn()

        AssertNameChangeSuccessfully(self.driver).assert_that_change_name_successfully().back_to_previous_page()

        HomePage(self.driver).open_home_page().logout()

if __name__ == '__main__':
    unittest.main()