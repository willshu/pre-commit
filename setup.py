from setuptools import setup

setup(
    name='pre-commit-hooks',
    entry_points={
        'console_scripts': [
            'check-tabs = pre_commit_hooks.check_tabs:main',
        ],
    }
)