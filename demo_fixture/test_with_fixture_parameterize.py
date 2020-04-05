

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

@pytest.mark.parametrize("prod_name, prod_value", 
                        [

                            ("milk" ,100),
                            ("banana", 30),
                            ("cheese", 70)

                        ]
                        )
def test_get_prod_size(setup_product, prod_name, prod_value):
    setup_product.add_prod(prod_name=prod_value)
    size = setup_product.get_prod_size()
    ### TO FIX : shoule be assert size == 3 
    assert size == 4

if __name__ == '__main__':
    pytest.main([__file__])
