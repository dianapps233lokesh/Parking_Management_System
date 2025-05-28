from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements 
    '''
    requirement_lst=[]
    try:
        with open('requirements.txt') as f:
            lines=f.readlines()
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e.]
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("no requirements.txt ")
    return requirement_lst

setup(
    name="Parking Management System",
    version="0.0.1",
    author="Lokesh",
    author_email="lokesh.saini@dianapps.com",
    packages=find_packages(),
    install_requires=get_requirements()
)