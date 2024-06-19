from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."


def get_requirements(file) -> List[str]:
    """
    This function will return the list of requirements
    """
    with open(file, "r") as f:
        packages = f.readlines()
        packages = [req.replace("\n", "") for req in packages]

        if HYPHEN_E_DOT in packages:
            packages.remove(HYPHEN_E_DOT)

    return packages


setup(
    name="oelhansali_mlproject",
    version="0.0.1",
    author="Oelhansali",
    author_email="oussamaelhansali@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
