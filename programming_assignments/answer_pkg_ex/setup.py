import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="answer_pkg_ex",
    version="0.0.14",
    author="Will Wagner",
    author_email="william.wagner@cgu.edu",
    description="A small example package that provides the answer to Life the Universe and Everything.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WillWagnerIV/Software-Development/tree/master/programming_assignments/answer_pkg_ex/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)