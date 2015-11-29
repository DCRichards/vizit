from setuptools import setup, find_packages

setup(
    name='vizit',
    author='DCRichards',
    author_email='',
    description='Simple dependency visualisation in Python',
    version='0.2.3',
    licence='MIT',
    url='https://github.com/DCRichards/vizit',
    packages=find_packages(),
    install_requires=['networkx', 'matplotlib', 'flask'],
    entry_points={
        'console_scripts': [
            'vizit=vizit:main',
        ],
    }
)
