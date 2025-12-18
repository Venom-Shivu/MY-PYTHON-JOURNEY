                     #Example 
                     
list1 = ["Apple", "Orange", 5, 342.09, True, "Shivansh", "Rahul"]
print("Original List:", list1)


                      #LIST METHODS


#1. append() - Adds an element at the end of the list

list1.append("Banana")
print("After append():", list1)

#2. insert() - Adds an element at the specified position

list1.insert(2, "Mango") # Inserts Mango at index 2, shifting the rest to the right
print("After insert():", list1)

#3. remove() - Removes the item with the specified value, first occurrence only

list1.remove(5)  # Removes the first occurrence of 5
print("After remove():", list1)

#4. pop() - Removes the element at the specified position (or the last item if index not specified)

popped_item = list1.pop(3)  # Removes the item at index 3
print("After pop():", list1) # Shows the list after the pop operation
print("Popped item:", popped_item) # Shows the removed item

#5. sort() - Sorts the list in ascending order (only works if all elements are of the same type)

num_list = [34, 12, 5, 67, 23]
num_list.sort()
print("Sorted num_list:", num_list)

#6. reverse() - Reverses the order of the list

num_list.reverse()
print("Reversed num_list:", num_list)

#7. count() - Returns the number of elements with the specified value

count_shivansh = list1.count("Shivansh")
print("Count of 'Shivansh':", count_shivansh)
print (list1.count("Rahul")) # Another syntax to print count of an element

#8. extend() - Adds the elements of a list (or any iterable) to the end of the current list.
    # It takes a single iterable (like another list, tuple, set, etc.) as an argument.

list2 = ["Grapes", "Pineapple"]
list1.extend(list2)
print("After extend():", list1)

#9. index() - Returns the index of the first occurrence of the specified value

index_rahul = list1.index("Rahul")
print("Index of 'Rahul':", index_rahul)
print(list1.index("Banana"))

#10. clear() - Removes all the elements from the list
    #Empties the list, it doesn't need any arguements.

list2.clear()
print("After clear(), list2:", list2)

#11. copy() - Returns a shallow copy of the list

list3 = list1.copy()
print("Copied list3 from list1:", list3)
# Modifying list3 to show that it's a separate copy
list3.append("Kiwi")
print("After appending 'Kiwi' to list3:", list3)
print("Original list1 remains unchanged:", list1)
#These are some of the most commonly used list methods in Python.

#------------------------END-------------------------