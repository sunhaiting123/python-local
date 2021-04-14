#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Description : 
@Author : sunhaiting
@Date : 2021/2/22 19:53 
"""
import numpy as np
import matplotlib.pyplot as plt


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


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


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


if __name__ == '__main__':
    # data = [[1, 0], [2, 0], [3, 0]]
    # data1 = np.array(data)
    # print(data)
    # print(data1)
    # n = np.shape(data)[0]
    # n2 = data1.shape
    # print(n)
    # print(n2)
    # x = []
    # x.append(data[0][0])
    # # x.append(data[1,0])
    # # x.append(data[2,0])
    #
    # print(x)
    # plotDataSet()
    dataMat, labelMat = loadDataSet()
    print(gradAscent(dataMat, labelMat))
    weights = gradAscent(dataMat, labelMat)
    plotBestFit(weights)
