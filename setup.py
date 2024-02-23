from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    description='EAI example python package',
    long_description=open('readme.MD').read(),
    install_requires=['numpy'],
    url='https://github.com/username/mypackage',
    author='Omojiade Marvellous',
    author_email='pinkymarvy@gmail.com'
    )