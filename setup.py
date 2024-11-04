from setuptools import find_packages, setup
from openanalytics import version

setup(
    name=version.APP_NAME,
    packages=find_packages(),
    version=version.VERSION,
    description="My first Python library",
    author="Lakitha Sam",
)
