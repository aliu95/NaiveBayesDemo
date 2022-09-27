# coding=UTF-8
import jieba
import re


# 分词类
class WordSplit(object):

    # 中文分词
    def stripdata(self, desc):
        # print("源文档：" + Test)
        # jieba 默认启用了HMM（隐马尔科夫模型）进行中文分词
        seg_list = jieba.cut(desc)  # 分词
        line = ", ".join(seg_list)
        # print("去除停用词前："+line)
        word = self.stripword(line)
        # print("去除停用词后："+word)
        return word

    # 停用词分析
    def stripword(self,seg):

        # 获取停用词表
        stop = open(r'C:/Users/tomtop/Desktop/stopword2.txt', 'r+', encoding='utf-8')
        stopword = stop.read().split("\n")
        wordlist = []
        # 遍历分词表
        for key in seg.split(', '):
            # 去除停用词，去除单双字，去除重复词
            if not (key.strip() in stopword) and (len(key.strip()) > 2 and re.search('^[a-zA-Z\u4e00-\u9fa5]+$', key)):
                wordlist.append(key)

        # 停用词去除END
        stop.close()
        return wordlist
