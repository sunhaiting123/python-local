from com.entity.battery import Battery
from com.entity.car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 调用父类的方法
        super().__init__(make, model, year)
        # 添加特有属性
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

    # # 添加特有方法
    # def describe_battery(self):
    #     """打印一条描述电瓶容量的消息"""
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # 重写父类的方法
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
