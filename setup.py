from setuptools import setup,find_packages

with open("requirement.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MULTI-AI AGENT",
    version="0.1",
    author="Otto",
    packages=find_packages(),
    install_requires = requirements,
)