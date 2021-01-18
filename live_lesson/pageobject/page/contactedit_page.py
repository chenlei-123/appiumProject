from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from live_lesson.PO.page.basepage import BasePage
from live_lesson.PO.page.memberinvite_Page import MemberInvitePage


class ContactEditPage(BasePage):
    def edit_name(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        return self

    def edit_gender(self, gender):
        locator = (MobileBy.XPATH, "//*[@text='男']")
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        return self

    def edit_phonenum(self, phonenum):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().className("android.widget.EditText").text("手机号")').send_keys(
            phonenum)
        return self

    def click_save(self):
        self.find((MobileBy.XPATH, "//*[@text='保存']")).click()
        return MemberInvitePage(self.driver)
