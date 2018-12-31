#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Fu Yixuan"
__pkuid__  = "1800011720"
__email__  = "FuYixuan@pku.edu.cn"
"""

import sys
from urllib.request import urlopen

import string
from collections import OrderedDict

from urllib import request
from urllib import error

def wcount(lines, topn=10): #输入文本统计字符串的函数#
    import string
    from collections import OrderedDict
    
    new_lines = ''
    for i in lines: #for循环将标点符号除去，建立新的lines#
        if i in string.ascii_letters:
            i = i.lower()
            new_lines = new_lines + i
        else:
            new_lines = new_lines + ' '   
    list = new_lines.split()
    list = sorted(list) #从31行到40行可用count函数代替，这里给出另一种方法#
    wcdic = {}          #即通过先将list排序，如果与上一个str相等就计数加一，不等就在字典建立新的str#
    for i in range(len(list)):
        if i == 0:
            wcdic[list[i]] = 1
        else:
            if list[i] != list[i-1]:
                wcdic[list[i]] = 1
            else:
                wcdic[list[i]] += 1
                
    tdic = sorted(wcdic.items(), key=lambda obj: obj[1], reverse = True) #字典排序#
    for i in range(topn): #输出#
        print(tdic[i][0],end = '\t')
        print(tdic[i][1],end = '\n')
    pass

def trys(t):
    req = request.Request(t[1])
    #运用try-except-slse完成判断网址是否正确#
    try:
        responese = request.urlopen(req)
        
    except ValueError as e: 
        print('请输入正确的网址，记得加上http和https哦')
    except error.HTTPError as e:
        dic = {400:'请求出错',
               401:'未授权',
               403:'禁止访问',
               404:'找不到或被河蟹',
               405:'不允许此方法',
               406:'不可接受',
               407:'需要代理身份验证',
               412:'前提条件失败',
               414:'Request-URI 太长',
               500:'服务器的内部错误',
               501:'未实现',
               502:'网关出错'}
        print(e.code,dic.get(e.code, '这不是一个常见错误，请您自行百度'))
    except error.URLError as e:
        print('URLError')
        print(e.reason)
        
    else: #真代码，用pyassign2的方法运行#
        doc = urlopen(t[1])
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode()
        wcount(jstr,int(t[2]))
    

if __name__ == '__main__':
    if  len(sys.argv) == 1: #如果输入内容转化成list只有一项的话，提示你如下内容#
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
    trys(sys.argv)
