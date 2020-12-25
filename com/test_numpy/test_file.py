from numpy import *

a = array([[1, 2, 3, 4], [5, 6, 7, 8]])
# 保存文件为csv格式
# savetxt("C:/Users/xm/Desktop/a.csv", a)

# csv文件不支持保存多维数据。
b = arange(24).reshape((2, 3, 4))
print(b)
# 报错：ValueError: Expected 1D or 2D array, got 3D array instead
# savetxt("C:/Users/xm/Desktop/b.csv", b)

# 读取文件
c = loadtxt("C:/Users/xm/Desktop/a.csv")
# print(c)

# 多维数组的保存csv文件
# 如果sep='',即数据分隔字符串是空串，写入的文件为二进制。
d = arange(24).reshape((2, 3, 4))
# d.tofile('C:/Users/xm/Desktop/d.csv', sep=',', format='%s')

# 多维数组的读取csv文件
e = fromfile('C:/Users/xm/Desktop/d.csv', dtype=int, sep=',').reshape((2, 3, 4))
print(e)
# 多维数组保存时，维度会转化一维保存
f = fromfile('C:/Users/xm/Desktop/d.csv', dtype=int, sep=',')
print(f)

# 多维数组存储npy文件 ,npy文件存储支持多维数组 npy文件
# g = array([[1, 2, 3, 4], [5, 6, 7, 8]])
g = arange(24).reshape((2, 3, 4))
save('C:/Users/xm/Desktop/g.npy', g)

# 读npy文件
h = load('C:/Users/xm/Desktop/g.npy')
print(h)

# 多个数组保存到一个文件中npz文件
a = array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = array([[1, 2, 3, 4], [5, 6, 7, 8]])
c = array([[1, 2, 3, 4], [5, 6, 7, 8]])

savez('C:/Users/xm/Desktop/z.npz', a, b, c)
# 重命名
savez('C:/Users/xm/Desktop/z.npz', a1=a, b1=b, c1=c)

A = load('C:/Users/xm/Desktop/z.npz')
print(A['a1'])
print(A['b1'])
print(A['c1'])



