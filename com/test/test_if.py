# if_else
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
print("结束。。。。")

# 字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# 给字典添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 定义空字典
a_1 = {}
a_1['x'] = 5
a_1['y'] = 4
print(a_1)

# 修改字典的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0 = {'color': 'yellow'}
print("The alien is " + alien_0['color'] + ".")

# 删除键值对
alien_1 = {'color': 'green', 'points': 5}
print(alien_1)
del alien_1['points']
print(alien_1)

# 使用字典存储
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(favorite_languages['sarah'].title())
print("Sarah's favorite language is " +
      favorite_languages['sarah'] +
      ".")

# 遍历字典
for key, value in favorite_languages.items():
    print("\nkey:" + key)
    print("value:" + value)
# 分别遍历字典的键,值
for key in favorite_languages.keys():
    print(key)
for value in favorite_languages.values():
    print(value)
# 去重
for value in set(favorite_languages.values()):
    print(value)

# 嵌套字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print("==========================")
# 字典添加元素 append
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")

# 修改字典某个值
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
print("========================")
for alien in aliens:
    print(alien)

# 字典中存储列表
dict = {}
dict['x'] = 1
dict['y'] = ['a', 'b', 'c']
print(dict['y'])
for value in dict['y']:
    # 不换行打印
    print(value, end='')

# 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
