from setuptools import setup

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'SAMAR'
SRC_REPO = 'src'
LIST_of_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author= AUTHOR_NAME,
    author_email = 'samarjamal326@gmail.com',
    description = 'This is the package for movie recommendation model',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = '',
    packages = [SRC_REPO],
    python_requires = '>=3.8',
    install_requires = LIST_of_REQUIREMENTS,
)