import sys
sys.path.append("/home/la1976/data_matedemp/matedemp/")
from core.service.DataProcessService import DataProcessService

if __name__ == '__main__':
    # 初始化mongo数据测试类

    # 初始化mongo数据
    dataProcessService = DataProcessService()
    # 获取数据库数据
    datas = dataProcessService.dataPostgreSQL('0', '100000')

    # 同步到mongo
    initGoodsInfoService = dataProcessService.moveMongo(datas)
    print('数据已同步到MongoDB')
