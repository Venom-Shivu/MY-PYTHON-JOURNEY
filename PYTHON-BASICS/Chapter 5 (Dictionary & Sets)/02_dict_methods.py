                #methods of Dictionary

d = {} # Empty dictionary
marks= {
    "Shivansh": 100,
    "Shubham": 56,
    "Rohan": 46,
    0:"Shivansh"
}

#1. a.items(): Returns a list of (key,value)tuples.

print(marks.items()) # Returns all the items inside a dictionary in forms of key value pairs(tuples)
# Output: dict_items([('Shivansh', 100), ('Shubham', 56), ('Rohan', 46), (0, 'Shivansh')])

#2. a.keys(): 

print(marks.keys()) # Returns all the keys  of dictionary in a list
#output: dict_keys(['Shivansh', 'Shubham', 'Rohan', 0])

#3. a.values(): Returns a list containing dictionary's values.

print(marks.values()) #Returns all the values of the dictionary in a list
#Output: dict_values([100, 56, 46, 'Shivansh'])

#4. a.update(): Updates the Dictionary with supplied key-value pairs.
marks.update({"Shivansh":99, "Venom":98})
print(marks) 
# The dictionary will be updated and the marks of "Shivansh" change to 99 and adds another item Venom(not present).

#5. a.get(): Returns the value of the specified keys.

print(marks.get("Shivansh")) # Returns marks corresponding to Key value "Shivansh"
print(marks.get("Shiva")) # Returns "None" , because key  value is not present in the Dictionary
#print(marks.get["Shiva"]) # Returns Error.

#6. len(): Returns the length od the dictionary
print(len(marks))

# There are other methods of dictionary available on docs.python.org


