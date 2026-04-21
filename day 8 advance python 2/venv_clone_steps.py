# File: venv_clone_steps.py

# Q1 & Q6: Virtual Environment setup and cloning process

"""
STEP 1: Create first environment
python -m venv env1

STEP 2: Activate env1
env1\Scripts\activate   (Windows)
source env1/bin/activate (Mac/Linux)

STEP 3: Install packages
pip install flask requests

STEP 4: Save dependencies
pip freeze > requirements.txt

STEP 5: Create second environment
python -m venv env2

STEP 6: Activate env2
env2\Scripts\activate

STEP 7: Install same packages
pip install -r requirements.txt
"""

print("Virtual environment cloning steps written successfully.")