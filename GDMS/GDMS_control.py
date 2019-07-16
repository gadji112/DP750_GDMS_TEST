#!/usr/bin/python3
# coding=utf-8
# Written by 帅力
# Date：7/10/19

from public_DP_control.public_DP_control import PublicDPControl
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class GDMSControl(PublicDPControl):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        PublicDPControl.__init__(self, self.driver)

    def login_gdms(self, username, psw):
        u"""登录GDMS网站"""
        # //TODO：将GDMS地址、用户名、密码等信息参数化
        self.driver.get("https://www.gdms.cloud")
        self.driver.implicitly_wait(60)
        username = self.driver.find_element_by_xpath('//input[@type=\'text\']')
        username.send_keys('lshuai@grandstream.cn')
        psw = self.driver.find_element_by_xpath('//input[@type=\'password\']')
        psw.send_keys('123456gs')
        psw.send_keys(Keys.ENTER)

    def switch_to_device_list(self):
        u"""切换到device list菜单"""
        self.driver.find_element_by_css_selector('.el-submenu:nth-child(3) > .el-submenu__title').click()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_css_selector('.is-opened .el-menu-item:nth-child(1)').click()

    def switch_to_diagnostics(self):
        u"""切换到diagnostics菜单"""
        self.driver.find_element_by_css_selector('.collapsed > .el-menu-item:nth-child(7)').click()

    def switch_to_model(self):
        u'''切换到型号页面'''
        pass

    def switch_to_group(self):
        u'''切换到group页面'''
        pass

    def swtich_to_cfg(self):
        u'''切换到cfg页面'''
        pass



if __name__ == '__main__':
    driver = webdriver.Chrome()
    test = GDMSControl(driver)
    test.login_gdms('lshuai@grandstream.cn', '123456gs')
    test.switch_to_device_list()
    test.switch_to_diagnostics()
    test.login_dp('test_public_control', 'psw')
    # driver.quit()

