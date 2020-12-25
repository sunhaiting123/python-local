"""
1. @classmethod 必须位于方法上面一行
2. 第一个cls 必须有；cls 指的就是“类对象”本身；
3. 调用类方法格式：“类名.类方法名(参数列表)”。参数列表中，不需要也不能给cls 传值。
4. 类方法中访问实例属性和实例方法会导致错误
5. 子类继承父类方法时，传入cls 是子类对象，而非父类对象
方法没有重载

"""


class Student:
    company = "SXT"  # 类属性

    @classmethod
    def printCompany(cls):
        print(cls.company)

    @staticmethod
    def add(a, b):  # 静态方法
        print("{0}+{1}={2}".format(a, b, (a + b)))
        return a + b


Student.printCompany()
Student.add(10, 20)


class Employee:
    __company = "百战程序员"  # 私有类属性. 通过dir 可以查到_Employee__company

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有实例属性

    def say_company(self):
        print("我的公司是：", Employee.__company)  # 类内部可以直接访问私有属性
        print(self.name, "的年龄是：", self.__age)
        self.__work()

    def __work(self):  # 私有实例方法通过dir 可以查到_Employee__work
        print("工作！好好工作，好好赚钱，娶个媳妇！")


p1 = Employee("高淇", 32)
print(p1.name)
print(dir(p1))
p1.say_company()
print(p1._Employee__age)  # 通过这种方式可以直接访问到私有属性。通过dir 可以查到属性：_Employee__age
# print(p1.__age) #直接访问私有属性，报错
# p1.__work() #直接访问私有方法，报错

# @property 可以将一个方法的调用方式变成“属性调用”
class Employee:
    @property
    def salary(self):
        return 30000

    def __str__(self):
        print("====")


emp1 = Employee()
print(emp1.salary)  # 打印30000
print(type(emp1.salary))  # 打印<class 'int'>
# emp1.salary() #报错：TypeError:
