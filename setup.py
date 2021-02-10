import os
from configparser import ConfigParser

from setuptools import find_packages, setup

config = ConfigParser()
rc = os.path.join(os.path.expanduser("~"), ".pypirc")
config.read(rc)

setup(
    name="matk",
    version="0.0.1",
    description=("Helpfull untils for NN programming"),
    author="Vladimir Sydorskyi",
    python_requires=">=3.7",
    packages=find_packages(),
)
