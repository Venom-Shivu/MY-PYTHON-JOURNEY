""" What will be the lenght of the following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20')
What will be the length of s after these operations
"""

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
# Normally length will be 3 but the output came out to be 2 only.
# This is beacause python compares 20==20.0 ->  if True, then only int is considered thats why len is 2 
print(s) # this will also show {'20', 20} excluding the floating point number.
