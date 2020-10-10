#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 15:44
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : action.py

import requests

from DestroyerRobot.automation.util.JosnUtil import  JsonUtils
from DestroyerRobot.automation.util.YamlUtil import yamlUtil


class HttpClient(object):
    def __init__(self):
        pass

    def request(self, requestMethod, requestUrl, paramsType,
                requestData, headers =None, **kwargs):

        if requestMethod == "post":
            print("---", requestData, type(requestData))
            if paramsType == "form":
                response = self.__post(url = requestUrl, data =JsonUtils().json_dumps(requestData),
                                  headers = headers, **kwargs)
                return response
            elif paramsType == "json":
                response = self.__post(url = requestUrl, json = JsonUtils().json_dumps(requestData),
                                  headers = headers, **kwargs)
                return response
        elif requestMethod == "get":
            request_url = requestUrl
            if paramsType == "url":
                request_url = "%s%s" %(requestUrl, requestData)
            response = self.__get(url = request_url, params = requestData, **kwargs)
            return response

    def __post(self, url, data = None, json = None, headers=None,**kwargs):
        print("----")
        response = requests.post(url=url, data = data, json=json, headers=headers)
        return response

    def __get(self, url, params = None, **kwargs):
        response = requests.get(url, params = params, **kwargs)
        return response

if __name__ == "__main__":
    hc = HttpClient()
    res = {"loginName": "13600000001","password": "123456","loginSysName": "bonus"}
    #re = JsonUtils().json_dumps(res)
    # header = {"Content-Type":"application/json"}

    datainfo = "C:\\Users\\vivid\\PycharmProjects\\untitled\\DestroyerRobot\\automation\\api\\cn\\hopsonApi\\config\\api_cms.yaml"
    header = yamlUtil(datainfo).get_yalm()
    # header = data['Content-Type']
    res = hc.request("post", "https://tapi.lifeat.cn:45788/user/login/login", "form",res,header)
    print(res.json())