from selenium.webdriver.common.by import By

from live_lesson.test_frame.basepage import BasePage
from live_lesson.test_frame.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.run_steps("../page/market_page.yaml", "goto_search")
        # self.find((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")).click()
        return SearchPage(self.driver)
