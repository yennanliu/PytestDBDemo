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

@pytest.fixture(scope="module")
def setup_product():
    p = Product()
    p.add_prod(milk = 100)
    p.add_prod(banana = 30)
    p.add_prod(cheese = 70)
    return p 

def test_product_lengh(setup_product):
    prod_size = setup_product.get_prod_size()
    assert prod_size == 3 

if __name__ == '__main__':
    pytest.main([__file__])
