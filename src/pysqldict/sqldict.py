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
        sql = "SELECT tbl_name FROM sqlite_master WHERE tbl_name=?"
        self.cursor.execute(sql, (table_name,))
        tbl = self.cursor.fetchone()

        if tbl is None:
            self.create_table(table_name, data)
        else:
            self.alter_table(table_name, data)

    def insert_data(self, table_name, data):
        sql = "INSERT INTO `%s` (%s) VALUES (%s)" % (
            table_name,
            ', '.join("`%s`" % k for k in data.keys()),
            ', '.join(['?'] * len(data)),
        )
        try:
            self.cursor.execute(sql, list(data.values()))
            self.cursor.execute('COMMIT')
        except sqlite3.OperationalError:
            self.ensure_table(table_name, data)
            self.cursor.execute(sql, data.values())

    def infer_columns_from_data(self, data):
        columns = []
        for k, v in data.items():
            if isinstance(v, str):
                column_type = 'TEXT'
            elif isinstance(v, int):
                column_type = 'INTEGER'
            elif isinstance(v, float):
                column_type = 'REAL'
            else:
                raise TypeError('Unsupported value type: %s' % type(v).__name__)
            columns.append((k, column_type))

        return columns

    def columns_to_sql(self, columns):
        return ', '.join('%s %s' % (k, v) for k, v in columns)

    def get_table_columns(self, table_name):
        sql = 'PRAGMA table_info(%s)' % table_name
        self.cursor.execute(sql)
        columns = self.cursor.fetchall()
        return {c[1]: c[2] for c in columns}

    def create_table(self, table_name, data):
        columns = self.infer_columns_from_data(data)
        sql = 'CREATE TABLE %s (_id INTEGER PRIMARY KEY AUTOINCREMENT, %s)' % (
            table_name, self.columns_to_sql(columns))
        self.cursor.execute(sql)

    def alter_table(self, table_name, data):
        columns = self.infer_columns_from_data(data)
        existing_columns = self.get_table_columns(table_name)
        columns = [c for c in columns if c[0] not in existing_columns]

        if columns:
            for column_name, column_type in columns:
                sql = 'ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type)
                self.cursor.execute(sql)


class SqlDictTable(object):
    def __init__(self, db, table_name):
        self.db = db
        self.table_name = table_name

    def put(self, data):
        self.db.open()
        self.db.insert_data(self.table_name, data)
        self.db.close()

    def get(self, **args):
        pass

    def filter(self, **args):
        pass
