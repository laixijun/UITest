#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/5 11:34
# @Author  : vivid
# @FileName: yamlutil.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import yaml

class yamlUtil:
    def __init__(self,yamlpath):
        self.yamlpath = yamlpath


    def get_yalm(self):
        try:
            with open(self.yamlpath,"r",encoding="utf-8") as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            with open(self.yamlpath,"r",encoding="utf-8") as f:
                data = yaml.load(f)
        finally:
            return  data
    # def get_yalm(self):
    #
    #     with open(self.yamlpath,"r",encoding="utf-8") as f:
    #         data = yaml.load(f , Loader=yaml.FullLoader)
    #
    #     return  data

if __name__=="__main__":
    datainfo = yamlUtil("C:\\Users\\vivid\\PycharmProjects\\untitled\\DestroyerRobot\\automation\\api\\cn\\hopsonApi\\config\\api_cms.yaml")
    data = datainfo.get_yalm()
    print(data)


