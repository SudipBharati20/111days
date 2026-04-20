"""
PIP FREEZE

Used to list installed packages and versions.
"""

import pkg_resources

packages = [str(d) for d in pkg_resources.working_set]

print("Installed Packages:")
for p in packages[:10]:  # limiting output
    print(p)

print("\nUse command:")
print("pip freeze > requirements.txt")