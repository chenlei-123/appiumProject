from selenium.webdriver.common.by import By

from live_lesson.test_frame.basepage import BasePage
from live_lesson.test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.run_steps("../page/main_page.yaml", "goto_market_page")
        # self.find((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']")).click()
        # self.find((By.XPATH,"//*[@text='行情']")).click()
        return MarketPage(self.driver)

    def goto_mine(self):
        # self.run_steps("../page/main_page.yaml,", "goto_mine")
        self.run_steps("../page/main_page.yaml", "goto_mine")