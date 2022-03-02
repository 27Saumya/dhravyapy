from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = "0.0.6"

setup(
    name="dhravyapy",
    author="27Saumya",
    url="https://github.com/27Saumya/dhravyapy",
    download_url="https://github.com/27Saumya/dhravyapy/archive/v0.0.6.tar.gz",
    version=version,
    packages=["dhravyapy"],
    license="MIT",
    description="An asynchronous wrapper for interacting with the Dhravya API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
