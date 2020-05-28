# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 10:58
# @Author  : Crush！！
# @FileName: 维吉尼亚密码.py
# @Software: PyCharm
def cut(obj, sec):
    return [obj[i:i + sec] for i in range(0, len(obj), sec)]
class Virginia_encryption(object):
    def __init__(self,k,m):
        self.m=int(m)
        self.k=k
        #将密钥转为数字串
        self.k_num=[]
        # 正向映射表
        self.forword_tables = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
                               'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
                               'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        # 反向映射表
        self.reverse_tables = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
                               11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
                               21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
        for i in self.k:
            self.k_num.append(self.forword_tables.get(i))
    #加密
    def ek(self,word):
        ek_list = cut(word, self.m)
        ek_num_lists = []
        # 将分组结果转换为对应数字
        for i in ek_list:
            ek_m_list = []
            for j in i:
                ek_m_list.append(self.forword_tables.get(j))
            ek_num_lists.append(ek_m_list)
        res_num_list=[]
        #加密计算
        for i in ek_num_lists:
            for j in range(0,self.m):
                res_num_list.append(divmod(i[j]+self.k_num[j],26)[1])
        res_word_list=''
        #将结果转为字母
        for i in res_num_list:
            res_word_list+=(self.reverse_tables.get(i))
        return res_word_list

k="cipher"
ve=Virginia_encryption(k,6)
x="thiscryptosystemisnotsec"
print(ve.ek(x))