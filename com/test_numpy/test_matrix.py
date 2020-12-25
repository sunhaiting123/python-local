from numpy import *

"""
1.矩阵的创建
"""

a = matrix([[1,0,],[0,1]])
b = matrix([[1, 2], [3,4]])
# print(b, b.dtype)
c = asarray(a) # matrix转array
print(c)
d = asmatrix(c) # array转matrix
print(d)

# print(a*b)
#运行结果：矩阵相乘
# [[1 2]
#  [3 4]]

c = array([[1,0,],[0,1]])
d = array([[1, 2], [3,4]])
# print(c*d)
#运行结果：对应位置相乘
# [[1 0]
#  [0 4]]
# print(c.dot(d))
#运行结果：矩阵相乘
# [[1 2]
#  [3 4]]


# print(a.T)  # 矩阵的转置
# print(a.H)  # 矩阵的共轭矩阵
# print(a.I)  # 矩阵的逆矩阵


e =matrix([[1,2],[3,4]])
f =array([[1,2],[3,4]])
# print(e**2)
#运行结果：
# [[ 7 10]
#  [15 22]]
# print(f**2)
#运行结果
# [[ 1  4]
#  [ 9 16]]
print("==========")
print(e.mean())
print(e.min())
print(f.mean())
print(f.min())














