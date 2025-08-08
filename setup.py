from setuptools import find_packages , setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements for the package.
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")   

    return requirement_lst  

setup(
    name='network_security_project',
    version='0.0.1',
    author='Prince Yadav',
    author_email="yadav27prince12@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(), 
) 