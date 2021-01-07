import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Test_DW():
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
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        print("搜索测试用例")
        """
        1、打开雪球app
        2、点击搜索输入框
        3、想搜索输入框里面输入"阿里巴巴"
        4、在搜索结果里面选择"阿里巴巴"，然后进行点击
        5、获取这只上香港 阿里巴巴的股价，并判断这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    # @pytest.mark.skip
    def test_get_attr(self):
        """
        打开雪球应用首页
        定位首页的搜索框
        判断搜索框的是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入：alibaba
        判断 【阿里巴巴】是否需可见
        如果可见，打印搜索功能点击，如果不可见，打印搜索失败
        :return:
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        print(element.is_enabled())
        search_enable = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enable == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # alibaba_element.is_displayed()
            print(alibaba_element.get_attribute("displayed"))
            element_displayed = alibaba_element.get_attribute("displayed")
            if element_displayed == "true":
                print("搜做成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect["width"]
        height = window_rect["height"]
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).move_to(x=x1, y=y_end).release().perform()
        time.sleep(4)

    def test_touchaction_1(self):
        print("解锁手势密码")
        TouchAction(self.driver).press(x=244, y=374).wait(100).move_to(x=711, y=374).wait(100).move_to(x=1198,
                                                                                                       y=384).wait(
            100).move_to(x=1198, y=1323).wait(100).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        print(self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)

    def test_myinfo(self):
        """
        1、打开雪球，
        2、点击我的，
        3、点击登录，输入用户名密码
        4、点击登录
        :return:
        """
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")')

        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("12345")
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()


if __name__ == '__main__':
    pytest.main()
