"""
Can You change the values inside a list which is contained in set S?...
s= {5,6,14, "Shivansh",[1,2]} 
"""
s= {5,6,14, "Shivansh",[1,2]} 

""" 
->We cannot even have a list as an element in a set because Python requires all their items 
to be immutable and hashable(the value that never changes) 
->Lists are mutable and not hashable, so they cannot be added to a set.
->If we try to do this Python will show error: 
    TypeError: cannot use 'list' as a set element (unhashable type: 'list')
    
"""