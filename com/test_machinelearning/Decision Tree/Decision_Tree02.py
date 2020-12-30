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


"""
函数说明:按照给定特征划分数据集

Parameters:
    dataSet - 待划分的数据集
    axis - 划分数据集的特征
    value - 需要返回的特征的值
Returns:
    比如：axis=0,value=0,第一列0的值去掉
    [0, 0, 0, 'no'],  
    [0, 0, 1, 'no'],
    [1, 0, 1, 'yes'],
    [1, 1, 0, 'yes'],
    [0, 0, 0, 'no']
"""


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            featVecData = featVec[:axis]
            featVecData.extend(featVec[axis + 1:])
            retDataSet.append(featVecData)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    baseEntropy = calcShannonEnt(dataSet)
    numFeatures = len(dataSet[0]) - 1
    bestFeature = -1
    bestGain = 0.0
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        featSet = set(featList)
        newEntroy = 0.0
        for value in featSet:
            subDataSet = splitDataSet(dataSet, i, value)
            pro = len(subDataSet) / float(len(dataSet))
            newEntroy += pro * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntroy
        print("第%d个特征的增益为%.3f" % (i, infoGain))
        if infoGain > bestGain:
            bestGain = infoGain
            bestFeature = i
    return bestFeature

if __name__ == '__main__':
    dataSet, labels = createDataSet()

    # shannonEnt = calcShannonEnt(dataSet)
    # print(shannonEnt)

    bestFeature = chooseBestFeatureToSplit(dataSet)
    print(bestFeature)