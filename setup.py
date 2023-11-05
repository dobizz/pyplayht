from setuptools import find_packages, setup

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
