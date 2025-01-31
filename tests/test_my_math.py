import pytest

from src.my_math import sum, multiply, difference

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply
def test_multiply():
    res = multiply(2,2)
    assert res == 4


# Check for understanding
## Test difference
def test_difference():
    res = difference(8,4)
    assert res == 4

# Work together
## Test absolute sum



# Check for understanding
## Test calculate age
