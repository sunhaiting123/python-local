#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Description : 
@Author : sunhaiting
@Date : 2021/1/25 11:40 
"""

import numpy as np
from functools import reduce


def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表侮辱性词汇，0代表不是
    return postingList, classVec


"""
整理样本集合成set格式
"""


def createVocabList(dataset):
    vocabList = set([])
    for document in dataset:
        vocabList = vocabList | set(document)
    return list(vocabList)


"""
每个单词转换数字
word2Vec
"""


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


def trainNB0(trainMat, trainCategory):
    num1 = len(trainMat)
    num2 = len(trainMat[0])
    pAbusive = sum(trainCategory) / float(num1)  #文档属于侮辱类的概率
    p0Num = np.zeros(num2)
    p1Num = np.zeros(num2)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(num1):
        if trainCategory[i] == 1: #统计属于侮辱类的条件概率所需的数据，即P(w0|1),P(w1|1),P(w2|1)···
            p1Num += trainMat[i]
            p1Denom += sum(trainMat[i])
        else:
            p0Num += trainMat[i]
            p0Denom += sum(trainMat[i])
    p1Vect = p1Num / p1Denom  # 相除
    p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = reduce(lambda x, y: x * y, vec2Classify * p1Vec) * pClass1
    p0 = reduce(lambda x, y: x * y, vec2Classify * p0Vec) * (1 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    postingList, classVec = loadDataSet()
    vocabList = createVocabList(postingList)
    trainMat = []
    for data in postingList:
        trainMat.append(setOfWords2Vec(vocabList, data))
    print('trainMat:\n', trainMat)
    p0Vect, p1Vect, pAbusive = trainNB0(trainMat, classVec)
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = setOfWords2Vec(vocabList, testEntry)
    if classifyNB(thisDoc,p0Vect,p1Vect,pAbusive):
        print(testEntry,'属于侮辱类')
    else:
        print(testEntry, '属于非侮辱类')
    testEntry = ['stupid', 'garbage']  # 测试样本2
    thisDoc = np.array(setOfWords2Vec(vocabList, testEntry))  # 测试样本向量化
    if  classifyNB(thisDoc,p0Vect,p1Vect,pAbusive):
        print(testEntry, '属于侮辱类')  # 执行分类并打印分类结果
    else:
        print(testEntry, '属于非侮辱类')



if __name__ == '__main__':
    # postingList, classVec = loadDataSet()
    # vocabList = createVocabList(postingList)
    # trainMat = []
    # for data in postingList:
    #     trainMat.append(setOfWords2Vec(vocabList, data))
    # print('trainMat:\n', trainMat)
    # p0Num,p1Num,p0Vect, p1Vect, pAbusive = trainNB0(trainMat,classVec)
    # print(p0Num)
    # print(p1Num)
    # print(p0Vect)
    # print(p1Vect)
    # print(pAbusive)

    a = np.array([2, 2])
    b = np.array([1, 3])
    print(a * b)
    c = reduce(lambda x, y: x * y, a * b)
    print(c)

    testingNB()
