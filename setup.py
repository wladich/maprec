from setuptools import setup, find_packages

setup(
    name='maprec',
    version='2.0.0',
    url='https://github.com/wladich/maprec',
    author='Sergey Orlov',
    author_email='wladimirych@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pyproj',
        'pyyaml',
        'tps @ git+https://github.com/wladich/thinplatespline.git',
    ],
)
