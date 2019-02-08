import unittest
from unittest.mock import patch

import pysqldict
from pysqldict import SqlDict


class PackageTestCase(unittest.TestCase):
    def test_open(self):
        db = pysqldict.open(':memory:')
        self.assertTrue(isinstance(db, SqlDict))


class SqlDictBasicTestCase(unittest.TestCase):

    def setUp(self):
        self.db = SqlDict(':memory:')

    def test_open(self):
        self.db._open()
        self.assertTrue(self.db.db)
        self.assertTrue(self.db.cursor)
        self.db._close()

    def test_close(self):
        self.db._open()
        self.db._close()
        self.assertIsNone(self.db.db)
        self.assertIsNone(self.db.cursor)

    def test_table(self):
        table = self.db.table('t1')
        self.assertTrue(table)


class SqlDictSqlTestCase(unittest.TestCase):

    def setUp(self):
        self.db = SqlDict(':memory:')
        self.db._open()

    def tearDown(self):
        self.db._close()

    @patch('pysqldict.SqlDict._create_table')
    def test_ensure_table_create(self, mock_create_table):
        self.db._ensure_table('t1', {'a': 1})
        self.assertTrue(mock_create_table.called)

    @patch('pysqldict.SqlDict._alter_table')
    def test_ensure_table_alter(self, mock_alter_table):
        self.db._ensure_table('t1', {'a': 1})
        self.db._ensure_table('t1', {'b': 2})
        self.assertTrue(mock_alter_table.called)

    def assertDbColumns(self, table_name, expected_columns):
        self.db.cursor.execute('PRAGMA table_info(%s)' % table_name)
        columns = self.db.cursor.fetchall()
        columns = [{'name': c['name'], 'type': c['type'], 'pk': c['pk']} for c in columns]
        columns.sort(key=lambda c:c['name'])
        self.assertListEqual(columns, expected_columns)

    def test_create_table(self):
        self.db._create_table('t1', {'int': 1, 'text': 'hello', 'float': 1.5})
        self.assertDbColumns('t1', [
            {'name': '_id', 'type': 'INTEGER', 'pk': 1},
            {'name': 'float', 'type': 'REAL', 'pk': 0},
            {'name': 'int', 'type': 'INTEGER', 'pk': 0},
            {'name': 'text', 'type': 'TEXT', 'pk': 0},
        ])

    def test_alter_table(self):
        self.db._create_table('t1', {'int2': 1})
        self.db._alter_table('t1', {'text2': 'hello', 'float2': 1.5})
        self.assertDbColumns('t1', [
            {'name': '_id', 'type': 'INTEGER', 'pk': 1},
            {'name': 'float2', 'type': 'REAL', 'pk': 0},
            {'name': 'int2', 'type': 'INTEGER', 'pk': 0},
            {'name': 'text2', 'type': 'TEXT', 'pk': 0},
        ])