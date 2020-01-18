# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:21:03 2020

@author: Nicolas Xiong
"""


import json

mydict={'name':'leon','age':'30','email':'xxxx@163.com'}

file='test.json'

with open(file,'w',encoding='utf-8') as f:

    json.dump(mydict,f)

    print("加载入文件完成...")
