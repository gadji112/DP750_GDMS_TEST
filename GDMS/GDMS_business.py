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
        add_device=GDMSControl.login_gdms()



