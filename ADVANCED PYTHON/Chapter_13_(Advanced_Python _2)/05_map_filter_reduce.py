"""
MAP, FILTER & REDUCE in Python
-----------------------------
This script demonstrates map(), filter(), and reduce()
with clear logic and well-structured output.
"""

from functools import reduce
from typing import List


# ============================
# MAP FUNCTIONS
# ============================

def square_numbers(numbers: List[int]) -> List[int]:
    """Return the square of each number."""
    return list(map(lambda x: x ** 2, numbers))


def convert_to_strings(numbers: List[int]) -> List[str]:
    """Convert all numbers to strings."""
    return list(map(str, numbers))


# ============================
# FILTER FUNCTIONS
# ============================

def get_even_numbers(numbers: List[int]) -> List[int]:
    """Return only even numbers."""
    return list(filter(lambda x: x % 2 == 0, numbers))


def get_numbers_greater_than_five(numbers: List[int]) -> List[int]:
    """Return numbers greater than 5."""
    return list(filter(lambda x: x > 5, numbers))


# ============================
# REDUCE FUNCTIONS
# ============================

def sum_numbers(numbers: List[int]) -> int:
    """Return the sum of all numbers."""
    return reduce(lambda x, y: x + y, numbers, 0)


def product_numbers(numbers: List[int]) -> int:
    """Return the product of all numbers."""
    return reduce(lambda x, y: x * y, numbers, 1)


def max_number(numbers: List[int]) -> int:
    """Return the maximum number."""
    return reduce(lambda x, y: x if x > y else y, numbers)


# ============================
# MAIN EXECUTION
# ============================

if __name__ == "__main__":

    input_list = [20, 2, 3, 6, 5]

    print("\n============================")
    print("INPUT DATA")
    print("============================")
    print("Input List:", input_list)

    print("\n============================")
    print("MAP OUTPUT")
    print("============================")
    print("Squares:", square_numbers(input_list))
    print("As Strings:", convert_to_strings(input_list))

    print("\n============================")
    print("FILTER OUTPUT")
    print("============================")
    print("Even Numbers:", get_even_numbers(input_list))
    print("Numbers > 5:", get_numbers_greater_than_five(input_list))

    print("\n============================")
    print("REDUCE OUTPUT")
    print("============================")
    print("Sum:", sum_numbers(input_list))
    print("Product:", product_numbers(input_list))
    print("Maximum:", max_number(input_list))
