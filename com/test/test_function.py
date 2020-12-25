# 无参函数
def test():
    print("hello world")


test()


def get_name(name):
    print(name.title())


get_name('aaa')


# 关键字实参的顺序无关紧要，因为Python知道各个值该存储到哪个形参中
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hhh', 'aaa')
# 下面两个相同
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet(pet_name='willie', animal_type='cat')


# 带有返回值的函数
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 给某一个参数添加默认值，放在末尾
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# 返回值是字典类型
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# 参数是字典类型
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs,completed_models)
print(unprinted_designs)
# 切片表示法[:] 创建列表的副本。 不清空completed_models
print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)


# 　传递任意数量的实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    for topping in toppings:
        print(topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
