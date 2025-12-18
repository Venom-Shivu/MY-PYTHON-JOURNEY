            # Methods in Sets
set ={1,3,55,6,34,3,6,6,6,7,8,8, "Shivansh"}
# Set accepts all type of values in it.
print(set,type(set)) 
#Output: {1, 34, 3, 6, 7, 8, 55, 'Shivansh'} <class 'set'>

#1. s.add(): Adds the value to the given defined set
set.add(45)
print(set,type(set))  # Output: {1, 34, 3, 6, 7, 8, 45, 55, 'Shivansh'} <class 'set'>

#2. s.remove(x): Removes x. If x is not found, it raises a KeyError (crashes your program if not handled).
set.remove(55) 
print(set,type(set)) # Output: {1, 34, 3, 'Shivansh', 6, 7, 8, 45} <class 'set'>

#3. s.descard(x): Removes x. If x is not found, it does nothing (no error).
set.discard(55)
print(set,type(set)) # It does nothing as the element 55 is already removed so it will be discarded.
# Output: # Output: {1, 34, 3, 'Shivansh', 6, 7, 8, 45} <class 'set'>

#4. s.update(t) : update() is for adding multiple items at once (like extending a list).
t = {88,67.34,9,87} # New set
set.update(t) #adding multiple values at once (adding another set values) from another set.
print(set,type(set)) #Output : {1, 34, 3, 67.34, 6, 7, 8, 9, 'Shivansh', 45, 87, 88} <class 'set'>


#5. len(s): Returns the length of the set
print(len(set))

#6. s.pop(): Reurns an arbitrary(random) element from the set and returns the element removed 
#print(set.pop()) # it returned 1 that means 1 has been removed
# It is usually no recommeneded to use pop() as it removes any random element from our set.

#7. s.clear(): empties the set s.
#print(set.clear()) # Returns none




