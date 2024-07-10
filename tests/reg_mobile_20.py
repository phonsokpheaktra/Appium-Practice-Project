import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage
from page_objects.login_page import LoginPage
import threading
from page_objects.home.home_page import HomePage

# Login using valid ID/password

class TestLoginValid(unittest.TestCase):
    def setUp(self):
        self.device_lock = threading.Lock()

        device1: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Pixel 2 API 30',
        'udid': 'emulator-5554',
        'port': 'http://localhost:4728/wd/hub',
        'appPackage': 'com.irodoki.sckp_client_app.stg',
        'appActivity': 'com.irodoki.sckp_client_app.MainActivity'
        }
        self.driver1 = webdriver.Remote("http://localhost:4728/wd/hub", options=AppiumOptions().load_capabilities(device1))
        time.sleep(5)

        device2: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Second Pixel 2 API 30',
        'udid': 'emulator-5556',
        'port': 'http://localhost:4723/wd/hub',
        'appPackage': 'com.irodoki.sckp_client_app.stg',
        'appActivity': 'com.irodoki.sckp_client_app.MainActivity'
        }
        self.driver2 = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(device2))
        time.sleep(5)

    # as set-up process, launch driver

    def test_login(self):
        thread1 = threading.Thread(target=self.login_on_device1)
        thread2 = threading.Thread(target=self.login_on_device2)

        thread1.start()
        time.sleep(5)
        thread2.start()

        thread1.join()
        time.sleep(5)
        thread2.join()

    def login_on_device1(self):
        TopPage(self.driver1).switchLanguage().get_started()

        LoginMenuPage(self.driver1).select_login()

        LoginPage(self.driver1).login('sokpheaktra@kirirom-digital.com', 'Test123%')

        HomePage(self.driver1).logout()

        self.driver1.quit()

    def login_on_device2(self):

        TopPage(self.driver2).switchLanguage().get_started()

        LoginMenuPage(self.driver2).select_login()

        LoginPage(self.driver2).login('sokpheaktra@kirirom-digital.com', 'Test123%')

        HomePage(self.driver2).logout()

        self.driver2.quit()


if __name__ == '__main__':
    unittest.main()
