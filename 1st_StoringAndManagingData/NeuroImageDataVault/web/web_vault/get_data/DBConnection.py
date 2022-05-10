import psycopg2

class DBConnection(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self, database='project', user='postgres', password='19980806', port='5433'):
        # print(database, user, password, port)
        self.conn = psycopg2.connect(database=database, user=user, password=password, port=port)
        super().__init__()

    def get_conn(self):
        return self.conn
    def close_conn(self):
        self.conn.close()
conn = DBConnection().get_conn()

def excuteSql(sql, conn=conn):
    cur = conn.cursor()
    if type(sql) is list: 
        for one in sql:
            cur.execute(one)
    else:
        cur.execute(sql)
    raw = cur.fetchall()

    conn.commit()
    return raw

def getData(sql, cols, conn=conn):
    raw = excuteSql(sql)
    data = []
    for rawitem in raw:
        item = {}
        for i, col in enumerate(cols):
            item[col] = rawitem[i]
        data.append(item)
    return data 