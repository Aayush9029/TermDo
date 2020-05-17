from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='TermDo',  
    version='1.8',
    author="Aayush Pokharel",
    author_email="aayushpokharel36@gmail.com",
    description="A Todo App for terminal / powerusers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aayush9029/TermDo.git",
    py_modules=["TermDo"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
