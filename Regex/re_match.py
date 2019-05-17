#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-05-13 22:01
@Author  : zxp
@Project : Python
@File    : re_match.py
@Description: ==================================
    re.match的用法
@license: (C) Copyright 2013-2019.    
************************************************
"""
import re
compile_pattern=re.compile(r'(.*) are (.*?) .*')



line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(compile_pattern, line, re.M | re.I)
matchObj1=compile_pattern.match(line)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))

else:
    print("No match!!")