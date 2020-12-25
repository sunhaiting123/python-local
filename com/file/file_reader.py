with open('../../test_file/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())

# 逐行读取
with open('../../test_file/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
        # print(line, end='')
# 创建一个包含文件各行内容的列表
with open('../../test_file/pi_digits.txt') as file_object:
    # 方法readlines() 从文件中读取每一行，并将其存储在一个列表中；
    lines = file_object.readlines()

pi_str = ''
for line in lines:
    pi_str += line.rstrip()
    # print(line.rstrip())
print(pi_str)

# 向文件中写入数据
with open('C:/Users/xm/Desktop/program.txt', 'w') as file_object:
    file_object.write('I love programming1.\n')
    file_object.write('I love programming2.\n')

# 向已有的文件中写入数据
with open('C:/Users/xm/Desktop/program.txt', 'a') as file_object:
    file_object.write('I love programming3.\n')
    file_object.write('I love programming4.\n')


