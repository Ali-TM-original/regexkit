from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name="regexkit",
    version="0.1",
    description="simplify the creation of regular expressions using a fluent interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/Ali-TM-original/regexkit",
    author="Ali-TM-original",
    license="MIT",
    zip_safe=False,
)
