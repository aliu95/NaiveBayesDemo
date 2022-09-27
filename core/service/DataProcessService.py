from core.component.DataSource import PostGreHelper
from core.component.MongoClient import MongoClient
from core.component.WordSplit import WordSplit


class DataProcessService:


    def moveMongo(self, datas):
        mongoClient = MongoClient(table='test_goods_datas')
        collection = mongoClient.get_connection()
        collection.insert_many(datas)
        print("数据同步至mongo成功")

    def findMongoData(self):
        mongoClient = MongoClient(table='test_goods_datas')
        collection = mongoClient.get_connection()
        rows = collection.find()
        return rows

    def dataMongoDB(self):
        datas = self.findMongoData()
        x = []
        y = []
        for row in datas:
            x.append(row['words'])
            y.append(row['categoryIds'])
        return x, y

    def dataPostgreSQL(self, start, end):
        # 查询多条测试
        sql3 = "SELECT a.ctitle,GROUP_CONCAT(a.category) FROM ( " \
                "SELECT b.clistingid,t.ctitle,c.icategory AS category FROM t_product_base AS b " \
                "LEFT JOIN t_product_translate AS t ON b.clistingid = t.clistingid AND t.ilanguageid = 1 " \
                "LEFT JOIN t_product_category_mapper_c2 c ON c.clistingid = b.clistingid AND c.ilanguageid = 1 " \
                "WHERE " \
                "b.iwebsiteid = 1 AND t.ctitle IS NOT NULL AND t.ctitle != ''  AND c.icategory IS NOT NULL " \
                ") a GROUP BY a.ctitle LIMIT 40000 OFFSET 0"


        pg_helper = PostGreHelper(database="product_tmp", password="tomtop")
        result = pg_helper.find_all(sql3)
        print("数据从数据库取出成功")
        datas = []
        wordSplit = WordSplit()
        for data in result:
            info = {}
            wordArr = wordSplit.stripdata(data[0])
            ids = sorted(data[1])
            s = ','.join(str(i) for i in ids)
            info['words'] = wordArr
            info['categoryIds'] = s
            datas.append(info)
        print("数据分词处理成功")
        return datas

    def findCategroyList(self, ids):
        sql = "SELECT icategoryid,cname FROM t_category_name_c2 WHERE icategoryid IN ("+ids+")"
        pg_helper = PostGreHelper(database="product_tmp", password="tomtop")
        result = pg_helper.find_all(sql)
        print("数据从数据库取出成功")
        return result




    def moveMongo2(self, datas):
        mongoClient = MongoClient(table='test_goods_datas2')
        collection = mongoClient.get_connection()
        collection.insert_many(datas)
        print("数据同步至mongo成功")

    def findMongoData2(self):
        mongoClient = MongoClient(table='test_goods_datas2')
        collection = mongoClient.get_connection()
        rows = collection.find()
        return rows

    def dataMongoDB2(self):
        datas = self.findMongoData2()
        x = []
        y = []
        for row in datas:
            x.append(row['words'])
            y.append(str(row['categoryIds']))
        return x, y

    def allCategorydataMongoDB2(self):
        # 查询多条测试
        sql3 = "SELECT a.category,count(1) FROM ( " \
               "SELECT t.ctitle,c.icategory AS category FROM t_product_base AS b " \
               "LEFT JOIN t_product_translate AS t ON b.clistingid = t.clistingid AND t.ilanguageid = 1 " \
               "LEFT JOIN t_product_category_mapper_c2 c ON c.clistingid = b.clistingid AND c.ilanguageid = 1 " \
               "WHERE " \
               "b.iwebsiteid = 1 AND t.ctitle IS NOT NULL AND t.ctitle != ''  AND c.icategory IS NOT NULL " \
               ") a GROUP BY a.category"

        pg_helper = PostGreHelper(database="product_tmp", password="tomtop")
        result = pg_helper.find_all(sql3)
        print("数据从数据库取出成功")
        datas = []
        for data in result:
            datas.append(str(data[0]))
        return datas

    
    def dataPostgreSQL2(self, start, end):
        # 查询多条测试
        sql3 = "SELECT t.ctitle,c.icategory AS category FROM t_product_base AS b " \
                "LEFT JOIN t_product_translate AS t ON b.clistingid = t.clistingid AND t.ilanguageid = 1 " \
                "LEFT JOIN t_product_category_mapper_c2 c ON c.clistingid = b.clistingid AND c.ilanguageid = 1 " \
                "WHERE " \
                "b.iwebsiteid = 1 AND t.ctitle IS NOT NULL AND t.ctitle != ''  AND c.icategory IS NOT NULL "


        pg_helper = PostGreHelper(database="product_tmp", password="tomtop")
        result = pg_helper.find_all(sql3)
        print("数据从数据库取出成功")
        datas = []
        wordSplit = WordSplit()
        for data in result:
            info = {}
            wordArr = wordSplit.stripdata(data[0])
            # ids = sorted()
            # s = ','.join(str(i) for i in ids)
            info['words'] = wordArr
            info['categoryIds'] = data[1]
            datas.append(info)
        print("数据分词处理成功")
        return datas