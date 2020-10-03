#!/usr/bin/env python
# coding:utf-8

__version__ = "1.0.0"
__author__ = "Kevin"
__date__ = "Thu May 30 22:02:49 2019"
__copyright__ = "All rights reserved"

'''
本模块实现打开网页的post方法和get方法的封装
web_page类包含4个属性：request、response、info、page。
    request是请求对象
    response是返回对象
    info是返回的head信息
    page是返回的网页内容

类包含一个方法，open_url()，使用方法如下：
    open_url(url, values='',
                 header={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15;"},
                 add_headers=[])
    参数解析：
    url：打开的网址
    values：采用post方法时，通过此参数传入data数据，该参数为字典形式
    header：浏览器代理信息，默认设置的是osx的safari，此参数为字典形式
    add_headers：可以添加额外的head信息，比如("Connection","keep-alive")等，此参数为元组参数对组成的列表

    执行该方法后，返回的内容通过page属性来访问

'''

import ssl
import urllib.request
import urllib.parse
import http.cookiejar
from urllib.error import URLError  # 导入错误处理模块
import chardet


def main():
    pass


if __name__ == "__main__":
    main()


class Web_Page(object):
    def __init__(self):
        self.request = None
        self.response = None
        self.info = None
        self.page = ""
        self.cookie = None

    def open_url(self,
                 url,
                 values=None,
                 header={
                     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15;"},
                 add_headers=None,
                 cookie=None):
        '''
        @note: 用指定指定参数打开指定的网址
        @parameter url: 要打开的网页的网址
        @parameter values: 使用post方法时，需要传递的参数，类型为dict
        @parameter header: 浏览器agent
        @parameter add_headers: 需要另外添加的链接参数，类型为tuple组成的list
        @parameter cookie: 载入cookie对象，默认为None，会自动保存访问时set的cookie到cookie属性
        '''

        ssl._create_default_https_context = ssl._create_unverified_context  # 提交表单，实现https支持

        if cookie == None:
            cookie = http.cookiejar.LWPCookieJar()
            handle = urllib.request.HTTPCookieProcessor(cookie)
            opener = urllib.request.build_opener(handle)
            urllib.request.install_opener(opener)
        else:
            handle = urllib.request.HTTPCookieProcessor(cookie)
            opener = urllib.request.build_opener(handle)
            urllib.request.install_opener(opener)

        if values != None:
            data = urllib.parse.urlencode(values).encode('utf-8')  # 对data数据进行编码
            self.request = urllib.request.Request(url, data, headers=header)  # 加入data数据，实现post请求
        else:
            self.request = urllib.request.Request(url, headers=header)  # 无data数据，实现get请求

        # 加入额外的header信息
        if add_headers != None:
            for head in add_headers:
                self.request.add_header(*head)

        # 开始发送请求
        try:
            self.response = urllib.request.urlopen(self.request, timeout=20)
        except URLError as e:
            print('发生错误', e)

        if self.response == None:
            print('未能正确获得网页内容')
        else:
            self.cookie = cookie
            readres = self.response.read()

            # 检测页面编码方式，如utf-8, gbk等
            mychar = chardet.detect(readres)
            code_stype = mychar['encoding']
            # print(code_stype)
            if code_stype == "GB2312":
                self.page = readres.decode('gbk')
            else:
                self.page = readres.decode(code_stype)  # 对返回的结果进行读取并解码，read方法可以指定数字参数，仅读取指定的前几行
            self.info = self.response.info()
