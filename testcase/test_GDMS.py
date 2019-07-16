#!/usr/bin/python3
# coding=utf-8
# Written by 帅力
# Date：7/10/19

import unittest
from selenium import webdriver
from GDMS.GDMS_business import GDMSBusiness
from GDMS.GDMS_control import GDMSControl
from public_DP_control.public_DP_control import PublicDPControl


class TestGDMS(unittest.TestCase):
    def setUp(self) -> None:
        self.driver_GDMS = webdriver.Chrome()
        self.driver_GDMS.get('www.gdms.cloud')
        gdms_user=
        gdms_psw=

        gdms=GDMSControl(self.driver_GDMS).login_GDMS(gdms_user,gdms_psw)


        self.driver_DP = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver_GDMS.quit()
