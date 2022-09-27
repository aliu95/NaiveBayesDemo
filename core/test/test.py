
# 建立数据
def dataBuild():
    data_all = [{"tag": "运动装", "desc": "限量款球鞋"},
                {"tag": "运动装", "desc": "李宁运动鞋"},
                {"tag": "食物", "desc": "海南大香蕉"},
                {"tag": "食物", "desc": "海南大桃子"},
                {"tag": "厨具", "desc": "很大的金铲铲"},
                {"tag": "厨具", "desc": "不锈钢刀叉"},
                {"tag": "玩具", "desc": "变形金刚灭霸"},
                {"tag": "玩具", "desc": "手动遥控飞机"},
                {"tag": "灯具", "desc": "方形电灯"},
                {"tag": "灯具", "desc": "长形状的电棒"},
                {"tag": "家具", "desc": "真皮的沙发"},
                {"tag": "家具", "desc": "彩色的电视机"},
                {"tag": "花草", "desc": "一朵玫瑰花"},
                {"tag": "花草", "desc": "一束兰花"},
                {"tag": "食物", "desc": "新鲜的芒果"}, ]

    x = []
    y = []
    for data in data_all:
        tag = data.get("tag")
        desc = data.get("desc")
        wordArr = WordSplit.stripdata(desc)
        x.append(wordArr)
        y.append(tag)
    return x, y


def dataPostgreSQL():
    # 查询多条测试
    sql = "SELECT t.ctitle,c.icategorys " \
          "FROM (" \
          "SELECT c.clistingid,GROUP_CONCAT(c.icategory) AS icategorys FROM t_product_category_mapper c WHERE 1=1 GROUP BY clistingid" \
          ") c " \
          "LEFT JOIN t_product_translate t  on t.clistingid = c.clistingid " \
          "WHERE " \
          "t.ilanguageid = 1 " \
          "LIMIT 1000"
    pg_helper = PostGreHelper(database="product_tmp", password="tomtop")
    result = pg_helper.find_all(sql)
    x = []
    y = []
    wordSplit = WordSplit()
    for data in result:
        wordArr = wordSplit.stripdata(data[0])
        s = '-'.join(str(i) for i in data[1])
        x.append(wordArr)
        y.append(s)
        # x.append(wordArr)
        # y.append(tag)
    return x, y

