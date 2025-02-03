import pytest

from src.my_math import sum, multiply, difference, absolute_sum, calculate_birth_year

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
def test_it_return_positive_numbers():
    res = absolute_sum(5, -10)
    assert res == 15
    
def test_it_should_return_postive():
    res = absolute_sum(-5, 10)
    assert res == 15




# Check for understanding
## Test calculate age
def test_calculate_age():
    res = calculate_birth_year(2025, 25, True)
    assert res == 2000
