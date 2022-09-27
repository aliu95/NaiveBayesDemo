# coding=UTF-8
import sys
sys.path.append("/home/la1976/data_matedemp/matedemp/")
from core.service.DataProcessService import DataProcessService
from core.service.CategoryMatchService import CategoryMatchService
import time

if __name__ == '__main__':
    print("测试匹配数据开始")
    # 导入time模块
    start = time.time()
    title = '1.44-inch TFT Touch Screen Kids Smart Watch Phone for Children Girls Boys'
    categoryMatchService = CategoryMatchService()
    result = categoryMatchService.batchCategorydataPredict(title)

    dataProcessService = DataProcessService()
    result2 = dataProcessService.findCategroyList(result[0])

    resu = {'code': 200, 'categoryId': result, 'categoryList': result2}  # 返回数据
    print(resu)
    print(result2)
    end = time.time()
    print("总耗时：{}".format(end - start))