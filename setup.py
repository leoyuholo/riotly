from setuptools import setup, find_packages

setup(
	name='riotly-coding-test',
	description='Riotly coding test for software engineer',
	author='Leo Yu Ho, Lo',
	author_email='leoyuholo@gmail.com',
	packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-PyMongo'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ]
)
