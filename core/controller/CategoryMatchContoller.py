# coding=UTF-8
import sys
sys.path.append("/home/la1976/data_matedemp/matedemp/")
import flask
import json
from flask import request
import time
import numpy as np
from core.service.CategoryMatchService import CategoryMatchService
from core.service.DataProcessService import DataProcessService

server = flask.Flask(__name__)

@server.route('/batchFit', methods=['get', 'post'])
def batchFit():

    print("测试开始建立数据模型")

    print("测试匹配数据开始")
    # 导入time模块
    start = time.time()
    title = 'Alignment Timing Tool Set For Benz AMG 156'
    categoryMatchService = CategoryMatchService()
    result = categoryMatchService.batchCategorydataPredict(title)
    end = time.time()
    print("总耗时：{}".format(end - start))

    print("总耗时：{}".format(end - start))
    resu = {'code': 200, 'desc': 'succee'}  # 返回数据

    print(resu)

    return json.dumps(resu)  # 将字典转换为json串, json是字符串


@server.route('/fit', methods=['get', 'post'])
def fit():

    print("测试开始建立数据模型")

    # 导入time模块
    start = time.time()
    categoryMatchService = CategoryMatchService()
    categoryMatchService.categoryDataFit()
    end = time.time()

    print("总耗时：{}".format(end - start))
    resu = {'code': 200, 'desc': 'succee'}  # 返回数据

    print(resu)

    return json.dumps(resu)  # 将字典转换为json串, json是字符串


@server.route('/predict', methods=['get', 'post'])
def predict():
    # 获取通过url请求传参的数据
    title = request.args.get('title')

    # 这里可以加入核心功能代码
    categoryMatchService = CategoryMatchService()
    result = categoryMatchService.categorydataPredict(title)
    resu = {'code': 200, 'categoryId': result[0]}  # 返回数据

    print(resu)

    return json.dumps(resu)  # 将字典转换为json串, json是字符串


@server.route('/batchPredict', methods=['get', 'post'])
def batchPredict():
    # 获取通过url请求传参的数据
    title = request.args.get('title')

    # 这里可以加入核心功能代码
    categoryMatchService = CategoryMatchService()
    result = categoryMatchService.batchCategorydataPredict(title)
    print(result)
    dataProcessService = DataProcessService()
    result2 = dataProcessService.findCategroyList(result[0])
    resu = {'code': 200, 'categoryId': result[0], 'categoryList': result2}  # 返回数据
    print(resu)

    return json.dumps(resu)  # 将字典转换为json串, json是字符串


if __name__ == '__main__':
    server.run(debug=True, port=80, host='0.0.0.0')  # 指定端口、host设为0.0.0.0代表不管几个网卡，任何ip都可以访问


