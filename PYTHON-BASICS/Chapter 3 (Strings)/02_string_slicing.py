#SLICING IN STRINGS

name = "Shivu"

""" 
    [S   H   I   V   U] 
    [0   1   2   3   4]  positive indexing
    [-5 -4  -3  -2  -1]  negative indexing
"""

print(name[0:4])  # returns 'Shiv' (chars at indices 0,1,2,3)

print(name[-4:-1])  # negative indexing equivalent to name[1:4]
print(name[1:4])
# The above two print statements produce the same result because
# the slice `[-4:-1]` maps to `[1:4]` for this string.
print(name[:4])  # same as print(name[0:4])
print(name[1:])  # from index 1 to the end (not the same as name[1:4])
print(name[:])   # same as print(name[0:4])

# If nothing is written on the left it's index 0; if nothing on the right
# the slice goes up to the last element of the sequence.

# SLICING WITH SKIP VALUE

word = "amazing"

"""
Example: word = "amazing" with indexes 0:a, 1:m, 2:a, 3:z, 4:i, 5:n, 6:g
Using a step of 2 starting at index 1 picks characters at indices 1,3,5 -> 'mzn' as there is skip value of 2.

"""
#Positive step value means slicing will be done in the forward direction.

print(word[1:6:2])  # 'mzn'
print(word[::2])    # 'aaig' (every second character from the whole string)
print(word[1::3])   # 'mi' (every third character starting from index 1)
print(word[::1])   # 'amazing' (returns the whole string)
print(word[::3])   # 'az' (every third character starting from index 0)
# The third value in the slice is the step value which indicates the interval between each index.


# A negative step value means slicing will be done in reverse order.

print(word[::-1])  # 'gnizama' (reverses the string)
print(word[5:2:-1])  # 'niz' (from index 5 to 2 in reverse order stops before index 2)
print(word[6:3:-2])  # 'gi' (from index 6 to 3 in reverse order with a step of 2 stops before index 3)
print(word[2:1:-1])  # 'a' (single character, as slicing goes from index 2 to 1 and stops before index 1)
# 1 is not included because the stop index is exclusive,i.e., it is not part of the slice.
print(word[3::-1])  # 'zama' (from index 3 to the start in reverse order)
print(word[:3:-1])  # 'gni' (from the end to index 3 in reverse order stops before index 3)
print(word[::-2])  # 'gzaa' (every second character in reverse order)
