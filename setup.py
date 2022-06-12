# -*- coding: utf-8 -*-
#
# vim: expandtab shiftwidth=4 softtabstop=4
#
from setuptools import setup
import io

version = "0.7.1"

long_description = (
    io.open("README.rst", encoding="utf-8").read() + "\n" + "Contributors\n"
    "============\n"
    + "\n"
    + io.open("docs/source/CONTRIBUTORS.rst", encoding="utf-8").read()
    + "\n"
    + io.open("CHANGES.rst", encoding="utf-8").read()
    + "\n"
)

setup(
    name="pyncclient",
    version=version,
    author="Suriem Kumite",
    author_email="salvo@test.com",
    packages=["nextcloud_client", "nextcloud_client.test"],
    url="https://github.com/surkum/pyncclient",
    license="LICENSE.txt",
    description="Python client library for nextCloud",
    long_description=long_description,
    install_requires=["requests >= 2.0.1", "six"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
