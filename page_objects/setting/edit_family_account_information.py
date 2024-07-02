import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import unittest
from page_objects.utility import Utility

class EditFamilyAccountInformation(Utility):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.driver = driver

    def tap_family_account_information(self):
        tap_family_account = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="家族を招待する"]')
        tap_family_account.is_displayed()
        tap_family_account.click()
        time.sleep(5)
        return self

    def add_family_account(self):
        add_family_acc = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="家族を追加"]')
        add_family_acc.is_displayed()
        add_family_acc.click()
        time.sleep(5)
        return self

    def tap_on_relationship(self):
        relationship = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="続柄"]')
        relationship.is_displayed()
        relationship.click()
        time.sleep(5)
        return self

    def select_mother(self):
        relationship_mom = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="ママ"]')
        relationship_mom.is_displayed()
        relationship_mom.click()
        time.sleep(5)
        return self

    def click_on_lastname(self):
        lastname = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[1]')
        lastname.is_displayed()
        lastname.click()
        time.sleep(3)
        lastname.send_keys('Mom')
        time.sleep(5)
        return self

    def click_on_firstname(self):
        firstname = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[2]')
        firstname.is_displayed()
        firstname.click()
        time.sleep(3)
        firstname.send_keys('Mother')
        time.sleep(5)
        self.driver.swipe(979,880,990,500)
        return self

    def click_on_lastnameKana(self):
        lastname_kana = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[2]')
        lastname_kana.is_displayed()
        lastname_kana.click()
        time.sleep(3)
        lastname_kana.send_keys('お母')
        time.sleep(5)
        return self

    def click_on_firstnameKana(self):
        click_on_firstnameKana = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[3]')
        click_on_firstnameKana.is_displayed()
        click_on_firstnameKana.click()
        time.sleep(3)
        click_on_firstnameKana.send_keys('さん')
        time.sleep(5)
        return self

    def click_on_email(self):
        self.driver.swipe(504,753,537,416)
        time.sleep(5)
        click_on_email = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[2]')
        click_on_email.is_displayed()
        click_on_email.click()
        time.sleep(3)
        click_on_email.send_keys('mother@gmail.com')
        time.sleep(5)
        return self

    def send_invite_mail(self):
        send_invite_mail = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="招待コードを送信"]')
        send_invite_mail.is_displayed()
        send_invite_mail.click()
        time.sleep(5)
        return self

    def click_mother_invitation(self):
        mother_invitation = self.driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "Mom Mother")]')
        mother_invitation.is_displayed()
        mother_invitation.click()
        time.sleep(5)
        return self

    def delete_account_btn(self):
        delete = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="削除"]')
        delete.is_displayed()
        delete.click()
        time.sleep(5)
        return self

    def input_password(self):
        input_password = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText')
        input_password.is_displayed()
        input_password.click()
        time.sleep(3)
        input_password.send_keys('Test123%')
        time.sleep(5)
        return self

    def delete(self):
        delete = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="確認する"]')
        delete.is_displayed()
        delete.click()
        time.sleep(5)
        return self

    def assert_that_account_invitation_deleted_successfully(self):
        delete = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="このアカウントは現在削除されています。ユーザーはアクセスできなくなります。"]')
        unittest.TestCase.assertTrue(delete.is_displayed, 'Invitation account has been deleted successfully')
        time.sleep(5)
        return self


