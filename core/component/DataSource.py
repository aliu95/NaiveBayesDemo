import psycopg2


class PostGreHelper(object):
    def __init__(self, database=None, user="tomtop", password=None, host="192.168.221.61", port="5432"):
        self._cursor = None
        self._conn = None
        self._database = database
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._result = None

    def get_connection(self):
        self._conn = psycopg2.connect(database=self._database, user=self._user, password=self._password,
                                      host=self._host, port=self._port)

    # 关闭数据库连接
    def close_connection(self):
        # 事务提交
        self._conn.commit()
        # 关闭数据库连接
        self._cursor.close()
        self._conn.close()

    # 执行一条sql  带参数
    def execute_sql_params(self, sql, params):
        self._cursor = self._conn.cursor()
        try:
            print(f"当前执行sql：{sql}，参数：{params}")
            # 执行语句
            self._cursor.execute(sql, params)
        except psycopg2.Error as e:
            print(f"执行sql：{sql}，出错，错误原因：{e}")

    # 通用执行方法
    def execute_method(self, sql, params=None, method_name=None):
        # 获取连接
        self.get_connection()
        # 执行sql
        self.execute_sql_params(sql, params)
        if method_name is not None:
            # 查询单条
            if "find_one" == method_name:
                self._result = self._cursor.fetchone()
            # 查询全部
            elif "find_all" == method_name:
                self._result = self._cursor.fetchall()
        # 关闭数据库连接
        self.close_connection()

    # 查询单条
    def find_one(self, sql, params=None):
        self.execute_method(sql, params=params, method_name="find_one")
        return self._result

    # 查询所有
    def find_all(self, sql, params=None):
        self.execute_method(sql, params=params, method_name="find_all")
        return self._result

    # 插入
    def insert(self, sql, params=None):
        self.execute_method(sql, params=params)

    # 更新
    def update(self, sql, params=None):
        self.execute_method(sql, params=params)

    # 删除
    def delete(self, sql, params=None):
        self.execute_method(sql, params=params)