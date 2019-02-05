import sqlite3


class SqlDict(object):
    def __init__(self, filename):
        self.dbname = filename

    def open(self):
        self.db = sqlite3.connect(self.dbname)
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()

    def table(self, table_name):
        return SqlDictTable(self, table_name)

    def ensure_table(self, table_name, data):
        pass

    def insert_data(self, table_name, data):
        sql = "INSERT INTO `%s` (%s) VALUES (%s)" % (
            table_name,
            ', '.join("`%s`" % k for k in data.keys()),
            ', '.join(['?'] * len(data)),
        )
        print(sql)


class SqlDictTable(object):
    def __init__(self, db, table_name):
        self.db = db
        self.table_name = table_name

    def put(self, data):
        self.db.ensure_table(self.table_name, data)
        self.db.insert_data(self.table_name, data)
    
    def get(self, **args):
        pass

    def filter(self, **args):
        pass