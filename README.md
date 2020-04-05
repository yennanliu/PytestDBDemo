# PytestDemo

## Intro
- Unittest/test demo in python via [pytest](https://docs.pytest.org/en/latest/)

## Context
- pytest with fixtures
	- Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.
	- Origin test : [test_mydb.py](https://github.com/yennanliu/PytestDemo/blob/master/test_mydb.py)
	- Modify with setup - tear down : [test_mydb_setup_teardown.py](https://github.com/yennanliu/PytestDemo/blob/master/test_mydb_setup_teardown.py)
	- Modify with `pytest fixtures` : [test_my_db_fixtures.py](https://github.com/yennanliu/PytestDemo/blob/master/test_my_db_fixtures.py)
- pytest with parametrize
	- `@pytest.mark.parametrize` allows one to define multiple sets of arguments and fixtures at the test function or class.
	- Origin test : [test_mymath.py](https://github.com/yennanliu/PytestDemo/blob/master/parametrize/test_mymath.py)
	- Modiffy with parametrize : [test_mymath_parametrize.py](https://github.com/yennanliu/PytestDemo/blob/master/parametrize/test_mymath_parametrize.py)

## Quick start 
```bash
# install package
pip install -r requirements.txt
# run the tests
pytest -v 
# run the tests & and see # of func called 
pytest --capture=no
# run on sungle test
pytest -k parametrize/test_mymath_parametrize.py
```

## Ref 
- Getting started
	- https://nedbatchelder.com/text/test3.html?fbclid=IwAR22T3xAZDymqErQzlloy876-OB1LwtpTB7hT8SLoR-B9oqCsd38fZvz2sU
	- https://realpython.com/tutorials/testing/
- Mock
	- https://realpython.com/python-mock-library/#patch
- fixture
	- https://docs.pytest.org/en/latest/fixture.html
- interface
	- https://realpython.com/python-interface/
- Modify from 
	- https://www.youtube.com/watch?v=IVrGz8w0H8c
	- https://github.com/codebasics/py/tree/master/unittesting_pytest
