from setuptools import setup, find_packages
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='randomidgenlib',
    version='0.1',
    install_requires=[],
    author='vtv',
    description='Learning: A simple library to generate random IDs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
)