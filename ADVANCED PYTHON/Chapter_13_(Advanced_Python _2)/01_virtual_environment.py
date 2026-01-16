"""
========================================
        PYTHON VIRTUAL ENVIRONMENTS
========================================

OVERVIEW:
---------
A virtual environment isolates project dependencies so different
projects can use different package versions without conflict.
This is mandatory for professional Python development.

----------------------------------------
INSTALLATION (Run in terminal)
----------------------------------------
pip install virtualenv

----------------------------------------
CREATE VIRTUAL ENVIRONMENT
----------------------------------------
# Terminal
virtualenv venv

----------------------------------------
ACTIVATE ENVIRONMENT
----------------------------------------
# Windows
venv\\Scripts\\activate

# macOS / Linux
source venv/bin/activate

----------------------------------------
INSTALL PACKAGES (ISOLATED)
----------------------------------------
pip install requests

----------------------------------------
PYTHON USAGE EXAMPLE
----------------------------------------
"""

import requests

response = requests.get("https://api.github.com")
print("Request successful:", response.status_code == 200)

"""
----------------------------------------
SAVE DEPENDENCIES
----------------------------------------
pip freeze > requirements.txt
It generates a requirements.txt file listing all installed packages.
----------------------------------------
RECREATE ENVIRONMENT
----------------------------------------
pip install -r requirements.txt
It is used to install all packages listed in requirements.txt into a new virtual environment.
----------------------------------------
DEACTIVATE
----------------------------------------
deactivate

----------------------------------------
BEST PRACTICE
----------------------------------------
• One virtual environment per project
• Never install packages globally
• Commit requirements.txt, NOT the venv folder
"""
