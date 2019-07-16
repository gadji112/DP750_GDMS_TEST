#!/usr/bin/python3 
# coding=utf-8
# Written by 帅力
# Date：7/11/19

import selenium


class PublicDPControl:
    def __init__(self, driver):
        self.driver = driver

    def login_dp(self, username, psw):
        print('this is function login_dp')
        print('username:',username)
        print('password:',psw)
        pass

    def get_user_name(self):
        pass
