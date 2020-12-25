# 导入全部模块
# import pizza
#
# pizza.make_pizza(12, 'AAA', 'BBB')

# 导入某个函数
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给函数起别名
from  pizza import make_pizza as mp
mp(12,'AAA')

# 使用as给模块起别名
import pizza as p
p.make_pizza(12,'ssss')

# 使用*导入模块中的全部函数
from pizza import *
make_pizza(11,'aaaa')



