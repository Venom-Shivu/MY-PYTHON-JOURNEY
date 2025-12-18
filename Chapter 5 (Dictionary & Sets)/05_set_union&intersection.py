set = { 1,3,5,7,8,12,34,"Shivansh" }

"""
    1. s.union()
                ->Returns a new set with all the items from both the set without repeatition.
                ->It contains the items from both sets in a new set formed by union.
                -> Union is also unordered i.e, the new set will also be unordered.

"""
print("Union: ",set.union({42,12,31,22})) 
# Union with new set {42,12,31,22}. or we can store this to a variable s2 then use set.union(s2)
#Output: {1, 34, 3, 5, 7, 8, 42, 12, 22, 31, 'Shivansh'}

"""
    2.s.intersection()
                    ->Returns a set which contains only items in both the sets.
                    -> It returns the element which are common in both the sets.
"""

print("Intersection: ", set.intersection({12,34,6,"Shivansh",9}))
#Output: {34, 12, 'Shivansh'}

'''
    3. difference()
                    ->Returns the element which are in first set but not in second.
                    -> It returns the element of the 1st set which are not in second set.
'''
print("Difference: ",set.difference({1,3,6,55,"Shiva"}))
#Output: {34, 5, 7, 8, 12, 'Shivansh'}


# In another way..
s2 = {12,3,56,8,53,46,"Shivansh","Shiva"}

print("UNION",set.union(s2)) # Returtns the union of "set" with "s2"
print("INTERSECTION",set.intersection(s2)) # Returns the intersection with set "s2".
print("DIFFERENCE",set.difference(s2)) # Gives the difference with reference to set "s2"


            # More On sets
            
# Using issubset() Method
print("{1,5} is a subset of 'set' which is :", {1,5}.issubset(set)) 
# Output {1,5} is a subset of 'set' which is : True

# Using issuperset() Method
print(" 'set' is Superset of {1,5} which is :",set.issuperset({1,5}))
#{1.5} is a part of of given 'set' so "set" will be superset of {1,5}, as it is derived from "set"
#Output:  'set' is Superset of {1,5} which is : True
