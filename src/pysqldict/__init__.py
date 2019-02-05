from .sqldict import SqlDict

__version__ = '0.1.0'


def open(filename=':memory:'):
    return SqlDict(filename)
