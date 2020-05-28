import numpy as np
x=np.array([[9,20],[11,24]])
k=np.array([[11,8],[3,7]])
kn=np.array([[7,18],[23,11]])

a=[[9, 20], [11, 24]]
xx=np.array(a)

#计算矩阵乘积
ek_res=np.dot(xx,k)
#将乘积结果中的每个数mod26
# res_num_list=[]
# for i in ek_res:
#    for j in i:
#        res_num_list.append(divmod(j,26)[1])
# print(res_num_list)

print(k)

k_inv=np.linalg.inv(k)
print(k_inv)


