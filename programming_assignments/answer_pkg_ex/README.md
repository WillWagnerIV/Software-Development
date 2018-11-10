# The Answer Package

This is a simple example package. 
Github Markdown reference:
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)


## About

This package provides a most basic setup example of an installable package.  As a bonus it also provides the answer to Life, the Universe and Everything.


## Installation Instructions

You can use pip to install from TestPyPI:

1.) cd to your working directory

    cd path/to/awesomeness

2.) Activate your virtual env

    env/bin/activate

3.) Install with the following command

    python3 -m pip install --index-url https://test.pypi.org/ answer_pkg_ex


## Test Installation

You can test that it was installed correctly by importing the module and referencing the name property.

Start your Python interpreter (make sure you are still in your virtualenv if you are using one):

    python

And then import the module and print out the name property.

    import answer_pkg_ex
    answer_pkg_ex.name

'answer_pkg_ex'

## Package Use

The package only has one callable function named provide_insight()

    import answer_pkg_ex

    answer_pkg_ex.provide_insight()