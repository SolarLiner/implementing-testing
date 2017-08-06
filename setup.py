import os
from setuptools import setup

# Utility: Read file in project
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="veryimportant_module",
    version="0.0.1",
    author="SolarLiner",
    author_email="solarliner@gmail.com",
    description="A VeryImportant module that needs to be thouroughly tested",
    long_description=read("README.md"),
    license="MIT",
    keywords="example test unittesting github",
    packages=['src', 'tests'],
    extras_require= {
        'test': ["coverage", "python-coveralls"]
        }
)
