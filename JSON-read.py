# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:29:27 2020

@author: Nicolas Xiong
"""


import json

 

filename='test.json'

with open(filename,'r',encoding='utf-8') as file:

    data=json.load(file)

    #<class 'dict'>,JSON文件读入到内存以后，就是一个Python中的字典。

    # 字典是支持嵌套的，

    print(type(data))
