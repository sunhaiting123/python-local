import  matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
#        ylabel='Y-Axis', xlabel='X-Axis')
# plt.show()

# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(224)

# plt.show()

# fig, axes = plt.subplots(nrows=2, ncols=2)
# axes[0,0].set(title='Upper Left')
# axes[0,1].set(title='Upper Right')
# axes[1,0].set(title='Lower Left')
# axes[1,1].set(title='Lower Right')
# plt.show()

# plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
# plt.xlim(0.5, 4.5)
# plt.show()


# x = np.linspace(0, np.pi)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# ax1.plot(x, y_sin)
# ax2.plot(x, y_sin, 'go--', linewidth=2, markersize=12)
# ax3.plot(x, y_cos, color='red', marker='+', linestyle='dashed')
# plt.show()


# x = np.linspace(0, 10, 200)
# data_obj = {'x': x,
#             'y1': 2 * x + 1,
#             'y2': 3 * x + 1.2,
#             'mean': 0.5 * x * np.cos(2*x) + 2.5 * x + 1.1}
#
# fig, ax = plt.subplots()
#
# #填充两条线之间的颜色
# ax.fill_between('x', 'y1', 'y2', color='yellow', data=data_obj)
#
# # Plot the "centerline" with `plot`
# ax.plot('x', 'mean', color='black', data=data_obj)
#
# plt.show()

# 散点图
# x = np.arange(10)
# y = np.random.randn(10)
# plt.scatter(x, y, color='red', marker='+')
# plt.show()

# 条形图
np.random.seed(1)
x = np.arange(5)
y = np.random.randn(5)

fig, axes = plt.subplots(ncols=2, figsize=plt.figaspect(1./2))

vert_bars = axes[0].bar(x, y, color='lightblue', align='center')
horiz_bars = axes[1].barh(x, y, color='lightblue', align='center')
#在水平或者垂直方向上画线
axes[0].axhline(0, color='gray', linewidth=2)
axes[1].axvline(0, color='gray', linewidth=2)
plt.show()