#Write a Program which finds out whether a given name is present in a list or not.

list_of_names = ['Shivansh', 'Aman', 'Shivam', 'Mayank', 'Divyansh', 'Ragini', 'Anjali', 'Sakshi']

name = input("Enter the name you want to search in the list: ")

if name in list_of_names:
    print(f"{name} is present in the list.")
else:
    print(f"{name} is not present in the list.")