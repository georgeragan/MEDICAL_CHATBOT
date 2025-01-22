import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(acstime)s]:%(message)s:')

list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "setup.py",
    "app.py",
    "research/trails.ipynb"
]
#setup.py: Used for packaging or installation, not for running the code directly.
#__init__.py: Makes a folder like src/ a Python package.
#Importing: Once the folder is a package, you can use from <package>.<module> import <function> to access its contents.

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file:{filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Created new file:{filepath}")
    else:
        logging.info(f"File already exists:{filepath}")