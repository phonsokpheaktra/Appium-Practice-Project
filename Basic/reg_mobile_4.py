import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy

# Set a student photo as favorite photo

cap:Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Pixel 2 API 30',
    'appPackage': 'com.irodoki.sckp_client_app.stg',
    'appActivity': 'com.irodoki.sckp_client_app.MainActivity'
}

url = "http://127.0.0.1:4723/wd/hub"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
time.sleep(2)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Get Started"]').is_displayed()
driver.swipe(574, 1356,577, 797)

language = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='日本語')
language.click()
time.sleep(2)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="はじめる"]').click()
time.sleep(2)

login = driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="ログイン"]')
login.click()

time.sleep(2)
login_id = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.widget.EditText[1]')
login_id.click()
time.sleep(2)
login_id.send_keys("rijihi5174@acuxi.com")

login_pw = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.widget.EditText[2]')
login_pw.click()
time.sleep(2)
login_pw.send_keys('Test123%')

login1 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="ログイン"]')
login1.is_enabled()
login1.click()
time.sleep(5)

img1 = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View/android.view.View/android.widget.ImageView[1]')
img1.click()
time.sleep(2)
driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "お気に入り")]').click()
driver.back()

fav_btn: WebElement = driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@content-desc, "お気に入り")]')
fav_btn.is_displayed()
fav_btn.click()