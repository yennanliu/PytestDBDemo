import pytest
from fixtures.mydb import MyDB

conn = None
cur = None

@pytest.fixture
def cur():
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    return cur

def test_employ_query1(cur):
    id = cur.execute("select id from employee where name=jim")
    assert id == 123

def test_employ_query2(cur):
    id = cur.execute("select id from employee where name=tom")
    assert id == 789

if __name__ == '__main__':
    pytest.main([__file__])
