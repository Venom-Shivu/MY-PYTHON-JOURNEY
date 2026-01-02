        #  Write a python function which converts inches to cms


# ======================================================
# CONVERSION FACTOR: 1 inch = 2.54 centimeters
# ======================================================

# FUNCTION: Converts inches to centimeters
def inch_to_cm(inches):
    # Calculation: Multiply the inch value by the constant 2.54
    return inches * 2.54

# --- PART 1: Inch to CM ---
# We use float() instead of int() to allow for decimal values (e.g., 5.5 inches)
n = float(input("Enter the value in inches: "))

# Calling the function and storing the result
result = inch_to_cm(n)
# Using an f-string to display the result clearly
print(f"The Corresponding value in centimeters is {result}cm")


# FUNCTION: Converts centimeters to inches
def cm_to_inch(cms):
    # Calculation: Divide the cm value by 2.54 to reverse the process
    return cms / 2.54

# --- PART 2: CM to Inch ---
n = float(input("Enter the value in centimeters: "))

# Calling the function and storing the result
result = cm_to_inch(n)
print(f"The Corresponding value in inches is {result}inch")