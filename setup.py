from setuptools import setup

setup(
    name='bento_azure_functions',
    version="0.1",

    author='michal.wojdylak',
    author_email='michal.wojdylak@wundermanthompson.com',

    install_requires=[
        "bentoml==0.13.2",
        "azure-functions",
        "flask",
        "docker",
        "pandas",
        "rich",
        "numpy",
        "pillow",
    ],

    entry_points={
        'console_scripts': [
            'deploy=bento_azure_functions.deploy',
            'describe=bento_azure_functions.describe',
        ]
    }
)
