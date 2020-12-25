#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from os import listdir

from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
import operator
from sklearn.neighbors import KNeighborsClassifier as kNN

"""
@Description : 
@Author : sunhaiting
@Date : 2020/12/23 20:27 
"""

"""
函数说明:将32x32的二进制图像转换为1x1024向量。

Parameters:
    filename - 文件名
Returns:
    returnVect - 返回的二进制图像的1x1024向量

Modify:
    2017-07-15
"""


def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        line = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(line[j])
    return returnVect


def handwritingClassTest():
    # 训练集labels
    trainLabels = []
    # 获取训练集下的文件名
    trainNames = listdir("trainingDigits")
    trainLength = len(trainNames)
    trainMatr = np.zeros((trainLength, 1024))
    labels = []
    for i in range(trainLength):
        trainName = trainNames[i]
        # 获得分类器的数字
        classNumber = int(trainName.split("_")[0])
        # 添加到标签
        labels.append(classNumber)
        # 生成训练集
        trainMatr[i, :] = img2vector('trainingDigits/%s' % (trainName))
    neigh = kNN(n_neighbors=3, algorithm='auto')
    # 训练模型
    neigh.fit(trainMatr, labels)
    testFileNames = listdir("testDigits")
    testLength = len(testFileNames)
    errorCount = 0.0
    for i in range(testLength):
        testFileName = testFileNames[i]
        testClassNum = int(testFileName.split("_")[0])
        testVect = img2vector('testDigits/%s' % (testFileName))
        classResult = neigh.predict(testVect)
        print("分类器返回结果为%d\t真实结果为%d" % (classResult, testClassNum))
        if (testClassNum != classResult):
            errorCount += 1.0
        print("总共错了%d个数据\n错误率为%f%%" % (errorCount, errorCount / testLength * 100))


if __name__ == '__main__':
    handwritingClassTest()
