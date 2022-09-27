# coding=UTF-8
import numpy as np
import time

from core.component.DataPersistence import DataPersistence
from core.component.NaiveBayes2 import NaiveBayes2
from core.component.WordSplit import WordSplit
from numpy import *
from functools import reduce


class DataPredictService(object):

    def __init__(self, path='F:/pythondata/allWordsVec.pkl', batchPath='F:/pythondata/batchAllWordsVec.pkl', batchPath2='F:/pythondata/batchAllWordsVec2.pkl'):
        self.path = path
        self.batchPath = batchPath
        self.batchPath2 = batchPath2

    def dataFit(self, xDatas, yDatas):

        # 此处生成的单词向量是不重复的
        allWordsVec = self.doc2VecList(xDatas)

        # 单词向量数据进行持久化
        dataPersistence = DataPersistence()
        dataPersistence.joblibDump(allWordsVec, self.path)

        # 数据输出为数字矩阵
        print("数据整理为数字矩阵开始")
        trainMat = list(map(lambda x: self.words2Vec(allWordsVec, x), xDatas))
        print("数据整理为数字矩阵成功")

        # 训练数据源
        naiveBayes2 = NaiveBayes2()
        result = naiveBayes2.fit2(trainMat, yDatas)

        # 打印结果日志
        # for i in range(len(yDatas)):
        #     if yDatas[i] == '1861-1860':
        #         a = trainMat[i]
        #         print(xDatas[i])
        #         print(trainMat[i])

        return result

    def dataBatchFit(self, xDatas, yDatas, num):

        # 此处生成的单词向量是不重复的
        allWordsVec = self.doc2VecList(xDatas)

        # 单词向量数据进行持久化
        dataPersistence = DataPersistence()
        dataPersistence.joblibDump(allWordsVec, self.batchPath)

        # 数据切割为num长度数组
        dataCount = len(yDatas)
        arrNum = int(dataCount/num)
        xDatasGroup=[]
        yDatasGroup=[]
        if arrNum ==0:
            xDatasGroup.append(xDatas)
            xDatasGroup.append(yDatas)
        else:
            xDatasGroup = np.array_split(np.array(xDatas), arrNum)
            yDatasGroup = np.array_split(np.array(yDatas), arrNum)

        for i in range(len(yDatasGroup)):
            xDatasUnitGroup = xDatasGroup[i]
            yDatasUnitGroup = yDatasGroup[i]

            print('整理数字矩阵')
            # 数据输出为数字矩阵
            trainMatUnit = list(map(lambda x: self.words2Vec(allWordsVec, x), xDatasUnitGroup))

            # 训练数据源
            naiveBayes2 = NaiveBayes2()
            naiveBayes2.batchfit2(trainMatUnit, yDatasUnitGroup, yDatas, i)
            print("已经训练完成" + str((i+1) * num) + '条数据')


    def dataBatchFit2(self, xDatas, yDatas,yAll, num):

        # 此处生成的单词向量是不重复的
        allWordsVec = self.doc2VecList(xDatas)

        # 单词向量数据进行持久化
        dataPersistence = DataPersistence()
        dataPersistence.joblibDump(allWordsVec, self.batchPath2)

        # 数据切割为num长度数组
        dataCount = len(yDatas)
        arrNum = int(dataCount/num)
        xDatasGroup=[]
        yDatasGroup=[]
        if arrNum ==0:
            xDatasGroup.append(xDatas)
            xDatasGroup.append(yDatas)
        else:
            xDatasGroup = np.array_split(np.array(xDatas), arrNum)
            yDatasGroup = np.array_split(np.array(yDatas), arrNum)

        for i in range(len(yDatasGroup)):
            xDatasUnitGroup = xDatasGroup[i]
            yDatasUnitGroup = yDatasGroup[i]

            print('整理数字矩阵')
            # 数据输出为数字矩阵
            trainMatUnit = list(map(lambda x: self.words2Vec(allWordsVec, x), xDatasUnitGroup))

            # 训练数据源
            naiveBayes2 = NaiveBayes2()
            naiveBayes2.batchfit22(trainMatUnit, yDatasUnitGroup, yAll, i)
            print("已经训练完成" + str((i+1) * num) + '条数据')


    def dataPredict(self, test):
        # 检索参数分词
        wordSplit = WordSplit()
        testWords = wordSplit.stripdata(test)

        # 单词向量数据进行取出
        dataPersistence = DataPersistence()
        allWordsVec = dataPersistence.joblibLoad(self.path)

        # 整理参数为数值
        testWordsMat = list(map(lambda x: self.words2Vec(allWordsVec, x), [testWords]))

        # 匹配分类
        naiveBayes2 = NaiveBayes2()
        result = naiveBayes2.predict2(testWordsMat)
        return result
    
    def batchDataPredict(self, test):
        # 检索参数分词
        wordSplit = WordSplit()
        testWords = wordSplit.stripdata(test)

        # 单词向量数据进行取出
        dataPersistence = DataPersistence()
        allWordsVec = dataPersistence.joblibLoad(self.batchPath)

        # 整理参数为数值
        testWordsMat = list(map(lambda x: self.words2Vec(allWordsVec, x), [testWords]))

        # 匹配分类
        naiveBayes2 = NaiveBayes2()
        result = naiveBayes2.batchPredict2(testWordsMat)
        return result

    def batchDataPredict2(self, test):
        # 检索参数分词
        wordSplit = WordSplit()
        testWords = wordSplit.stripdata(test)

        # 单词向量数据进行取出
        dataPersistence = DataPersistence()
        allWordsVec = dataPersistence.joblibLoad(self.batchPath2)

        # 整理参数为数值
        testWordsMat = list(map(lambda x: self.words2Vec(allWordsVec, x), [testWords]))

        # 匹配分类
        naiveBayes2 = NaiveBayes2()
        result = naiveBayes2.batchPredict22(testWordsMat)
        return result

    def doc2VecList(self, docList):
        start = time.time()
        print('开始整理单词量')
        # 从第一个和第二个集合开始进行并集操作，最后返回一个不重复的并集
        words = list(reduce(lambda x, y: set(x) | set(y), docList))
        end = time.time()
        print("整理单词量成功总耗时：{}".format(end - start))
        return words

    def words2Vec(self, vecList, inputWords):
        """把单子转化为词向量"""
        # 转化成以一维数组
        resultVec = [0] * len(vecList)
        for word in inputWords:
            if word in vecList:
                # 在单词出现的位置上的计数加1
                resultVec[vecList.index(word)] += 1
            else:
                print('没有发现此单词')

        return array(resultVec)
