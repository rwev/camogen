#! /usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    name="camogen",
    version="0.1.0",
    description="Randomized camouflage generator",
    author="rwev",
    author_email="rwev@protonmail.ch",
    url="https://gitlab.com/rwev/camogen",
    packages=["camogen"],
    include_package_data=True,
    install_requires=["numpy", "Pillow"],
    license="GNU GPL 3.0",
)

