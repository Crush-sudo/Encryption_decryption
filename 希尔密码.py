# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 17:43
# @Author  : Crush！！
# @FileName: 希尔密码.py
# @Software: PyCharm

#将字符按长度分组
def cut(obj, sec):
    return [obj[i:i + sec] for i in range(0, len(obj), sec)]
import numpy as np
class Hill_encryption(object):
    def __init__(self,k,kn,m):
        self.m=int(m)
        self.k=np.array(k)
        #求密钥k矩阵的逆矩阵
        self.kn=np.array(kn)
        # self.kn =np.linalg.inv(self.k)
        # 正向映射表
        self.forword_tables = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
                               'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
                               'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        # 反向映射表
        self.reverse_tables = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
                               11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
                               21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

    def ek(self,word):
        #将字符串先分组
        ek_list=cut(word,self.m)
        ek_num_lists=[]
        #将分组结果转换为对应数字
        for i in ek_list:
            ek_m_list = []
            for j in i:
                ek_m_list.append(self.forword_tables.get(j))
            ek_num_lists.append(ek_m_list)
        #将分组数字结果转换为矩阵
        x=np.array(ek_num_lists)
        #开始加密计算
        ek_res = np.dot(x,self.k)
        # 将乘积结果中的每个数mod26,结果存放到list中
        res_num_list = []
        for i in ek_res:
            for j in i:
                res_num_list.append(divmod(j, 26)[1])
        #转为字母
        res_word_list=''
        for i in res_num_list:
            res_word_list+=(self.reverse_tables.get(i))
        return res_word_list
    #解密函数
    def dk(self,word):
        # 将字符串先分组
        ek_list = cut(word, self.m)
        ek_num_lists = []
        # 将分组结果转换为对应数字
        for i in ek_list:
            ek_m_list = []
            for j in i:
                ek_m_list.append(self.forword_tables.get(j))
            ek_num_lists.append(ek_m_list)
        # 将分组数字结果转换为矩阵
        ex= np.array(ek_num_lists)
        # 开始解密计算
        ek_res = np.dot(ex, self.kn)
        # 将乘积结果中的每个数mod26,结果存放到list中
        dkres_num_list = []
        for i in ek_res:
            for j in i:
                dkres_num_list.append(divmod(j, 26)[1])
        # 转为字母
        dkres_word_list = ''
        for i in dkres_num_list:
            dkres_word_list += (self.reverse_tables.get(i))
        return dkres_word_list
#定义key矩阵和逆矩阵
k=[[11,8],[3,7]]
kn=[[7,18],[23,11]]
hill=Hill_encryption(k,kn,2)
ek_word=hill.ek("word")
dk_word=hill.dk(ek_word)
print("加密后为：",ek_word)
print("解密后为：",dk_word)

