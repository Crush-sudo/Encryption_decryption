# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 11:37
# @Author  : Crush！！
# @FileName: 仿射密码.py
# @Software: PyCharm

class mapping_encryption(object):
    def __init__(self,a,b):
        # 定义a,b的值
        self.a = int(a)
        self.b = int(b)
        #正向映射表
        self.forword_tables={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        #反向映射表
        self.reverse_tables={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
    #加密
    def ek(self,x):
        #ek(x)=(ax+b)mod26
        if x in self.forword_tables:
            x=int(self.forword_tables.get(x))
            k_res=divmod((self.a*x+self.b),26)[1]
            return self.reverse_tables.get(k_res)
        else:
            return x
    #解密
    def dk(self,y):
        #dk(y)=a(-1)(y-b)mod26
        if y in self.forword_tables:
            y=int(self.forword_tables.get(y))
            res=()
            for i in range(0,26):
                res=divmod(i*26+(y-self.b),self.a)
                if res[1] == 0:
                    break
            k_res=res[0]
            return self.reverse_tables.get(k_res)
        else:
            return y
m=mapping_encryption(7,3)
# forword_x=m.ek("z")
# print("加密后为：",forword_x)
# reverse_x=m.dk(forword_x)
# print("解密后为：",reverse_x)
#定义原始明文
word="hot"
reverse_word=''
forword_word=''
for i in word:
    forword_word+=m.ek(i)
print(forword_word)
for i in forword_word:
    reverse_word+=m.dk(i)
print(reverse_word)