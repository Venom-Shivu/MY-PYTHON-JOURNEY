             # SETS IN PYTHON
# These are the collection of well defined objects

# Sets are also written in curly brackets like dictionary but the only difference is dictionary 
# is written in key value pairs while sets are seperated by commas.
d = {} # Empty dictionary
print(d,type(d))
# Returns {}  <class 'dict'>

#Set with Only One value
e = {1}
print(e,type(e)) # returns {1} <class 'set'>
#for Empty set
s =set() # No repetition allowed!
# We dont use e = {} as this will create an empty dictionary not an empty set.

s.add(1)
s.add(2) # Or set ={1,2}
print(s,type(s)) # returns {1, 2} <class 'set'>

set ={1,3,55,6,34,3,6,6,6,7,8,8,}
print(set,type(set)) # No repetition allowed! Output: {1, 34, 3, 55, 6, 7, 8} <class 'set'>

# Sets are unordered => Element's order doesn't matter.
# Sets are unindexed => Cannot acces elements by index.
# There is no way to change items in  sets.
# Sets cannot contain duplicate values.

