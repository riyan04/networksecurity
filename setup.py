from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            # Read lines form the file
            lines = file.readlines()
            # process line
            for line in lines:
                requirement = line.strip()
                # ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
                
    except FileNotFoundError:
        print("requirements.txt file not found")

    
    return requirement_lst


setup(
    name="Network Security",
    version="0.0.1",
    author="Riyan Gaikwad",
    packages=find_packages(),
    install_requires=get_requirements()
)