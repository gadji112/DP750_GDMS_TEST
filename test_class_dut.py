#!/usr/bin/python3
# coding=utf-8
# Written by 帅力
# Date：2019/7/15

import selenium.webdriver
from DATA.config_data_reader import DataReader


class DUTInfo(object):
    def __init__(self, *args):
        self.dut_index = args[0]
        self.dut_ip = args[1]
        self.dut_user = args[2]
        self.dut_psw = args[3]
        self.dut_mac = args[4]
        self.dut_sn = args[5]


if __name__ == '__main__':
    n = DataReader.get_dp_num()
    DataReader.get_dp_info_via_index()
    dut_list = []
    for i in range(n):
        list.append(DUTInfo(DataReader.get_dp_info_via_index(i)))

    print(dut_list)