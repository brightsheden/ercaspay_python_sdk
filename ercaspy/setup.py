from setuptools import setup, find_packages

setup(
    name="ercaspy",
    version="0.1.0",
    description="A Python SDK for interacting with the Ercaspay payment gateway.",
long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Shedenbright",
    author_email="shedenbright@gmail.com",
    url="https://github.com/yourusername/ercaspy", 
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pydantic>=1.10.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
