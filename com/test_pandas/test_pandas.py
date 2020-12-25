from pandas import Series, DataFrame
import pandas as pd
import numpy as np

"""
1.通过一维数组创建Series
2.通过字典的方式创建Series
3.Series应用NumPy数组运算
4.Series缺失值检测 isnull  notnull
5.不同Series之间进行算术运算，会自动对齐不同索引的数据
6.通过二维数组创建DataFrame
7.通过字典的方式创建DataFrame
"""

"""
1.通过一维数组创建Series
2.可以自定义索引
"""
a = np.array([1, 2, 3, 4])
# 索引，元素，元素类型
b = pd.Series(a)
print(b)
# 自定义索引
c = Series([70, 80, 90], index=['语文', '数学', '英语'])
print(c)
# 字典的方式创建Series
d = {'a': 1, 'b': 2, 'c': 3}
e = Series(d)
print(e)

# 通过索引取值
f = e['a']
print(f)
# Series应用NumPy数组运算
g = np.exp(e)
print(g)
h = e / 10
print(h)
# 缺失值检测
s1 = Series([70, 80, 90], index=['语文', '数学', '英语'])
new_index = ['语文', '数学', '英语', '物理']

s2 = Series(s1, index=new_index)
print(s2)

s3 = pd.isnull(s2)
s4 = pd.notnull(s2)
print(s3)
print(s4)
# 过滤出为缺失值和不为缺失值的项
s5 = s2[s3]
s6 = s2[s4]
print(s5)
print(s6)
# 不同Series之间进行算术运算，会自动对齐不同索引的数据
num1 = Series([1, 2, 3, 4], index=['p3', 'p1', 'p2', 'p5'])
num2 = Series([1, 2, 3, 4, 5], index=['p1', 'p2', 'p3', 'p4', 'p5'])
res = num1 * num2
print(res)
num1.name = 'sss'
num1.index.name = 'aaa'
print(num1)
# 通过二维数组创建DataFrame
df1 = DataFrame([['a', 'b', 'c'], [10, 20, 30]])
print(df1)
df2 = DataFrame([['a', 10], ['b', 20], ['c', 30]])
print(df2)
# 自定义行索引和列索引
arr = np.array([['a', 1], ['b', 2], ['c', 3]])
df3 = DataFrame(arr, index=['row1', 'row2', 'row3'], columns=['col1', 'col2'])
print(df3)
# 通过字典方式创建Dataframe
data = {"a": [1, 2, 3, 4], "b": [1.0, 2.0, 3.0, 4.0], "c": [2, 4, 6, 8]}
df4 = DataFrame(data)
print(df4)
# 通过索引从dataframe中取值
df5 = df4['a']
print(df5)
print("=============")
print(df5.describe())

ser = Series(['a', 'b', 'c', 'a', 'a', 'b', 'c'])
mask = ser.isin(['b', 'c'])
print(mask)
res = ser[mask]
print(res)

# 缺失值的处理

ser2 = Series([1, 2, 3, 4, np.NaN, 5])
# 删除缺失值
ser3 = ser2.dropna()
print(ser3)

df6 = DataFrame([[1, 2, 3, 4], [np.nan, np.nan, np.nan, np.nan], [5, 6, np.nan, 8]])
# 删除有空值的全部行
df7 = df6.dropna()
print(df7)
# 删除全部为缺省值的行
df8 = df6.dropna(how='all')
print(df8)
# 丢失全部为缺失值的列
df9 = df6.dropna(axis=1, how='all')
print(df9)

# 缺失值填充为0
df10 = df6.fillna(0)
print(df10)

# dataframe层次化索引
data = Series([1, 2, 3, 4, 5], index=[['a', 'a', 'b', 'b', 'c'], ['2020', '2020', '2019', '2019', '2018']])
print(data)

data2 = DataFrame({'year': ['2020', '2020', '2019', '2019', '2018'], 'month': ['1', '2', '2', '3', '3'],
                   'price': [10.2, 11, 13.2, 14.3, 23.5]})
print(data2)

data3 = data2.set_index(['year', 'month'])
print(data3)

# 按照层级统计数据
data4 = data3.sum(level='year')
print(data4)


