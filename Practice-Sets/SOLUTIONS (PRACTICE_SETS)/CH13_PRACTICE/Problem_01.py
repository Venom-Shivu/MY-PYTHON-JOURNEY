'''
Create two isolated Python virtual environments. Install a set of required packages in the first environment. 
Demonstrate how to replicate the exact same package configuration in the second environment to ensure environment
consistency across systems or deployments.
'''

# ------------------------------------------------------------
# STEP 1: Create and activate the first virtual environment
# ------------------------------------------------------------

#   OPEN THE TERMINAL --> FOLLOW THE BELOW STEPWISE COMMANDS IN TERMINAL 
""" 
--------Create virtual environment--------
python -m venv env1

--------Activate environment-------------
Windows:   env1\Scripts\activate
macOS / Linux:  source env1/bin/activate

"""

# ------------------------------------------------------------
# STEP 2: Install required packages in the first environment
# ------------------------------------------------------------

"""
pip install numpy pandas matplotlib
"""

# ------------------------------------------------------------
# STEP 3: Export installed packages to requirements file
# ------------------------------------------------------------

"""
pip freeze > requirements.txt
"""

# ------------------------------------------------------------
# STEP 4: Deactivate the first environment
# ------------------------------------------------------------

"""
deactivate
"""

# ------------------------------------------------------------
# STEP 5: Create and activate the second virtual environment
# ------------------------------------------------------------

"""
python -m venv env2
"""

# Activate environment

"""
Windows:    env2\Scripts\activate
macOS / Linux:  source env2/bin/activate
"""

# ------------------------------------------------------------
# STEP 6: Install the same packages in the second environment
# ------------------------------------------------------------

"""
pip install -r requirements.txt
"""

# ------------------------------------------------------------
# STEP 7: Deactivate the second environment
# ------------------------------------------------------------

"""
deactivate
"""