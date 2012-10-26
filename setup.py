from setuptools import setup

setup(
    name='restful', 
    version='0.1', 
    author='Jorge E. Cardona', 
    author_email='jorge@cardona.co',
    packages=['restful'],
    test_suite='tests',
    setup_requires=[
        'unittest2',
        ])
