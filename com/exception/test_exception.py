# try-except 捕获异常数据   pass 失败时什么都不做
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        # 失败时什么都不做
        pass
        # print("You can't divide by 0!")
    else:
        print(answer)
