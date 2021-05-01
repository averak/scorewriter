from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="scorewriter",
    version="0.1.0",
    description="This project is a scorewriter developed at welcome seminar.",
    license="MIT",
    author="averak",
    packages=find_packages(),
    package_data={},
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
)