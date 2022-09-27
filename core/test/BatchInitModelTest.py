# coding=UTF-8
import sys
sys.path.append("/home/la1976/data_matedemp/matedemp/")
from core.service.CategoryMatchService import CategoryMatchService
import time

if __name__ == '__main__':
    print("测试开始批次建立数据模型")
    # 导入time模块
    start = time.time()
    categoryMatchService = CategoryMatchService()
    categoryMatchService.categoryDataBatchFit(10000)
    end = time.time()
    print("总耗时：{}".format(end - start))