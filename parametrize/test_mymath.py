"""
Not good to test with below code/style

1. code repetition

Way to fix 
1. pytest.mark.parametrize
"""
import mymath

def test_calc_square1():
    result = mymath.calc_square(5)
    assert result == 25

def test_calc_square2():
    result = mymath.calc_square(10)
    assert result == 100

def test_calc_square3():
    result = mymath.calc_square(9)
    assert result == 81

if __name__ == '__main__':
    pytest.main([__file__])
