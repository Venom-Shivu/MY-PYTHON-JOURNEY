                                #Lists in python

#List is a collection which is ordered and changeable. Allows duplicate members.
#List is written with square brackets.
# Unlike Strings, Lists are mutable, meaning their elemnets can be changed after they have been created.
# Lists can contain items of different data types.
# Unlike strings, lists can store multiple items in a single variable.
# Lists allow duplicate values.

    #Creating a List

list1 = ["Apple", "Orange", 5, 342.09, True, "Shivansh", "Rahul"]
print(list1)        #Printing the entire list
print(list1[1])    #Accessing the second item of the list
print(type(list1))  #Printing the type of list

    #Accessing List Items/Slicing (List Slicing is same as string slicing.)

newlist = ["25", "50", "75", "100", "125"]
print(newlist[1:4])       #Accessing a range of items (from index 1 to 4, excluding 4)
print(newlist[:3])        #Accessing items from the beginning to index 3 (excluding 3)
print(newlist[2:])        #Accessing items from index 2 to the end

    #Changing List Items

newlist[1] = "60"         #Changing the second item
print(newlist)

newlist[2] = "80"   #Changing multiple items
print(newlist)

