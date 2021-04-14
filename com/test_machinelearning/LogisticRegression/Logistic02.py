#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Description : 
@Author : sunhaiting
@Date : 2021/2/23 15:52 
"""
import numpy as np
import random
import matplotlib.pyplot as plt


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


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open("testSet.txt")
    for line in fr.readlines():
        lineArr = line.strip().split("\t")
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    fr.close()
    return dataMat, labelMat


def plotBestFit(weights):
    dataMat, labelMat = loadDataSet()
    dataArr = np.array(dataMat)
    n = np.shape(dataMat)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    # fig = plt.figure()
    # ax = fig.add_subplot(111)  # 添加subplot
    # ax.scatter(xcord1, ycord1, s=20, c='red', marker='s', alpha=.5)  # 绘制正样本
    # ax.scatter(xcord2, ycord2, s=20, c='green', alpha=.5)  # 绘制负样本
    # plt.title('DataSet')  # 绘制title
    # plt.xlabel('x')
    # plt.ylabel('y')  # 绘制label
    # plt.show()  # 显示
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 添加subplot
    ax.scatter(xcord1, ycord1, s=20, c='red', marker='s', alpha=.5)  # 绘制正样本
    ax.scatter(xcord2, ycord2, s=20, c='green', alpha=.5)  # 绘制负样本
    x = np.arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.title('BestFit')  # 绘制title
    plt.xlabel('X1')
    plt.ylabel('X2')  # 绘制label
    plt.show()


if __name__ == '__main__':
    dataMat, labelMat = loadDataSet()
    weights = stocGradAscent1(np.array(dataMat), labelMat)
    plotBestFit(weights)
