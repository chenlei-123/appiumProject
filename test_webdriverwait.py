import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestWebDriverWait():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]/*[@text='股票']").click()

        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        ele = self.driver.find_element(*locator)
        print(ele.text)
        current_price = float(ele.text)
        expected_price = 240
        # assert current_price > expected_price
        assert_that(current_price, close_to(expected_price, expected_price * 0.1))

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Make a Popup').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)
