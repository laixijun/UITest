#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 17:15
# @Author  : vivid
# @FileName: MySQLDB.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

import configparser, os
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs

class Config:
    def __init__(self, group,configPath="automation/configs/config.cfg"):
        """

        :param group: 配置[ ]中的属性
        :param configPath: "automation/configs/config.cfg"，获取相对路径，绝对路径需要从根开始
        """
        self.group = group
        self.configPath = configPath
    def parsing_config(self, key):
        """
        解析config.cfg配置文件
        :param group: 传入组名
        :param key: 传入key值
        :return:
        """
        try:
            # 生成config对象
            conf = configparser.ConfigParser()
            # 获取根项目路径，导入SystemOsUtil.SystemOs
            sysos=SystemOs()
            sysOsPath=sysos.sys_path(self.configPath)
            # 用config对象读取配置文件
            conf.read(sysOsPath)
            return conf.get(self.group, key)  # type:str
        except Exception as e:
            print(e)
            # 异常后，让程序停止。暂留
            os._exit(1)

    def get_url_config(self, url_key):
        """
        获取url的配置信息
        :param url_key:
        :return:
        """
        return self.parsing_config(url_key)

    def get_path_config(self, path_key):
        """
        获取一些文件的路径
        :param path_key:
        :return:
        """
        return self.parsing_config(path_key)

    def get_email(self, email_key):
        """
        获取邮件信息
        :param email_key:
        :return:
        """
        return self.parsing_config(email_key)  # type:str

    def get_mysqldb(self,mysql_key):
        """
        获取数据库信息
        :param mysql_key:
        :return:
        """
        return self.parsing_config(mysql_key)

    def get_mongodb(self,mongoDB_key):
        """
        获取数据库信息
        :param mysql_key:
        :return:
        """
        return self.parsing_config(mongoDB_key)

    def get_configPath(self,configPath):
        """
            获取配置文件信息
            :param mysql_key:
            :return:
        """
        return self.parsing_config(configPath)
if __name__=='__main__':

    #conf = Config("FilePath",configPath="E:/python_workspace/DestroyerRobot/automation/com/cn/markerting_points/config/config.cfg")
    conf = Config("YamlFile")
    keys = conf.parsing_config("marketing")
    # s = SystemOs().sys_path()
    # print("s=",s)
    # filepath = s+"automation/com/cn/markerting_points/config/config.cfg"
    # conf = Config("FilePath",
    #               configPath=filepath)
    # keys=conf.parsing_config("user_login")
    print(keys)