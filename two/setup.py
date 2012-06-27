from setuptools import setup, find_packages

setup(
    name='sample.main.two',
    version='0.0.1',
    packages=find_packages(),
    namespace_packages=['sample', 'sample.main'],
    include_package_data=True,
)
