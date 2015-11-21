from setuptools import setup, find_packages

setup(
    name='vizit',
    author='DCRichards',
    author_email='',
    description='Simple dependency visualisation in Python',
    version='0.1.1',
    licence='MIT',
    url='https://github.com/DCRichards/vizit',
    packages=find_packages(),
    install_requires=['networkx', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'vizit=vizit:main',
        ],
    }
)
