"""
 1.array使用
 2.其他创建数组的方式
 3.特殊数组
 4.数组索引
 5.数组的运算
 6.数组的索引
 7.数组的拷贝
 8.数组的排序
"""
from numpy import *

"""
1.array使用
"""
x = array([[1, 1, 1], [2, 2, 2]])
print(x)
# 数组元素的总个数 6
print(x.size)
# 数组维度数 2
print(x.ndim)
# 数组的维数 （2,3）
print(x.shape)
# 数组的元素类型 int32
print(x.dtype)
# 每个元素占有字节的大小 4
print(x.itemsize)
# 数组元素的缓冲区 <memory at 0x00000195BB670AD0>
print(x.data)
"""
2.其他创建数组的方式
    arange使用
    linspace
    concatenate
"""
# arange 三个参数的含义分别为：开始值、结束值、步长（不包括结束值）
# reshape指定数组的行列
y = arange(0, 15, 1).reshape(3, 5)
print(y)
# linspace 三个参数含义分别为：开始值、结束值、元素数量（包括结束值）
z = linspace(0, 4, 5)
print(z)
# float64
print("z.dtype:" + str(z.dtype))
a = array([1, 2, 3])
b = array([4, 5, 6])
w = concatenate((a, b))
print(w)

print("==========================")
b = array([[[1, 2, 3], [3, 4, 5]], [[4, 5, 6], [7, 8, 9]]])
c = vstack(b)  # 面向行的方式对数组进行堆叠
print(c)
"""
[[1 2 3]
 [3 4 5]
 [4 5 6]
 [7 8 9]]
"""
d = hstack(b)
print(d)
"""
[[1 2 3 4 5 6]
 [3 4 5 7 8 9]]
"""
a = array([[1, 2], [3, 4]])
b = array([[5, 6], [7, 8]])
c = vstack((a, b))
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
print(c)
d = hstack((a, b))
# [[1 2 5 6]
#  [3 4 7 8]]
print(d)
#相当于hstack
c = column_stack((a, b))

print(c)

print("==============================")
"""
3.特殊数组
    zeros:全零数组
    ones：全一数组
    empty：空数组 元素都接近0
    eye:单位矩阵
    full(shape,val):生成数量为shape的元素全为val的数组
    ones_like(a):根据数组a的形状生成全是1的数组
    zeros_like(a):根据数组a的形状生成全是0的数组
    full_like(a,value):根据数组a的形状生成全是value的数组
"""
a = zeros((3, 4))
print(a)
b = ones((3, 4))
print(b)
c = empty((4, 4))
print(c)
d = eye(3)
print(d)
e = full(4, 2)
print(e)
f = ones_like(d)
print(f)
g = zeros_like(d)
print(g)
h = full_like(d, 3)
print(h)
"""
4.数组的变换
    4.1.reshape:不修改原数组
        resize:修改原数组
        ravel() :扁平化数组，变成一维数组 不修改原数组
        T():数组的转置 不修改原数组
        flatten():对数组降维，返回折叠后的一维数组，原数组不变
        swapaxes(value,ax1,ax2):对数组value中的两个维度进行交换
    4.2.astype：类型变换,一定会创建新的数组，即使两个类型一致(原始数据的一个拷贝)
    4.3.tolist：数组向列表转换
"""

i = ones((2, 3, 4), dtype=int32)
j = i.reshape((3, 2, 4))
print(j)
print(i)
print(i)
i.resize((3, 8))
print(i)
k = i.flatten()
print(k)
l = array([[2, 3, 4], [5, 6, 7]])
print(l)
m = swapaxes(l, 0, 1)
print(m)
n = array([[[0, 1],
            [2, 3]],
           [[4, 5],
            [6, 7]]])
o = swapaxes(n, 0, 2)
print(o)

p = ones((2, 3, 4), dtype=int)
print(p)
q = p.astype(float)
print(q)
r = p.tolist()
print(r)
s = array([[1, 2, 3], [4, 5, 6]])
print(s.T)
# [[1 4]
#  [2 5]
#  [3 6]]


"""
5.数组索引
    5.1.一维数组的索引
    5.2.多为数组的索引
"""
# 一维数组的索引
a = array([2, 3, 4, 5, 6])
# 编号0从左开始递增，或者-1开始从右递减
print(a[2])
print(a[-2])
# 起始编号，终止编号（不包含），步长
print(a[1:4:2])

# 多维数组的索引
d = arange(24).reshape(2, 3, 4)
print(d)
print(d[1, 0, 1])
# 多维数组的切片
print(d[1, 0, :])
# 每个维度可以使用步长跳跃切片
print(d[:, :, ::2])
"""
6.数组的运算
数组的加减乘除以及乘方运算方式为，相应位置的元素分别进行运算。
"""
print("=======================")
e = array([20.1, 30.9, 40, 50])
ee = arange(1, 5)
print(e + ee)
print(e - ee)
print(e * ee)
print(e / ee)
print(e ** ee)  # 乘方
# 数组中元素求和，最大值，最小值
print(e.sum())
print(sum(e))
print(e.max())
print(e.min())
print(e.mean())
print(e * 2)
print(floor(e))
# [20. 30. 40. 50.]
print(ceil(e))
# [21. 31. 40. 50.]
print(modf(e))
# (array([0.1, 0.9, 0. , 0. ]), array([20., 30., 40., 50.]))

f = array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 如果数值小于80，替换为0，如果大于等于80，替换为90
g = where(f < 80, '良好', '优秀')
print(g)
# cumsum:累加
a = arange(12).reshape(3, 4)
b = a.cumsum(axis=1)
print(a)
# [[ 0  1  3  6]
#  [ 4  9 15 22]
#  [ 8 17 27 38]]
print(b)

"""
7.数组的拷贝
"""
# 浅拷贝，只拷贝数组的引用，如果对拷贝进行修改，源数组也将修改
f = ones((2, 3))
print(f)
g = f
g[0, 0] = 2
print(g)
print(f)
# 深拷贝会复制一份和源数组一样的数组，新数组与源数组会存放在不同内存位置，因此对新数组的修改不会影响源数组
h = ones((2, 3))
print(h)
i = h.copy()
i[0, 0] = 2
print(i)
print(h)

"""
8.数组的排序
"""

a = array([[2, 3, 1], [1, 6, 5]])
# 整体排序
print(sort(a))
# 仅行排序
print(sort(a, axis=0))
# 仅列排序
print(sort(a, axis=1))

"""
9.线性代数相关计算

"""
# 1.矩阵相乘
a = array([[1, 2], [3, 4]])
b = array([[5, 6], [7, 8]])
c = dot(a, b)
print(c)  # [1*5+2*7,1*6+2*8],[3*5+4*7,3*6+4*8]
# 2.向量点积
d = vdot(a, b)
print(d)  # 1*5+2*6+3*7+4*8
# 3.一维数组的向量乘积
e = array([1, 2, 3])
f = array([4, 5, 6])
g = inner(e, f)
print(g)  # 1*4+2*5+3*6

h = inner(a, b)
print(h)  # [1*5+2*6,1*7+2*8],[3*5+4*6,3*7+4*8]
# 4.矩阵乘积
# 二维数组相当于矩阵乘法
i = array([[1, 0], [0, 1]])
j = array([[1, 2], [3, 4]])
k = matmul(i, j)
print(k)
# 二维数组和一维数组的运算
l = array([1, 2])
m = matmul(j, l)  # [1*1+2*2,3*1+4*2]
print(m)
n = matmul(l, j)  # [1*1+2*3,1*2+2*4]
print(n)
# 维度大于2的计算
o = arange(8).reshape(2, 2, 2)
p = array([[0, 1], [2, 3]])
q = matmul(o, p)
print(q)
# [[[ 2  3]
#   [ 6 11]]
#  [[10 19]
#   [14 27]]]
# 5.行列式计算
r = array([[1, 2], [3, 4]])
# 求行列式的值
s = linalg.det(r)
print(s)
t = array([2, 3])
# 计算线性方程组的解
u = linalg.solve(r, t)
print(u)
