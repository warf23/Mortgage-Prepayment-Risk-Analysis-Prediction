from setuptools import setup, find_packages

from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]: # this function is used to get the requirements from the file requirements.txt , and return a list of requirements
    '''
    Retrieve a list of project requirements from a file.

    This function reads a file containing project requirements and returns
    a list of those requirements. Each requirement is a string, and any
    newline characters at the end of each requirement are removed.

    Args:
        file_path (str): The path to the requirements file.

    Returns:
        List[str]: A list of project requirements.
    '''
    requirements=[] # this list will contain the requirements
    with open(file_path) as file_obj: # open the file in read mode 
        requirements=file_obj.readlines() # read the file line by line and put the lines in the list requirements
        requirements=[req.replace("\n","") for req in requirements] # remove the new line character from each line in the list requirements

        if HYPEN_E_DOT in requirements: # if the list requirements contains the string HYPEN_E_DOT , remove it from the list requirements 
            requirements.remove(HYPEN_E_DOT)
    
    return requirements # return the list requirements


setup(
    
    name='Final_Intership_TechnoLabs_END_TO_END_Mortgage_Risk', 
    
    version='0.0.1',
    
    author="AGRAT_MOHAMMED" , 
    
    author_email="simo.agrat1@gmail.com",
    
    
    description="A short description of your package",
    
    url="https://github.com/warf23/Final_Intership_TechnoLabs_END_TO_END_Mortgage_Risk.git",
   
    packages=find_packages(), # find all the packages in the project
    
    install_requires=get_requirements('requirements.txt') , # call the function get_requirements to get the requirements from the file requirements.txt
    
    python_requires=">=3.8",
    
   
)
