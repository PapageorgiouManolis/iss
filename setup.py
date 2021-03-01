from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="ISS's location prediction",
    version="0.0.1",
    long_description=readme(),
    author='manolisisv@gmail.com',
    install_requires=[
    ],
    include_package_data=True)
