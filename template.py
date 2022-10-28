import os
from pathlib import Path
# This library helps tp make an application OS independent as it automatically finds out the default path based on the operating system
import logging

logging.basicConfig(level = logging.INFO,
                    format = "[%(asctime)s : %(levelname)s]: %(message)s"
                    )

while True:
    project_name = input("Enter the project name: ")
    if project_name != "":
        break
    
logging.info(f"Creating Project with name: {project_name}")

#list of files

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",   # helps in creating repository and basic environment setup i.e conda environment
    "requirements.txt",  
    "requirements_dev.txt",
    "setup.py",   # used for basic project setup
    "pyproject.toml", # this file contains the build system requirements of Python projects. This resolves the build tool dependency and the error"pip can read
                      # pyproject.toml and what versions of setuptools or wheel one may need
    "setup.cfg",  # It is used to supply parameters to the commands that setup.py makes available.
    "tox.ini", # used to configure different type of packages. The python package we are building will be verified on different environments and this file willhelp in verification of packge in different packages
    
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file : {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")
        