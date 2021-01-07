import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
desired_caps['noReset'] = 'true'
desired_caps['dontStopAppOnReset'] = 'true'
desired_caps['skipDeviceInitialization'] = 'true'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 隐式等待

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.find_element_by_accessibility_id("").click()  # 相当于content-desc属性
driver.back()
driver.back()

time.sleep(3)  # 强制等待
WebDriverWait(driver, 10, 0.5).until(
    expected_conditions.visibility_of_element_located((MobileBy.ID, "com.xueqiu.android:id/stock_name_five")))
driver.quit()
