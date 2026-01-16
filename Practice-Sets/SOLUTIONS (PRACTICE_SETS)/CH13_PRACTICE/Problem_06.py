"""
Using the system Python interpreter, generate a complete list of installed packages and their versions.
Store this information using pip freeze, and then create a new Python virtual environment that replicates
the same package configuration to ensure environment consistency and reproducibility.
"""

"""
⚠️ NOTE: These commands are executed in the terminal/command prompt, as package and environment 
          management is not performed inside Python scripts.
"""

# ------------------------------------------------------------
# STEP 1: Verify system Python interpreter
# ------------------------------------------------------------
"""
python --version
"""

# ------------------------------------------------------------
# STEP 2: Capture system-installed packages
# ------------------------------------------------------------
"""
pip freeze > system_requirements.txt
"""

# ------------------------------------------------------------
# STEP 3: Create a new virtual environment
# ------------------------------------------------------------
"""
python -m venv replicated_env
"""

# ------------------------------------------------------------
# STEP 4: Activate the virtual environment
# ------------------------------------------------------------
"""
Windows:    replicated_env\Scripts\activate

macOS / Linux:  source replicated_env/bin/activate
"""

# ------------------------------------------------------------
# STEP 5: Install packages from pip freeze output
# ------------------------------------------------------------
"""
pip install -r system_requirements.txt
"""

# ------------------------------------------------------------
# STEP 6: Verify replicated environment (optional)
# ------------------------------------------------------------
"""
pip list
"""

# ------------------------------------------------------------
# STEP 7: Deactivate the virtual environment
# ------------------------------------------------------------
"""
deactivate
"""
