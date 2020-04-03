import mymath
import pytest

@pytest.mark.parametrize("test_input, expected_output",
						[
							(5, 25),
							(9, 81),
							(10, 100)
						]
						)
def test_mymath(test_input, expected_output):
	result = mymath.calc_square(test_input)
	assert result == expected_output

if __name__ == '__main__':
    pytest.main([__file__])