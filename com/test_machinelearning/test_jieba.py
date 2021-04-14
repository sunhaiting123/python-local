#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Description : 
@Author : sunhaiting
@Date : 2021/1/26 20:27 
"""
import jieba
import numpy as np
# 全模式
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode:", "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode:", "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
#
#
# seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", cut_all=True)
# print("Full Mode:", ", ".join(seg_list))  # 全模式
#
#
# p1Num = np.zeros(3)
# print(p1Num)
# p1Num += [1,2,3]
# print(p1Num)
# p1Num +=[4,5,6]
# print(p1Num)


import random

list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a','a','b','b','b','b']
print(list1)
# random.shuffle(list1)
print(list1)
list3 = list(zip(list1, list2))
print(list3)
train_data_list, train_class_list = zip(*list3)
print(train_class_list)
print(train_data_list)
