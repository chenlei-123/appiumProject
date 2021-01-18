# 启动app/关闭app/启动app、进入首页。。
from appium import webdriver

from live_lesson.PO.page.basepage import BasePage
from live_lesson.PO.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
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
            # 设置页面空闲状态为0秒
            desired_caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)  # 隐式等待
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
