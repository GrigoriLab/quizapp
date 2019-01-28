"""Setuptools script."""

from setuptools import setup, find_packages


setup(
    name='quiz',
    version='1.0',
    description='Quiz app',
    long_description="Quiz app",
    classifiers=[
        "Programming Language :: Python"
    ],
    author='Grigori Kartashyan',
    author_email='grigori.kartashyan@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='quiz',
    install_requires=['behave']
)
