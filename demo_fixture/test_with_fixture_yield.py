"""
Not only test with pytest.fixture 
but use "yield" so during fixture we can "clean up" the test data 
to make sure the test env is back to its initial state 
"""

# https://nedbatchelder.com/text/test3.html?fbclid=IwAR22T3xAZDymqErQzlloy876-OB1LwtpTB7hT8SLoR-B9oqCsd38fZvz2sU

import pytest 

class Product:
    def __init__(self):
        self.p = {}

    def add_prod(self, **kwargs):
        for k, v in kwargs.items():
            self.p[k] = v

    def get_prod_size(self):
        return len(self.p)

    def get_product(self):
        return self.p

@pytest.fixture(scope="module")
def setup_product():
    p = Product()
    p.add_prod(milk = 100)
    p.add_prod(banana = 30)
    p.add_prod(cheese = 70)
    yield p 
    p = Product()

def test_get_prod_size(setup_product):
    prod_size = setup_product.get_prod_size()
    assert prod_size == 3 

def test_get_product(setup_product):
    prod = setup_product.get_product()
    assert prod == {'banana': 30, 'cheese': 70, 'milk': 100} 

def test_product_sum(setup_product):
    prod = setup_product.get_product()
    assert sum(prod.values()) == 200 

if __name__ == '__main__':
    pytest.main([__file__])
