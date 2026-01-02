# ============================================================
#               MULTI-LEVEL INHERITANCE (CLEAN VERSION)
# ============================================================
# Concept:
# A child class inherits from a parent,
# and the parent itself inherits from a grandparent.
#
# Grandparent  →  Parent  →  Child
#
# Each class:
# - Initializes its OWN data
# - Calls the parent constructor using super()
# - Does NOT overwrite attributes of other classes
# ============================================================

#---------------------SIMPLE EXAMPLE---------------------------
class Variable1:
    name = "Abhay"
class Variable2(Variable1):
    name2 = "Rahul"
class Variable3(Variable2):
    name3 = "Rohit"
print(f"\n=================== SIMPLE EXAMPLE =====================")
e = Variable1()
print(f"{e.name} is Parent of Rahul and GrandParent of Rohit.")

e2 = Variable2()
print(f"{e2.name2} is Child of {e2.name} and Parent of Rohit")

e3 = Variable3()
print(f"{e3.name3} is Child of {e2.name2} and GrandSon of {e.name}")
print (f"\n=======================================================")
#----------------------END OF SAMPLE CODE---------------------------

#           ======================================================================
#                           ADVANCED MULTILEVEL INHERITENCE CODE
#           ======================================================================

class Grandparent:
    def __init__(self, grandparent_name):
        # Stores the grandparent's name
        self.grandparent_name = grandparent_name
        print(f"Grandparent '{self.grandparent_name}' created.")

    def get_grandparent_name(self):
        # Returns grandparent's name
        return self.grandparent_name


class Parent(Grandparent):
    def __init__(self, parent_name, grandparent_name):
        # Call Grandparent constructor first
        # This ensures grandparent data is initialized properly
        super().__init__(grandparent_name)

        # Stores the parent's name
        self.parent_name = parent_name
        print(f"Parent '{self.parent_name}' created.")

    def get_parent_name(self):
        # Returns parent's name
        return self.parent_name


class Child(Parent):
    def __init__(self, child_name, parent_name, grandparent_name):
        # Call Parent constructor first
        # Parent will automatically call Grandparent
        super().__init__(parent_name, grandparent_name)

        # Stores the child's name
        self.child_name = child_name
        print(f"Child '{self.child_name}' created.")

    def get_child_name(self):
        # Returns child's name
        return self.child_name


# ============================================================
#                   OBJECT CREATION & USAGE
# ============================================================

print("\n=================== Creating Child Object ======================")
child = Child("Student", "Teacher", "Principal")

# Accessing data from all levels using ONE object
print(f"\nChild's Name       : {child.get_child_name()}")
print(f"Parent's Name      : {child.get_parent_name()}")
print(f"Grandparent's Name : {child.get_grandparent_name()}")


# ============================================================
#       CREATING PARENT & GRANDPARENT OBJECTS DIRECTLY
# ============================================================

print("\n=================== Creating Parent Object =======================")
parent = Parent("Teacher", "Principal")
print(f"Parent's Name      : {parent.get_parent_name()}")
print(f"Grandparent's Name : {parent.get_grandparent_name()}")

print("\n=================== Creating Grandparent Object ==================")
grandparent = Grandparent("Principal")
print(f"Grandparent's Name : {grandparent.get_grandparent_name()}")


# ============================================================
#                   TYPE CHECKING (isinstance)
# ============================================================
# isinstance() checks whether an object belongs to a class
# or any of its parent classes.

print("\n=================== Verifying Object Types =======================")
print(f"Is child an instance of Child?       : {isinstance(child, Child)}")        # True
print(f"Is child an instance of Parent?      : {isinstance(child, Parent)}")       # True
print(f"Is child an instance of Grandparent? : {isinstance(child, Grandparent)}")  # True

print(f"\nIs parent an instance of Child?      : {isinstance(parent, Child)}")       # False
print(f"Is parent an instance of Parent?     : {isinstance(parent, Parent)}")      # True
print(f"Is parent an instance of Grandparent?: {isinstance(parent, Grandparent)}") # True

print(f"\nIs grandparent an instance of Child? : {isinstance(grandparent, Child)}")  # False
print(f"Is grandparent an instance of Parent?: {isinstance(grandparent, Parent)}") # False
print(f"Is grandparent an instance of Grandparent?: {isinstance(grandparent, Grandparent)}")  # True


# ============================================================
#              METHOD RESOLUTION ORDER (MRO)
# ============================================================
# MRO defines the order in which Python looks for methods
# when multiple classes are involved.

print("\n=================== Method Resolution Order (MRO) ================")
print("Child MRO       :", Child.__mro__)
print("Parent MRO      :", Parent.__mro__)
print("Grandparent MRO :", Grandparent.__mro__)
