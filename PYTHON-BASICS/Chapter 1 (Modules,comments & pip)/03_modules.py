# ==========================================
# BUILT-IN MODULES
# ==========================================
# These come pre-installed with Python. 
# You don't need to install anything; just 'import' them.

import math  # The 'math' module provides mathematical functions

# Example: Using math.pi and math.sqrt
result = math.sqrt(16)
print(f"The square root of 16 is: {result}")
print(f"The value of Pi is: {math.pi}")


# ==========================================
# EXTERNAL MODULES
# ==========================================
# These are NOT included with Python by default. 
# You must install them using 'pip' in your terminal first.
# Command: pip install requests

import requests # 'requests' is a popular external module for HTTP tasks

# Example: Checking if a website is online
try:
    response = requests.get("https://www.google.com")
    print(f"Google Status Code: {response.status_code} (Success!)")
except:
    print("External module 'requests' is not installed or no internet.")
    