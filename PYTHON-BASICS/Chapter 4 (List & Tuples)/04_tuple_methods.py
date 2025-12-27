         #TUPLE METHODS

tuple3 = (10, 20, 30, "Shivansh", 45.67, True, "Rahul", 10) # Tuple with multiple elements

#1. count() - Returns the number of elements with the specified value

count_10 = tuple3.count(10)
print("Count of 10:", count_10) #Returns 2
# Another syntax to print count of an element
print(tuple3.count("Shivansh")) # Returns 1

#2. index() - Returns the index of the first occurrence of the specified value

index_rahul = tuple3.index("Rahul")
print("Index of 'Rahul':", index_rahul) # Returns 6
# Another syntax to print index of an element
print(tuple3.index(30)) # Returns 2



#NOTE: Tuples have only two built-in methods: count() and index() because they are immutable.

#Meanwhile they have functions that can be used with tuples like len(), min(), max(), sum(), etc.


#3. len() - Returns the number of items in a tuple
print("Length of tuple3:", len(tuple3))

#4. min() - Returns the smallest item in a tuple
tuple_numbers = (5, 10, 2, 8, 3)
print("Minimum value in tuple_numbers:", min(tuple_numbers))

#5. max() - Returns the largest item in a tuple
print("Maximum value in tuple_numbers:", max(tuple_numbers))

#6. sum() - Returns the sum of all items in a tuple
print("Sum of items in tuple_numbers:", sum(tuple_numbers))

#7. sorted() - Returns a new sorted list from the items in a tuple
sorted_tuple = sorted(tuple_numbers)
print("Sorted tuple_numbers:", sorted_tuple)

#8. any() - Returns True if any item in the tuple is true
tuple_bool = (0, "", None, True)
print("Any true in tuple_bool:", any(tuple_bool))

#9. all() - Returns True if all items in the tuple are true
tuple_bool2 = (1, "Hello", 3.14, True)
print("All true in tuple_bool2:", all(tuple_bool2))

#10. tuple() - Converts an iterable (like a list) into a tuple
list1 = [1, 2, 3, 4, 5]
tuple_from_list = tuple(list1)
print("Tuple from list1:", tuple_from_list)

#11. reversed() - Returns a reversed iterator of the tuple
reversed_tuple = tuple(reversed(tuple3))
print("Reversed tuple3:", reversed_tuple)

#12. zip() - Combines multiple iterables into a tuple of tuples
tuple_a = (1, 2, 3)
tuple_b = ('a', 'b', 'c')
zipped_tuple = tuple(zip(tuple_a, tuple_b))
print("Zipped tuple:", zipped_tuple)

#13. enumerate() - Returns an enumerate object that contains pairs of index and value
enumerated_tuple = tuple(enumerate(tuple3))
print("Enumerated tuple3:", enumerated_tuple)

# These functions provide additional functionality when working with tuples in Python.