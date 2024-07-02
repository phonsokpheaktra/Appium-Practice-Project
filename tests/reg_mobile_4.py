import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage
from page_objects.login_page import LoginPage
from page_objects.home.student_photo.photo_thumbnail_page import PhotoThumbnailPage as StudentPhotoThumbnailPage
from page_objects.home.student_photo.photo_preview_page import PhotoPreviewPage as StudentPhotoPreviewPage
from page_objects.favorite.photo_thumbnail_page import PhotoThumbnailPage as FavoritePhotoThumbnailPage
from page_objects.favorite.photo_preview_page import PhotoPreviewPage as FavoritePhotoPreviewPage
from page_objects.home.home_page import HomePage

# Set a student photo as favorite photo

class TestFavoriteFeature(unittest.TestCase):
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

    def test_set_a_student_photo_as_favorite_photo(self):
        TopPage(self.driver).switchLanguage().get_started()

        LoginMenuPage(self.driver).select_login()

        LoginPage(self.driver).login('sokpheaktra@kirirom-digital.com', 'Test123%')

        StudentPhotoThumbnailPage(self.driver).tap_top_left_photo_thumbnail()

        StudentPhotoPreviewPage(self.driver).set_photo_as_favorite().back_to_previous_page().open_favorite_page()

        FavoritePhotoThumbnailPage(self.driver).assert_that_photo_thumbnail_is_displayed()

    # as tear-down process, remove the photo from Favorite page
    def tearDown(self):
        FavoritePhotoThumbnailPage(self.driver).tap_top_left_photo_thumbnail()

        FavoritePhotoPreviewPage(self.driver).tap_favorite_button().back_to_previous_page()

        FavoritePhotoThumbnailPage(self.driver).assert_that_no_photo_thumbnails_are_displayed().open_home_page()

        HomePage(self.driver).logout()

if __name__ == '__main__':
    unittest.main()
