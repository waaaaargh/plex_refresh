from setuptools import setup

setup(
    install_requires=[
        "fire",
        "plexapi"
    ],
    name='plexrefresh',
    version='0.1',
    py_modules=['plexrefresh'],
    entry_points={
        'console_scripts': ['plexrefresh=plexrefresh:run']
    },
)
