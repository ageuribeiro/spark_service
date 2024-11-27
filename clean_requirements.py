import pkg_resources
import logging
import os
import subprocess

# Path requirements file
requirements_path = 'requirements.txt'

# Read file requirements
with open(requirements_path, 'r') as file:
    requirements = file.readlines()

# List packages installed
installed_packages = [pkg.key for pkg in pkg_resources.working_set]

# Filter the packages installed
used_requirements = [req for req in requirements if req.strip() in installed_packages]

# Writing requiriments used in requirements.txt file
with open(requirements_path, 'w') as file:
    file.writelines(used_requirements)

    logging.info("Requiriments clean with success")

# open powershell in default diretory project and start cmd pip freeze
project_root = os.path.dirname(os.path.abspath(__file__))
subprocess.run(["powershell", "-Command", f"cd {project_root}; pip freeze > requirements.txt"], shell=True)

logging.info("Requiriments updated with success")