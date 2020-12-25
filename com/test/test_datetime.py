import time
from datetime import date

a = date.max
print(a)
b = date.min
print(b)
c = date.resolution
print(c)
d = date.today()
print(d)

e = date.fromtimestamp(time.time())
print(e)
dd1 = d.year
dd2 = d.month
dd3 = d.day
# 返回日期是星期几，[0, 6]，0表示星期一
dd4 = d.weekday()
# 返回日期是星期几，[1, 7], 1表示星期一
dd5 = d.isoweekday()
# 返回一个元组，格式为：(year, weekday, isoweekday)
dd6 = d.isocalendar()
# 返回'YYYY-MM-DD'格式的日期字符串
dd7 = d.isoformat()
dd8 = d.strftime('%Y/%m/%d')
dd9 = d.ctime()
print(dd1, dd2, dd3, dd4, dd5, dd6)
print(dd7, dd8, dd9)
dd10 = d.timetuple()
print(dd10)








