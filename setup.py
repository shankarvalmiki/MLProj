from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''this functionn will return requirments for the application'''

    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        #here the readlines function will add \n also to the list object so remove that we have to replace \n with ""
        requirements=[req.replace("\n","") for req in requirements]
        #the "-e ." is added to the end of the requiremnts.txt file so that whenever we are trying to install this txt file 
        # the setup.py should also run to build those packages
        if "-e ." in requirements:
            requirements.remove('-e .')
        

setup(
    name = "MLProj",
    version="0.0.1",
    author="Shankar",
    author_email="shankarvalmikidr@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")

)