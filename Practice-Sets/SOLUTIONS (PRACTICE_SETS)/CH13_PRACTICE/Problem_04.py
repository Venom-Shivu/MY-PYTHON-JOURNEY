"""
Given a list of integers, write a Python program to filter and extract all elements that are divisible by 5.
The program should return a new list containing only those numbers that satisfy the divisibility condition.
"""

# ============================================================
# Input list (used for Method 1 and Method 2)
# ============================================================

numbers = [10, 23, 45, 67, 80, 90, 33, 55]


# ============================================================
# Method 1: Using filter() and lambda
# ============================================================

filtered_filter = list(filter(lambda x: x % 5 == 0, numbers))

print("========== METHOD 1 : filter() FUNCTION ==========")
print(filtered_filter)


# ============================================================
# Method 2: Using list comprehension (Shortcut)
# ============================================================

filtered_list_comp = [num for num in numbers if num % 5 == 0]

print("\n========== METHOD 2 : LIST COMPREHENSION ==========")
print(filtered_list_comp)


# ============================================================
# Method 3: User input based filtering
# ============================================================

user_numbers = list(map(int, input("\nEnter numbers separated by space: ").split()))

filtered_user_input = [num for num in user_numbers if num % 5 == 0]

print("\n========== METHOD 3 : USER INPUT ==========")
print(filtered_user_input)
