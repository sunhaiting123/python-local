import copy

"""
copy.copy(a) 浅拷贝：不拷贝子对象的内容，只是拷贝子对象的引用。
copy.deepcopy(a) 深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象
传递不可变对象时。不可变对象里面包含的子对象是可变的。则方法内修改了这个可变对象，源对象也发生了变化。
可变参数指的是“可变数量的参数”。分两种情况：
1. *param（一个星号），将多个参数收集到一个“元组”对象中。
2. **param（两个星号），将多个参数收集到一个“字典”对象中。
nonlocal 用来声明外层的局部变量。
global 用来声明全局变量。
"""


def testCopy():
    '''测试浅拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.copy(a)
    print("a", a)
    print("b", b)
    b.append(30)
    b[2].append(7)
    print("浅拷贝......")
    print("a", a)
    print("b", b)


def testDeepCopy():
    '''测试深拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)
    print("a", a)
    print("b", b)
    b.append(30)
    b[2].append(7)
    print("深拷贝......")
    print("a", a)
    print("b", b)


testCopy()
print("*************")
testDeepCopy()

# 传递不可变对象时。不可变对象里面包含的子对象是可变的。则方法内修改了这个可变对象，源对象也发生了变化。
a = (10, 20, [5, 6])
print("a:", id(a))


def test01(m):
    print("m:", id(m))
    m[2][0] = 888
    print(m)
    print("m:", id(m))


test01(a)
print(a)


def f1(a, b, *c):
    print(a, b, c)


def f2(a, b, **c):
    print(a, b, c)


def f3(a, b, *c, **d):
    print(a, b, c, d)


f1(8, 9, 19, 20)
f2(8, 9, name='gaoqi', age=18)
f3(8, 9, 20, 30, name='gaoqi', age=18)

s = "print('abcde')"
eval(s)
a = 10
b = 20
c = eval("a+b")
print(c)
dict1 = dict(a=100, b=200)
d = eval("a+b", dict1)
print(d)

# 测试nonlocal、global 关键字的用法
a = 100


def outer():
    b = 10

    def inner():
        nonlocal b  # 声明外部函数的局部变量
        print("inner b:", b)
        b = 20
        global a  # 声明全局变量
        a = 1000

    inner()
    print("outer b:", b)


outer()
print("a：", a)



str = "global"
def outer():
    str = "outer"
    def inner():
        str = "inner"
        print(str)
    inner()
    print(str)
outer()
print(str)
