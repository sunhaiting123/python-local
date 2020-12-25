#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Description : 
@Author : sunhaiting
@Date : 2020/12/24 11:33 
"""
import math
from math import log
import numpy as np

def calcShannonEnt(dataSet):
    num = len(dataSet)
    labelCounts = {}
    for data in dataSet:
        curLabel = data[-1]
        if curLabel not in labelCounts:
            labelCounts[curLabel] = 1
        labelCounts[curLabel] += 1

    shannonEnt = 0.0
    for key in labelCounts:
        pro = float(labelCounts[key]) / num
        shannonEnt -= pro * math.log2(pro)
    return shannonEnt





def createDataSet():
    dataSet = [[0, 0, 0, 0, 'no'],  # 数据集
               [0, 0, 0, 1, 'no'],
               [0, 1, 0, 1, 'yes'],
               [0, 1, 1, 0, 'yes'],
               [0, 0, 0, 0, 'no'],
               [1, 0, 0, 0, 'no'],
               [1, 0, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [2, 0, 1, 2, 'yes'],
               [2, 0, 1, 1, 'yes'],
               [2, 1, 0, 1, 'yes'],
               [2, 1, 0, 2, 'yes'],
               [2, 0, 0, 0, 'no']]
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况']  # 分类属性
    return dataSet, labels  # 返回数据集和分类属性


if __name__ == '__main__':
    dataSet, labels = createDataSet()
    shannonEnt = calcShannonEnt(dataSet)
    print(shannonEnt)
