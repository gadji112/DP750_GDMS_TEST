#!/usr/bin/python3
# coding=utf-8
# Written by 帅力


from selenium import webdriver
import public_DP_control
import GDMS.GDMS_control
from selenium import webdriver
from GDMS.GDMS_control import GDMSControl
from DATA.config_data_reader import DataReader


class GDMSBusiness(GDMSControl):
    def __init__(self, driver):
        self.driver = driver
        GDMSControl.__init__(self.driver)

    def add_dp(self):
        add_device = GDMSControl.login_gdms()
        pass

    def reboot_dp(self):
        '''从gdms的设备列表页面，发起reboot设备的指令'''
        pass

    def factory_reset_dp(self):
        '''从gdms的设备列表页面，发起reset设备的指令'''
        pass

    def set_parameter(self, config_file):
        '''从gdms的设备列表页面，发起设置参数操作，需要调用DATA文件夹中的GDMS config.txt

        '''
        pass

    def set_account(self):
        '''从gdms页面设置账号及线路
           这里的账号测试数据最好使用固定数据，在gdms上预先配置好，方便起见
        '''
        pass


