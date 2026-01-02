'''
Write a program to generate multiplication table from to 2 to 20 and write it to the different files. Place these files in a folder named Table_For_Kids. 
'''
def generateTables(n):
    """
    This function generates multiplication tables
    from 2 up to the given number n.
    Each table is written into a separate file.
    """

    # Loop through numbers from 2 to n
    for i in range(2, n + 1):

        # Open a file in write + read mode
        # 'w+' creates the file if it does not exist
        # If the file exists, its content is overwritten
        with open(f"Table_For_Kids/multiplication_table_{i}.txt", "w+") as f:

            # Generate multiplication table from 1 to 10
            for j in range(1, 11):

                # Write each multiplication result into the file
                f.write(f"{i} X {j} = {i * j}\n")


# Call the function to generate tables from 2 to 20
generateTables(20)


























