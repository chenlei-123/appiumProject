from appium import webdriver

from page.Main import Main
from page.base_page import BasePage


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = "com.xueqiu.android.view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrandPermissions"] = True
            caps["noReset"] = "true"
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)
