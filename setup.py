from setuptools import find_packages,setup
from typing import List

def get_requirements(url:str)->List[str]:
    try:
        requirements_list:List[str] = []
        with open(url,"r") as file:
            files = file.readlines()

            for fil in files:
                if fil.strip() and fil != "-e.":
                    requirements_list.append(fil.strip()) 

    except Exception as e:
        print('Requirements file not found: ',e)

    return requirements_list


setup(name="NetworkSecurity",
      version="0.0.1",
      author="Mahavir Rajpruohit",
      author_email="mrajpurohit1912@gmail.com",
      find_packages=find_packages(where="networksecurity"),
      package_dir={"networksecurity":"networksecurity"},
      install_requires=get_requirements('requirements.txt'))


# if __name__ == "__main__":
#     req = get_requirements('requirements.txt')
#     print(req)
