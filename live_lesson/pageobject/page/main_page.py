# 点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from live_lesson.pageobject.page.addresslist_page import AddressListPage
from live_lesson.pageobject.page.basepage import BasePage


class MainPage(BasePage):

    def click_addresslist(self):
        self.find((MobileBy.XPATH, '//*[@text="通讯录"]')).click()
        return AddressListPage(self.driver)
