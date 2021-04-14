#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Description : 
@Author : sunhaiting
@Date : 2021/2/23 15:52 
"""
import random

import numpy as np


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m, n = np.shape(dataMatrix)
    weight = np.ones(n)
    for i in range(numIter):
        dataIndex = list(range(m))
        for j in range(m):
            alpha = 4.0 / (1 + i + j) + 0.01
            randomIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randomIndex] * weight))
            error = classLabels[randomIndex] - h
            weight = weight + alpha * dataMatrix[randomIndex] * error
            del (dataIndex[randomIndex])
    return weight

"""
梯度下降法
"""


def gradAscent(dataMatIn, classLabels):
    dataMat = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m, n = np.shape(dataMat)
    weight = np.ones((n, 1))
    alpha = 0.001  # 移动步长,也就是学习速率,控制更新的幅度。
    maxCycles = 500  # 最大迭代次数
    for i in range(maxCycles):
        h = sigmoid(dataMat * weight)
        error = labelMat - h
        weight = weight + alpha * dataMat.transpose() * error
    return weight.getA()


def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0

"""
使用随机梯度下降法
"""
def colicTest():
    frTrain = open("horseColicTraining.txt")
    frTest = open("horseColicTest.txt")
    trainData = []
    trainLabel = []
    for line in frTrain.readlines():
        curLine = line.strip().split("\t")
        dataArr = []
        for i in range(len(curLine) - 1):
            dataArr.append(float(curLine[i]))
        trainData.append(dataArr)
        trainLabel.append(float(curLine[-1]))
    weight = stocGradAscent1(np.array(trainData), trainLabel, 500)

    errorCount = 0
    numTestCount = 0.0
    for line in frTest.readlines():
        numTestCount += 1
        testLine = line.strip().split("\t")
        testArr = []
        for i in range(len(testLine) - 1):
            testArr.append(float(testLine[i]))
        proLabel = int(classifyVector(np.array(testArr), weight))
        if proLabel != int(testLine[-1]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestCount) * 100  # 错误率计算
    print("测试集错误率为: %.2f%%" % errorRate)


"""
使用梯度下降法
"""
def colicTest1():
    frTrain = open("horseColicTraining.txt")
    frTest = open("horseColicTest.txt")
    trainData = []
    trainLabel = []
    for line in frTrain.readlines():
        curLine = line.strip().split("\t")
        dataArr = []
        for i in range(len(curLine) - 1):
            dataArr.append(float(curLine[i]))
        trainData.append(dataArr)
        trainLabel.append(float(curLine[-1]))
    weight = gradAscent(np.array(trainData), trainLabel)

    errorCount = 0
    numTestCount = 0.0
    for line in frTest.readlines():
        numTestCount += 1
        testLine = line.strip().split("\t")
        testArr = []
        for i in range(len(testLine) - 1):
            testArr.append(float(testLine[i]))
        proLabel = int(classifyVector(np.array(testArr), weight[:,0]))
        if proLabel != int(testLine[-1]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestCount) * 100  # 错误率计算
    print("测试集错误率为: %.2f%%" % errorRate)



if __name__ == '__main__':
    colicTest1()
