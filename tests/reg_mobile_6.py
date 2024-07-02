import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest
from page_objects.download_photo.download_photo import DownloadPhotoPreviewPage
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage
from page_objects.login_page import LoginPage
from page_objects.home.student_photo.photo_thumbnail_page import PhotoThumbnailPage as StudentPhotoThumbnailPage
from page_objects.favorite.photo_thumbnail_page import PhotoThumbnailPage
from page_objects.home.home_page import HomePage

# Set a student photo as favorite photo

class TestStudentAsFavoritePhoto(unittest.TestCase):
    irodoki: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Pixel 2 API 30',
        'appPackage': 'com.irodoki.sckp_client_app.stg',
        'appActivity': 'com.irodoki.sckp_client_app.MainActivity'
    }

    photos: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Pixel 2 API 30',
        'appPackage': 'com.google.android.apps.photos',
        'appActivity': 'com.google.android.apps.photos.home.HomeActivity'
    }



    url = "http://127.0.0.1:4723/wd/hub"
    driver: webdriver

    # as set-up process, launch driver
    def setUp(self):
        self.driver = webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.irodoki))
        time.sleep(5)

    def test_favorite_photo(self):
        TopPage(self.driver).switchLanguage().get_started()

        LoginMenuPage(self.driver).select_login()

        LoginPage(self.driver).login('sokpheaktra@kirirom-digital.com', 'Test123%')

        StudentPhotoThumbnailPage(self.driver).tap_top_left_photo_thumbnail().tap_download_photo().back_to_previous_page()

        HomePage(self.driver).logout()

        #  Open Photos App
        self.driver = webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.photos))
        time.sleep(5)

        DownloadPhotoPreviewPage(self.driver).get_started_btn().tap_next_btn().tap_library().click_on_cover_photo()

        PhotoThumbnailPage(self.driver).assert_that_download_photo_is_displayed()

        DownloadPhotoPreviewPage(self.driver).tap_delete_photo_btn().view_photo()
    def tearDown(self):
        DownloadPhotoPreviewPage(self.driver).delete_download_photo()

if __name__ == '__main__':
    unittest.main()
