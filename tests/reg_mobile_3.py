import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest
from page_objects.home.home_page import HomePage
from page_objects.setting.setting_upload_image import UploadImageSetting
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage
from page_objects.login_page import LoginPage
from page_objects.upload_image.photo_preview_page import PhotoUploadPage
from page_objects.upload_image.upload_image import UploadImage

# Upload 参考画像 photo (training images)

class TestUploadImage(unittest.TestCase):
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

    def test_Upload_Image(self):
        TopPage(self.driver).switchLanguage().get_started()

        LoginMenuPage(self.driver).select_login()

        LoginPage(self.driver).login('sokpheaktra@kirirom-digital.com', 'Test123%')

        UploadImageSetting(self.driver).Setting().tap_child_info_btn().tap_student_icon().tap_add_traning_image_btn().tap_plus_icon().tap_hamburger_menu()

        # upload image from Google Photo
        UploadImage(self.driver).click_storage().tap_pic_category().tap_pic_display_top_left().save_btn_uploadImage().tap_your_pic_tab()

        PhotoUploadPage(self.driver).assert_that_photo_upload_is_displayed()

    def tearDown(self):
        UploadImageSetting(self.driver).tap_X_icon_on_the_photo().comfirm_btn_on_ModalWindow().back_to_previous_page().back_to_previous_page().back_to_previous_page()

        HomePage(self.driver).open_home_page().logout()

if __name__ == '__main__':
    unittest.main()


