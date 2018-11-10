# The Answer Package

This is a simple example package. 

## About

This package provides a most basic setup example of an installable package.  As a bonus it also provides the answer to Life, the Universe and Everything.  Make sure to call the function provide_insight() after installation.


## Installation Instructions

testPyPi erases its content without warning to create space for new test projects.  If there are any errors with testPyPi, please use the tar package instructions.

### testPyPi Installation ( Easiest )

You can use pip to install from TestPyPI:

1.) cd to your working directory.

    cd path/to/awesomeness

2.) Activate your virtual env

    env/bin/activate

3.) Install with the following command

    python3 -m pip install --index-url https://test.pypi.org/ answer_pkg_ex

### tar Package Installation

1.) You can download the tar archive here:

  <https://github.com/WillWagnerIV/Software-Development/tree/master/programming_assignments/answer_pkg_ex/dist/>

2.) copy the downloaded tar to your working directory

3.) cd to your working directory.

    cd path/to/awesomeness

4.) Activate your virtual env

    env/bin/activate

5.) use pip to install the archive.  The following is example code.  Please change the version to match your download.

    python3 -m pip install python3 -m pip install answer_pkg_ex-0.0.13.tar.gz

## Test Installation

You can test that it was installed correctly by importing the module and referencing the name property.

Start your Python interpreter (make sure you are still in your virtualenv if you are using one):

    python

And then import the module and print out the name property.

    import answer_pkg_ex
    answer_pkg_ex.name

'answer_pkg_ex'

## Package Use

### provide_insight()

The package's only callable function is named __provide_insight()__.  Import it and call it like this:

    import answer_pkg_ex

    answer_pkg_ex.provide_insight()