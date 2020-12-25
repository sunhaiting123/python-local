class Battery():
    def __init__(self, battery_size=70):
        #初始化电瓶的属性
        self.battery_size =battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")



