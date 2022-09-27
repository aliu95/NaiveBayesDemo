# coding=UTF-8
import numpy as np
from numpy import *
from sklearn.naive_bayes import GaussianNB
from core.component.DataPersistence import DataPersistence



class NaiveBayes2(object):

    def __init__(self, path='F:/pythondata/dataModel.pkl', batchPath='F:/pythondata/batchDataModel.pkl', batchPath2='F:/pythondata/batchDataModel2.pkl'):
        self.path = path
        self.batchPath = batchPath
        self.batchPath2 = batchPath2

    def fit2(self, X, Y):
        print('开始建立模型')
        clf_Ga = GaussianNB()
        clf_Ga.fit(X, Y)
        print('模型建立完成。')
        
        # 持久化模型
        dataPersistence = DataPersistence()
        dataPersistence.joblibDump(clf_Ga, self.path)
        print('持久化数据完成')

    def batchfit2(self, X, Y,AllY, i):

        if i==0:
            print('开始建立模型')
            clf_Ga = GaussianNB()
            clf_Ga.partial_fit(X, Y, AllY)

            print('模型建立完成。')
            # 持久化模型
            dataPersistence = DataPersistence()
            dataPersistence.joblibDump(clf_Ga, self.batchPath)
            print('持久化数据完成')
        else:
            dataPersistence = DataPersistence()
            clf_Ga = dataPersistence.joblibLoad(self.batchPath)
            clf_Ga.partial_fit(X, Y, AllY)
            # 持久化模型
            dataPersistence = DataPersistence()
            dataPersistence.joblibDump(clf_Ga, self.batchPath)
            print('持久化数据完成')
            
    def batchfit22(self, X, Y,AllY, i):

        if i==0:
            print('开始建立模型')
            clf_Ga = GaussianNB()
            clf_Ga.partial_fit(X, Y, AllY)

            print('模型建立完成。')
            # 持久化模型
            dataPersistence = DataPersistence()
            dataPersistence.joblibDump(clf_Ga, self.batchPath2)
            print('持久化数据完成')
        else:
            dataPersistence = DataPersistence()
            clf_Ga = dataPersistence.joblibLoad(self.batchPath2)
            clf_Ga.partial_fit(X, Y, AllY)
            # 持久化模型
            dataPersistence = DataPersistence()
            dataPersistence.joblibDump(clf_Ga, self.batchPath2)
            print('持久化数据完成')


    def predict2(self, Z):
        dataPersistence = DataPersistence()
        clf_Ga = dataPersistence.joblibLoad(self.path)
        result = clf_Ga.predict(Z)
        print('匹配结果为')
        print(result)
        # classesList = clf_Ga.classes_
        # print(classesList)
        # result2 = clf_Ga.predict_proba(Z)
        # print(result2)
        return result

    def batchPredict2(self, Z):
        dataPersistence = DataPersistence()
        clf_Ga = dataPersistence.joblibLoad(self.batchPath)
        result = clf_Ga.predict(Z)
        print('匹配结果为')
        print(result)
        return result

    def batchPredict22(self, Z):
        dataPersistence = DataPersistence()
        clf_Ga = dataPersistence.joblibLoad(self.batchPath2)
        result = clf_Ga.predict(Z)
        classesList = clf_Ga.classes_
        pGroup = clf_Ga.predict_proba(Z)
        pList = pGroup[0]
        classesPredict = []
        for i in range(len(pList)):
            p = pList[i]
            classes = classesList[i]
            if p > 0:
                print('匹配结果为')
                print(p)
                print(classes)
                classesPredict.append(classes)
        print('匹配结果为')
        print(result)
        return classesPredict