"""
 使用json.load() 将这个列表读取到内存中
 使用json.dump来存储数据
"""

import json

# numbers = [2, 3, 5, 7, 11, 13]
filename = 'C:/Users/xm/Desktop/numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)


with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)



