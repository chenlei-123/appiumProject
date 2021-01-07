import pytest
from appium import webdriver
from hamcrest import *


class TestGetAttr:
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
        pass

    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("text"))
        print(search_ele.get_attribute("checkable"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("bounds"))
        assert 'search' in search_ele.get_attribute("resource-id")

    @pytest.mark.skip
    def test_assert(self):
        a = 10
        b = 20
        assert a > b
        assert 'h' in 'this'  # 当上一个断言为false的时候，下面的断言不执行


