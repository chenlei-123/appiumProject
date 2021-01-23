from appium.webdriver.common.mobileby import MobileBy

from live_lesson.pageobject.page.basepage import BasePage
from live_lesson.pageobject.page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):
    def addcontact_menual(self):
        self.find((MobileBy.XPATH,'//*[@text="手动输入添加"]')).click()
        return ContactEditPage(self.driver)

    def get_toast(self):
        ele = self.find((MobileBy.XPATH,'//*[@class="android.widget.Toast"]')).text
        return ele
