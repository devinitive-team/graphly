import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphly",
    version="1.0.4",
    author="devinitive",
    author_email="devinitive@placeholder.com",
    description="A small library for studying graphs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devinitive-team/graphly",
    packages=setuptools.find_packages(),
    install_requires=[
        "networkx",
        "matplotlib",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
