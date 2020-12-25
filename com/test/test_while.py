# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# n = 1
# while n <= 5:
#     print(n)
#     n += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if (message != 'quit'):
#         print(message)

# break退出
# while True:
#     city =input()
#     if city=='quit':
#         break
#     else:
#         print(city.title())

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    else:
        print(num)

# while循环处理字典
# 函数pop() 以每次一个的方式从列表nums末尾删除数据
nums = [1, 2, 3]
while nums:
    num = nums.pop()
    print(num)

# remove
data_tool = ['hive', 'spark', 'spark sql', 'hadoop', 'flink']
while 'spark' in data_tool:
    data_tool.remove('spark')
print(data_tool)
