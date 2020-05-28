# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 17:04
# @Author  : Crush！！
# @FileName: 凯撒密码2.py
# @Software: PyCharm

def sec(s,key):
    t = ""
    for c in s:
        if 'a' <= c <= 'z': #str是可以直接比较的
            t += chr( ord('a') + ((ord(c)-ord('a')) + int(key) )%26 )
        elif 'A'<=c<='Z':
            t += chr( ord('A') + ((ord(c)-ord('A')) + int(key) )%26 )
        else:
            t += c
    return t
s = input("原文：")
key = input("key:")
print(sec(s,key))
