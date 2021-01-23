import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Add_Contact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '84681e49'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        # 不清空本地缓存
        desired_caps['noReset'] = 'true'
        desired_caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间为0秒
        desired_caps['settings[waitForIdleTimeout]'] = 0
        desired_caps['unicodeKeyBoard'] = 'true'
        # 设置页面空闲状态为0秒
        desired_caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown(self):
        self.driver.quit()

    def test_add_contact(self):
        name = 'zhangsan'
        genger = '女'
        phonenum = '18211112222'
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        print("输入姓名")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        print("选择性别")
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("男")').click()
        if genger =='女':
            print("选择性别女")
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            print("选择性别男")
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()

        print("输入手机号")
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().className("android.widget.EditText").text("手机号")').send_keys(
            phonenum)
        # print("输入邮箱")
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiSelector().textContains("邮箱").fromParent(new UiSelector().text("选填"))').send_keys(
        #     "11111@qq.com")
        print("点击保存")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        ele = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
        assert "添加成功" == ele

