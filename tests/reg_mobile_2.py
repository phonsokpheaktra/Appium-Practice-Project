import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage
from page_objects.login_page import LoginPage
from page_objects.home.home_page import HomePage

# Login using invalid ID/password

class TestLoginInvalid(unittest.TestCase):
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

    def test_login_homepage_unsuccessfully(self):
        TopPage(self.driver).switchLanguage().get_started()

        LoginMenuPage(self.driver).select_login()

        LoginPage(self.driver).login('sadopo2353_fake@agromgt.com', 'Test123%_fake')

        LoginMenuPage(self.driver).login_unsuccessful()


    # as tear-down process, back to Main screen of the app
    def tearDown(self):

        LoginPage(self.driver).unable_to_login()


if __name__ == '__main__':
    unittest.main()