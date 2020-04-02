import pytest
from mydb import MyDB

def setup_module(module):
    global conn 
    global cur
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()

def teardown_module(module):
    cur.close()
    conn.close()

def test_employ_query1():
    id = cur.execute("select id from employee where name=jim")
    assert id == 123


def test_employ_query2():
    id = cur.execute("select id from employee where name=tom")
    assert id == 789

if __name__ == '__main__':
    pytest.main([__file__])
