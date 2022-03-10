from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name = 'storer',
    version = '1.0',
    packages = find_packages(),
    install_requires = ['click'],
    entry_points = '''
    [console_scripts]
    storer=store:store
    '''
)