# coding=UTF-8
from core.service.DataPredictService import DataPredictService
from core.service.DataProcessService import DataProcessService
import time


class CategoryMatchService(object):

    def categoryDataFit(self):
        start = time.time()
        # 训练数据源
        # xDatas, yDatas = self.dataPostgreSQL()
        dataProcessService = DataProcessService()
        xDatas, yDatas = dataProcessService.dataMongoDB()

        centre = time.time()
        print("获取数据源耗时：{}".format(centre - start))
        # 预测
        dataProcessService = DataPredictService()
        dataProcessService.dataFit(xDatas, yDatas)

    def categorydataPredict(self, title):
        # 预测
        dataProcessService = DataPredictService()
        result = dataProcessService.dataPredict(title)
        categoryGroup = result[0]
        categoryGroup = categoryGroup.replace('-', ',')
        dataProcessService = DataProcessService()

        return result

    def batchCategorydataPredict(self, title):
        # 预测
        dataProcessService = DataPredictService()
        result = dataProcessService.batchDataPredict(title)
        return result

    def batchCategorydataPredict2(self, title):
        # 预测
        dataProcessService = DataPredictService()
        result = dataProcessService.batchDataPredict2(title)
        return result

    def categoryDataBatchFit(self,num):
        start = time.time()
        # 批次训练数据源
        # xDatas, yDatas = self.dataPostgreSQL()
        dataProcessService = DataProcessService()
        xDatas, yDatas = dataProcessService.dataMongoDB()

        centre = time.time()
        print("获取数据源耗时：{}".format(centre - start))
        # 预测
        dataProcessService = DataPredictService()
        dataProcessService.dataBatchFit(xDatas, yDatas, num)


    def categoryDataBatchFit2(self,num):
        start = time.time()
        # 批次训练数据源
        # xDatas, yDatas = self.dataPostgreSQL()
        dataProcessService = DataProcessService()
        xDatas, yDatas = dataProcessService.dataMongoDB2()
        yAll = dataProcessService.allCategorydataMongoDB2()
        centre = time.time()
        print("获取数据源耗时：{}".format(centre - start))
        # 预测
        dataProcessService = DataPredictService()
        dataProcessService.dataBatchFit2(xDatas, yDatas,yAll, num)