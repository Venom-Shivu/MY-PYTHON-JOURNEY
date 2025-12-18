#Program to store seven fruits in a list entered by the user.

fruits = []  # Initialize an empty list to store fruits

for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

print("Fruits list:", fruits)

# The list 'fruits' now contains the seven fruits entered by the user.

#Another way to do the same program

fruits = []

f1 = input("Enter Fruit naame: ")
fruits.append(f1)
f2 = input("Enter Fruit naame: ")
fruits.append(f2)
f3 = input("Enter Fruit naame: ")
fruits.append(f3)
f4 = input("Enter Fruit naame: ")
fruits.append(f4)
f5 = input("Enter Fruit naame: ")
fruits.append(f5)
f6 = input("Enter Fruit name: ")
fruits.append(f6)
f7 = input("Enter Fruit name: ")
fruits.append(f7)

print("Fruits namme", fruits)