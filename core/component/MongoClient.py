import pymongo


class MongoClient(object):
    def __init__(self, database='matedatas', table=None, user=None, password=None, host="192.168.221.61",
                 port=27017):
        self._cursor = None
        self._database = database
        self._table = table
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._result = None

    def get_connection(self):
        client = pymongo.MongoClient(host=self._host, port=self._port)
        db = client[self._database]
        collection = db[self._table]
        return collection
