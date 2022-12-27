# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
import codecs

version = "0.10.0"

setup(
    name="py3o.template",
    version=version,
    description="An easy solution to design reports using LibreOffice",
    long_description=codecs.open(
        "README.rst", mode="r", encoding="utf-8"
    ).read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="LibreOffice OpenOffice templating PDF",
    author="Florent Aide",
    author_email="florent.aide@gmail.com",
    url="http://bitbucket.org/faide/py3o.template",
    license="MIT License",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    namespace_packages=["py3o"],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "setuptools",
        "six >= 1.9",
        "babel",
        "lxml",
        "genshi >= 0.7",
        "pyjon.utils > 0.6",
        "Pillow",
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
    tests_require=["nose", "nosexcover", "mock"],
    test_suite="nose.collector",
)
