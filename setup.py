import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hlre",
    version="0.1.0",
    author="Zach Gulde",
    author_email="zachgulde@gmail.com",
    description="Interactively highlight regular expression matches",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zgulde/hlre",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "prompt_toolkit>=2",
    ],
    entry_points={"console_scripts": ["hlre = hlre.hlre:main"]}
)
