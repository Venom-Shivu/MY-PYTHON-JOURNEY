"""Create a class 'Pets' from the class 'Animals' and further create a class 'Dog' from the 'pets'
class. Add a method 'bark' to class 'Dog'  """

# ============================================================
# BASE CLASS
# ============================================================
class Animals:
    """
    Base class representing common characteristics of all animals.
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"\n{self.name} is eating.")


# ============================================================
# INTERMEDIATE CLASS
# ============================================================
class Pets(Animals):
    """
    Represents animals that are kept as pets.
    Inherits basic behavior from Animals.
    """
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def show_owner(self):
        print(f"{self.name} belongs to {self.owner}.")

# CHILD CLASS FOR DOG

class Dog(Pets):
    """
    Dog is a specific type of Pet with its own behavior.
    """
    def bark(self):
        print(f"{self.name} says: Bhau! Bhau! 🐶")

print("\n"+"-"*20,"Instance-based OOP code","-" * 20) 

# USAGE

dog = Dog("Bruno", "Rahul")
dog.eat()           # From Animals
dog.show_owner()    # From Pets
dog.bark()          # From Dog


#           ___________ANOTHER EXAMPLE___________________

# CHILD CLASS FOR CAT

class Cat(Pets):
    """
    Cat is another type of Pet with different behavior.
    """
    def meow(self):
        print(f"{self.name} says: Meow! Meow! 🐱")

# USAGE

cat = Cat("Whiskers", "Ananya")
cat.eat()           # From Animals
cat.show_owner()    # From Pets
cat.meow()          # From Cat


# ============================================================
#                    USING @STATICMETHOD
# ============================================================

#---------------------BASE/PARENT CLASS--------------------------

class Creature:
    """
    Base class for all living creatures.
    """
    def __init__(obj, species_name):
        obj.species_name = species_name

    def consume(obj):
        print(f"\n{obj.species_name} is consuming food.\n")



# ---------------------INTERMEDIATE CLASS---------------------------------

class DomesticAnimal(Creature):
    """
    Represents animals that live with humans.
    """
    def __init__(obj, species_name, caretaker):
        super().__init__(species_name)
        obj.caretaker = caretaker

    def caretaker_info(obj):
        print(f"{obj.species_name} is taken care of by {obj.caretaker}.")

    @staticmethod
    def animal_category():
        """
        Static method because this information
        does NOT depend on any specific object.
        """
        print("Category: Domestic Animal")

# ============================================================
# CHILD CLASS : DOG
# ============================================================
class PetDog(DomesticAnimal):
    """
    Represents a Dog with dog-specific behavior.
    """
    def make_sound(obj):
        print(f"{obj.species_name} says: Woof! Woof!")

    @staticmethod
    def dog_fact():
        print("Dogs are known for loyalty and guarding.")

print("\n"+"-"*20,"Mixed OOP code (Instance + Static methods)","-" * 20)  # To make clarity in static vs instance based code
 
# USAGE : DOG

dog_obj = PetDog("Rocky", "Amit")

dog_obj.consume()           # From Creature
dog_obj.caretaker_info()    # From DomesticAnimal
dog_obj.make_sound()        # From PetDog

DomesticAnimal.animal_category()  # Static Method
PetDog.dog_fact()                  # Static Method

# ============================================================
# CHILD CLASS : BIRD
# ============================================================
class PetBird(DomesticAnimal):
    """
    Represents a Bird with bird-specific behavior.
    """
    def chirp(obj):
        print(f"{obj.species_name} says: Chirp! Chirp!")

    @staticmethod
    def bird_fact():
        print("Birds have hollow bones and can fly.")

# USAGE : BIRD

bird_obj = PetBird("Parrot", "Sneha")

bird_obj.consume()           # From Creature
bird_obj.caretaker_info()    # From DomesticAnimal
bird_obj.chirp()             # From PetBird

PetBird.bird_fact()          # Static Method

