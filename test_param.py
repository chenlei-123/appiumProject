import time
import hamcrest
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


class Test_Param:
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
        pass

    @pytest.mark.parametrize('searchkey,type,price', [
        ('阿里巴巴', 'BABA', 240),
        ('小米集团-W', '01810', 33)
    ])
    def test_search(self, searchkey, type, price):
        """
        1、打开雪球应用
        2、点击搜索框
        3、输入搜索词 'alibaba' or 'xiaomi'...
        4、点击第一个搜索结果
        5、判断 股票价格
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element_by_xpath(
            f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{searchkey}']").click()
        expect_price = price
        current_price = float(self.driver.find_element(MobileBy.XPATH,
                                                       f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(current_price)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
        self.driver.back()
