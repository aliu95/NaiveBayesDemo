# coding=UTF-8
import sys
sys.path.append("/home/la1976/data_matedemp/matedemp/")
from core.service.CategoryMatchService import CategoryMatchService
import time

if __name__ == '__main__':
    print("测试匹配数据开始")
    # 导入time模块
    start = time.time()
    title = 'plating Dress Cap Warm Hat Headwear With Ball Of Fluff'
    categoryMatchService = CategoryMatchService()
    result = categoryMatchService.categorydataPredict(title)
    end = time.time()
    print("总耗时：{}".format(end - start))
