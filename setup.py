from setuptools import find_packages,setup
from typing import list

HYPEN_E_DOT ="-e ."

def get_requirements(file_path: str)->list[str]:
    '''
        this function will return the list of requirements
        '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return



setup(
   name='PythonProjects',
    version="0.0.1",
    author="Mansoureh",
    author_email="mans.aghabeig@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)