from pathlib import Path

from setuptools import find_packages, setup

requirements = Path("requirements.txt").read_text().split("\n")

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your dependencies here
        *requirements
    ],
)
