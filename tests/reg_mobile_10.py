import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest
from page_objects.home.home_page import HomePage
from page_objects.setting.edit_family_account_information import EditFamilyAccountInformation
from page_objects.setting.setting_upload_image import UploadImageSetting
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage
from page_objects.login_page import LoginPage

# Edit Family Account information (invite family account)

class TestEditFamilyAccount(unittest.TestCase):
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

    def test_edit_family_account_information(self):
        TopPage(self.driver).switchLanguage().get_started()

        LoginMenuPage(self.driver).select_login()

        LoginPage(self.driver).login('sokpheaktra@kirirom-digital.com', 'Test123%')

        UploadImageSetting(self.driver).Setting()

        EditFamilyAccountInformation(self.driver).tap_family_account_information().add_family_account().tap_on_relationship().select_mother().click_on_lastname().click_on_firstname()

        EditFamilyAccountInformation(self.driver).click_on_lastnameKana().click_on_firstnameKana().click_on_email().send_invite_mail()


    def tearDown(self):
        EditFamilyAccountInformation(self.driver).click_mother_invitation().delete_account_btn().input_password().delete()

        EditFamilyAccountInformation(self.driver).assert_that_account_invitation_deleted_successfully()

        EditFamilyAccountInformation(self.driver).back_btn().back_to_previous_page()

        HomePage(self.driver).open_home_page().logout()

if __name__ == '__main__':
    unittest.main()

