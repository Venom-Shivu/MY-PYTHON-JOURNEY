#            ============================================================
#               PYTHON BUILT-IN DATA TYPES – DESCRIPTION WITH EXAMPLES
#            ============================================================


#               ------------------------------------------------------------
#                                    NUMERIC DATA TYPES
#               ------------------------------------------------------------

x = 10
# int → Stores whole numbers with unlimited precision.
# Used for counting, indexing, loops, and arithmetic operations.

y = 3.75
# float → Stores real numbers with decimal points.
# Used in calculations requiring precision like measurements and averages.

z = 4 + 2j
# complex → Stores numbers with real and imaginary parts.
# Used in scientific, mathematical, and signal-processing applications.


#               ------------------------------------------------------------
#                                   TEXT DATA TYPE
#               ------------------------------------------------------------

name = "Shivu"
# str → Stores textual data as Unicode characters.
# Used for names, messages, file paths, and user input.


#               ------------------------------------------------------------
#                                 BOOLEAN DATA TYPE
#               ------------------------------------------------------------

is_logged_in = True
# bool → Represents logical truth values.
# Used in conditions, decision-making, and control flow.


#               ------------------------------------------------------------
#                                 NONE DATA TYPE
#               ------------------------------------------------------------

data = None
# NoneType → Represents the absence of a value.
# Used to initialize variables or indicate “no result”.


#               ------------------------------------------------------------
#                               SEQUENCE DATA TYPES
#               ------------------------------------------------------------

numbers = [1, 2, 3]
# list → Ordered and mutable collection.
# Used when data needs to change frequently.

coordinates = (10, 20)
# tuple → Ordered and immutable collection.
# Used for fixed data that should not be modified.

values = range(1, 5)
# range → Generates a sequence of numbers efficiently.
# Used mainly in loops to avoid unnecessary memory usage.


#               ------------------------------------------------------------
#                               SET DATA TYPES
#               ------------------------------------------------------------

unique_numbers = {1, 2, 3}
# set → Unordered collection of unique elements.
# Used for removing duplicates and fast membership testing.

fixed_numbers = frozenset([4, 5, 6])
# frozenset → Immutable version of a set.
# Used when a set must remain constant or be used as a dictionary key.


#               ------------------------------------------------------------
#                           MAPPING DATA TYPE
#               ------------------------------------------------------------

student = {"name": "Shivu", "age": 22}
# dict → Stores data as key-value pairs.
# Used for structured data, configurations, and fast lookups.


#               ------------------------------------------------------------
#                           BINARY DATA TYPES
#               ------------------------------------------------------------

raw_data = b"ABC"
# bytes → Immutable binary data.
# Used for files, network communication, and encryption.

mutable_data = bytearray(b"ABC")
# bytearray → Mutable binary data.
# Used when binary data needs modification.

buffer = memoryview(b"XYZ")
# memoryview → Access binary data without copying it.
# Used for performance-critical applications.

#               ============================================================
#                        DATA TYPE VERIFICATION USING type()
#               ============================================================

print(type(x))               # <class 'int'>
print(type(y))               # <class 'float'>
print(type(z))               # <class 'complex'>

print(type(name))            # <class 'str'>

print(type(is_logged_in))    # <class 'bool'>

print(type(data))            # <class 'NoneType'>

print(type(numbers))         # <class 'list'>
print(type(coordinates))     # <class 'tuple'>
print(type(values))          # <class 'range'>

print(type(unique_numbers))  # <class 'set'>
print(type(fixed_numbers))   # <class 'frozenset'>

print(type(student))         # <class 'dict'>

print(type(raw_data))        # <class 'bytes'>
print(type(mutable_data))    # <class 'bytearray'>
print(type(buffer))          # <class 'memoryview'>
