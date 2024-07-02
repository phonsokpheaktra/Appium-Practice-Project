import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
import unittest
from page_objects.forgot_password.forgot_password_page import ForgotPassword
from page_objects.login_page import LoginPage
from page_objects.top_page import TopPage
from page_objects.login_menu_page import LoginMenuPage

# Reset Password

class TestEditFamilyAccount(unittest.TestCase):
    irodoki: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Pixel 2 API 30',
        'appPackage': 'com.irodoki.sckp_client_app.stg',
        'appActivity': 'com.irodoki.sckp_client_app.MainActivity'
    }

    gmail: Dict[str, Any] = {
        "platformName": "android",
        "appium:platformVersion": "11",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Pixel 2 API 30",
        "appium:appPackage": "com.google.android.googlequicksearchbox",
        "appium:appActivity": "com.google.android.googlequicksearchbox.SearchActivity"
    }

    url = "http://127.0.0.1:4723/wd/hub"
    driver: webdriver

    def setUp(self):
        self.driver = webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.irodoki))
        time.sleep(5)

    def test_edit_family_account_information(self):
        TopPage(self.driver).switchLanguage().get_started()

        LoginMenuPage(self.driver).select_login()

        LoginMenuPage(self.driver).forgot_password()

        ForgotPassword(self.driver).gmail_for_forgetPassword('sokpheaktra@kirirom-digital.com').confirm_button()

        self.driver = webdriver.Remote(self.url, options=AppiumOptions().load_capabilities(self.gmail))
        time.sleep(10)

        ForgotPassword(self.driver).click_searchBar()

        ForgotPassword(self.driver).click_on_search_gmail('mail.google.com')

        ForgotPassword(self.driver).code_verification_code_in_Gmail()

        ForgotPassword(self.driver).get_verify_code()

        verification_code = ForgotPassword(self.driver).get_verify_code()

        self.driver.activate_app("com.irodoki.sckp_client_app.stg")
        time.sleep(5)

        ForgotPassword(self.driver).paste_verification_code(verification_code)

    # def tearDown(self):

        # HomePage(self.driver).open_home_page().logout()

if __name__ == '__main__':
    unittest.main()
