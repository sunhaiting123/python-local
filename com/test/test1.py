# print("sxt" * 3)
#
# print("aaa" \
#       "ccc")
# a = "to be or not to be"
# print(a[::-1])
#
# a = "名字是:{0},年龄是：{1}"
# print(a.format("aaa", 11))
#
# list = []
# for x in range(10, 80, 10):
#     list.append(x)
# print(list)

# 循环代码优化测试
import time

# start = time.time()
# for i in range(1000):
#     result = []
#     for m in range(10000):
#         result.append(i * 1000 + m * 100)
# end = time.time()
# print("耗时：{0}".format((end - start)))
# start2 = time.time()
# for i in range(1000):
#     result = []
#     c = i * 1000
#     for m in range(10000):
#         result.append(c + m * 100)
# end2 = time.time()
# print("耗时：{0}".format((end2 - start2)))


# gnt = {x for x in range(1, 100) if x % 9 == 0}
# for x in gnt:
#     print(x, end=' ')
# print()
# for x in gnt:
#     print(x, end=' ')
#
a = 100
b = 200
c = 300


def f1(a, b, c):
    print(a, b, c)
    print(locals())  # 打印输出的局部变量
    print("#" * 20)
    print(globals())  # 打印输出的全局变量


f1(2, 3, 4)
