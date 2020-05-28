# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 16:49
# @Author  : Crush！！
# @FileName: 凯撒密码.py
# @Software: PyCharm

#大写字母表
ALP="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#小写字母表
alp=ALP.lower()
#大写加密表
SEC="DEFGHIJKLMNOPQRSTUVWXYZABC"
#小写加密表
sec= SEC.lower()
str= input("请输入原文：")
code=""
for i in str:
    if i in ALP:
        c = ord(i) - ord("A")
        code = code + SEC[c]
    elif i in alp:
        c = ord(i) - ord("a")
        code = code + sec[c]
    else:
        code = code + i
print(code)

