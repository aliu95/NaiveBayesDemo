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
    title = 'Acrylic Nail Kit Acrylic Powder and Liquid Set Nail Art Crystal Powder Liquid Monomer for Acrylic Nails Extension Carving'
    categoryMatchService = CategoryMatchService()
    result = categoryMatchService.batchCategorydataPredict2(title)
    dataProcessService = DataProcessService()
    result2 = dataProcessService.findCategroyList(','.join(result))
    resu = {'code': 200, 'categoryId': result, 'categoryList': result2}  # 返回数据
    print(resu)
    print(result2)
    end = time.time()
    print("总耗时：{}".format(end - start))