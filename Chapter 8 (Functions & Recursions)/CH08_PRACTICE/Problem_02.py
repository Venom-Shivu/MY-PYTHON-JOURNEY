# Write a python program using function to convert Celsius to Farenheit.

#       (Celsius/5) = (Farenheit - 32) / 9

def farh(cel):
    return (cel * (9/5)) + 32 # using the formula to find Farenheit from Celsius

input_temp = float(input("Enter the Temperature in ° Celsius: "))
        # Taking the input from user as floating point number as the temperature can be in  decimals
f = farh(input_temp)

print(f"The temperature is {round(f, 2)}°F")
