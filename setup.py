from setuptools import setup

setup(
    name='pre_commit_hooks',
    entry_points={
        'console_scripts': [
            'check-tabs = pre_commit_hooks.check_tabs.:main',
        ],
    }
)