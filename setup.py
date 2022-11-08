"""A package to monitor journal RSS feeds and tweet new articles."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="feedpapers",
    version="1.0.3",
    author="Jemma Stachelek",
    author_email="stachel2@msu.edu",
    description="A package to monitor journal RSS feeds and tweet new \
                articles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feedpapers/feedpapers",
    scripts=["bin/feedpapers"],
    include_package_data=True,
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
