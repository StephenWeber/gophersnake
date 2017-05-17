from setuptools import setup

setup(
    name='gophersnake',
    version='1.0.0',
    description='A gopher server written in Python',
    license='MIT',
    packages=['gophersnake'],
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'gophersnake=gophersnake.gophersnake:main',
        ],
    },
)