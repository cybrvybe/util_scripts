from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="util_scripts",
    version="0.1",
    packages=["util_scripts"],
    install_requires=requirements,
)
