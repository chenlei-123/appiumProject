from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)
driver.find_element_by_id("")
driver.find_element_by_id("").send_keys("")

driver.quit()