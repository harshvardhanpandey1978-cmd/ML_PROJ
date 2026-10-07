from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Return the list of requirements from the given file."""
    requirements: List[str] = []
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj.readlines()]
        requirements = [
            req for req in requirements if req and not req.startswith("#") and req != HYPHEN_E_DOT
        ]
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("reuirements.txt"),
)
