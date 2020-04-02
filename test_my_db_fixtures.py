import pytest
from fixtures.mydb import MyDB

conn = None
cur = None

# @pytest.fixture(scope="module") # make sure the cur only called once (module level) 
# def cur():
#     print ("setting up")
#     db = MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#     return cur

@pytest.fixture(scope="module") # make sure the cur only called once (module level) 
def cur():
    print ("setting up")
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    # yield cursor so can run the close op later
    yield cur
    cur.close()
    conn.close()
    print ("close DB")

def test_employ_query1(cur):
    id = cur.execute("select id from employee where name=jim")
    assert id == 123

def test_employ_query2(cur):
    id = cur.execute("select id from employee where name=tom")
    assert id == 789

if __name__ == '__main__':
    pytest.main([__file__])
