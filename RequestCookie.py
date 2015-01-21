
# Copyright (C) 2013-2014 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html

import http.cookies


class RequestCookie(http.cookies.SimpleCookie):
    '''为SimpleCookie()类加入了一个新的方法, 将里面的cookie值输出为http
    request header里面的字段.
    '''

    def __init__(self, rawdata=''):
        print('/usr/local/lib/python3.4/dist-packages/bcloud/RequestCookie.py:__init__ 13')
        super().__init__(rawdata)

    def header_output(self):
        print('/usr/local/lib/python3.4/dist-packages/bcloud/RequestCookie.py:header_output 16')
        '''只输出cookie的key-value字串.
        
        比如: HISTORY=21341; PHPSESSION=3289012u39jsdijf28; token=233129
        '''
        result = []
        for key in self.keys():
            result.append(key + '=' + self.get(key).value)
        return '; '.join(result)

    def sub_output(self, *keys):
        print('/usr/local/lib/python3.4/dist-packages/bcloud/RequestCookie.py:sub_output 26')
        '''获取一部分cookie, 并将它输出为字符串'''
        result = []
        for key in keys:
            if self.get(key):
                result.append(key + '=' + self.get(key).value)
        return '; '.join(result)

    def __str__(self):
        print('/usr/local/lib/python3.4/dist-packages/bcloud/RequestCookie.py:__str__ 34')
        return self.header_output()

    def load_list(self, raw_items):
        print('/usr/local/lib/python3.4/dist-packages/bcloud/RequestCookie.py:load_list 37')
        '''读取多个以字符串形式存放的cookie.'''
        if not raw_items:
            return
        for item in raw_items:
            self.load(item)
