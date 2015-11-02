from setuptools import setup, find_packages

setup(
    name='vizit',
    version="0.0.1",
    packages=find_packages(),
    install_requires=['networkx'],
    entry_points={
        'console_scripts': [
            'vizit=vizit:main',
        ],
    }
)
