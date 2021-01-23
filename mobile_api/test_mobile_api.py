import time

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class Test_Demo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '84681e49'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        # 不清空本地缓存
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        # 以模拟器形式启动，case执行结束自动回收
        # desired_caps['avd'] = 'Pixel_23_6'
        # 设置页面空闲状态为0秒
        desired_caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown(self):
        self.driver.quit()

    def test_mobile_api(self):
        self.driver.make_gsm_call("13511112222", GsmCallActions.CALL)
        self.driver.send_sms("13511113333", "hello appium api")
        self.driver.set_network_connection(1)  # 设置飞行模式
        self.driver.set_network_connection(4)  # 设置回数据网络模式
        self.driver.get_screenshot_as_file("./photo/img.png")
        self.driver.start_recording_screen()
        self.driver.stop_recording_screen()
        pass
