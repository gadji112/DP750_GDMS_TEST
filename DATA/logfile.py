<<<<<<< HEAD
# coding=utf-8
# 作者:蒋甜
# 时间:2018年4月27日

import os, logging
import time

log_path = "/home/DP750_GDMS_TEST/DATA/log"


# log_path_2="~/PycharmProjects/DP750_GDMS_TEST/DATA/log"

# /home/leo/Downloads/GWN76xx_regressiontest_7630_v9.0.3_jffan/data
class Log:
    def __init__(self, model_name):
        # 文件的命名
        # self.logname = os.path.join(log_path, '%s%s.log'%(model_name,time.strftime('%Y_%m_%d')))
        self.logname = os.path.join(log_path, '%s.log' % model_name)
        # self.logname_2 = os.path.join(log_path_2, '%s.log'%model_name)
=======
#coding=utf-8
#作者:蒋甜
#时间:2018年4月27日

import os,logging
import time
log_path = "/home/leo/PycharmProjects/DP750_GDMS_TEST/DATA/log"
log_path_2="~/PycharmProjects/DP750_GDMS_TEST/DATA/log"

#/home/leo/Downloads/GWN76xx_regressiontest_7630_v9.0.3_jffan/data
class Log:
    def __init__(self,model_name):
        # 文件的命名
        # self.logname = os.path.join(log_path, '%s%s.log'%(model_name,time.strftime('%Y_%m_%d')))
        self.logname = os.path.join(log_path, '%s.log'%model_name)
        self.logname_2 = os.path.join(log_path_2, '%s.log'%model_name)
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        print(self.logname)
<<<<<<< HEAD
        # print(self.logname_2)
        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')
        self.formatter = logging.Formatter('[%(asctime)s]:%(message)s')

=======
        print(self.logname_2)
        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')
        self.formatter = logging.Formatter('[%(asctime)s]:%(message)s')
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

<<<<<<< HEAD

=======
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
if __name__ == "__main__":
    log = Log('dp750')
    log.info("---测试开始----")
    log.info("输入密码")
<<<<<<< HEAD
    log.warning("----测试结束----")
=======
    log.warning("----测试结束----")
>>>>>>> ad9fa975c480da67d428a20779f69481b3b79636
