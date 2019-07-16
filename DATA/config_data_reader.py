#!/usr/bin/python3 
# coding=utf-8
# Written by 帅力
# Date: 2019-7-12
import xlrd
import xlwt

XLS_FILE = 'config_data.xlsx'


class DataReader(object):

    def __init__(self):
<<<<<<< HEAD
        self.f = xlrd.open_workbook(XLS_FILE)

    def get_dp_num(self):
        try:
            return self.f.sheet_by_name('DP_Device_Info').nrows
        except IOError as e:
            print(e)

    def get_gdms_info(self):
=======
        pass

    def get_gdms_info():
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
        """获取xls文件中GDMS_Info页签中数据，字典结构
        Args:
          无参数，可直接用DataReader.get_gdms_info()调用
        Raises:
            捕捉文件错误和IO错误
        Returns:
          字典结构返回xls中数据，具体查看$XLS_FILE文件
          keys=['gdms_url', 'gdms_username', 'gdms_psw', 'dp_username', 'dp_psw', 'dp_mod_psw']
        """
        try:
            data = {}
<<<<<<< HEAD

            table = self.f.sheet_by_name('GDMS_Info')
=======
            f = xlrd.open_workbook(XLS_FILE)
            table = f.sheet_by_name('GDMS_Info')
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
            for i in range(table.nrows):
                data[table.cell_value(i, 0)] = table.cell_value(i, 1)
            return data
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(e)

<<<<<<< HEAD
    def get_dp_info_by_list(self):
=======
    def get_dp_info_by_list():
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
        """获取xls文件中DP_Device_Info页签中数据，二维列表结构
        Args:
          无参数，可直接用DataReader.get_gdms_info()调用
        Raises:
            捕捉文件错误和IO错误
        Returns:
          二维列表结构返回xls中数据
          [['DUT_1', '192.168.85.191', 'admin', 'admin', '00:0B:82:B3:F1:83', '207GHTWH40B3F183'],
          ['DUT_2', '192.168.85.192', 'admin', 'admin', '', ''],
                    ...
          ['DUT_5', '192.168.85.188', 'admin', 'admin', '', ''],
          ['DUT_6', '192.168.85.187', 'admin', 'admin', '', '']]
          设备序号，IP地址，用户名，密码，MAC，SN号
        """
        try:
            data = []
<<<<<<< HEAD
            table = self.f.sheet_by_name('DP_Device_Info')
=======
            f = xlrd.open_workbook(XLS_FILE)
            table = f.sheet_by_name('DP_Device_Info')
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
            for i in range(table.nrows):
                data.append(table.row_values(i))
            return data
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(e)

<<<<<<< HEAD
    def get_dp_info_via_index(self, index=0):
        '''
        :param index:
        :return: 返回index+1台设备的所有信息：
        ['DUT_1', '192.168.85.191', 'admin', 'admin', '00:0B:82:B3:F1:83', '207GHTWH40B3F183']
        设备序号，IP地址，用户名，密码，MAC，SN号
        '''
        return self.get_dp_info_by_list()[index]

    def get_dp_mac_as_list(self, index=0):
=======
    def get_dp_mac_as_list(index=0):
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
        """
        按index索引获取设备列表中第index+1台设备的MAC地址
        Args:
            index为设备索引，0起始
        Raises:
            捕捉文件错误和IO错误
        Returns:
            list返回mac地址各段
        """
<<<<<<< HEAD
        tmp_list = DataReader.get_dp_info_by_list(self)
=======
        tmp_list = DataReader.get_dp_info_by_list()
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
        try:
            return str(tmp_list[index][4]).split(':')
        except IndexError as e:
            print(e)
        except IOError as e:
            print(e)

<<<<<<< HEAD
    def get_gdms_p_value_config(self):
=======
    def get_gdms_p_value_config():
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
        """
        获取gdms上预设的P值配置文件
        Args:
            None
        Raises:
            捕捉文件错误和IO错误
        Returns:
            返回配置文件字符串
        """
        tmp_file = open('GDMS config.txt')
        tmp_str = tmp_file.readlines()
        return tmp_str

<<<<<<< HEAD
    def get_dut_info_as_list(self):
        dut_info_list = []
        for i in range(self.f.sheet_by_name('DP_Device_Info').nrows):
            dut_info_list.append(DUTInfo(DataReader.get_dp_info_via_index(self, i)))
        return dut_info_list


class DUTInfo(object):
    '''
    DUT类，存储xls文件中各字段，通过类属性方式直接读取数据
    '''

    def __init__(self, args):
        self.dut_index = args[0]
        self.dut_ip = args[1]
        self.dut_user = args[2]
        self.dut_psw = args[3]
        self.dut_mac = args[4]
        self.dut_sn = args[5]


if __name__ == '__main__':
    dut = DataReader()
    print(dut.get_gdms_info()['gdms_username'])
    # print(DataReader.get_dp_info_by_list())
    # print(DataReader.get_dp_mac_as_list(0))
    # print(DataReader.get_gdms_p_value_config())

    # print(DataReader.get_dp_info_via_index(dut,0))

    # for i in DataReader().get_dut_info_as_list():
    #   print(i.dut_ip)
=======

if __name__ == '__main__':
    print(DataReader.get_gdms_info().keys())
    print(DataReader.get_dp_info_by_list())
    print(DataReader.get_dp_mac_as_list(0))
    print(DataReader.get_gdms_p_value_config())
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
