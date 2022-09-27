import joblib


class DataPersistence(object):

    # 持久化数据
    def joblibDump(self, data, path):
        print("持久化数据:" + path)
        joblib.dump(data, path)

    # 取出持久化数据
    def joblibLoad(self, path):
        print("取出持久化数据:" + path)
        return joblib.load(path)
