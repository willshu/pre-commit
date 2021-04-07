from setuptools import setup
from setuptools import find_packages

setup(
    name='pre-commit-hooks',
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'check-tabs = pre_commit_hooks.check_tabs:main',
        ],
    }
)