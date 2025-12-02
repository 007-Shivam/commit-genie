from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="commit-genie",  
    version="1.0.4",
    author="Shivam Bhosle",
    author_email="shivambhosle270903@gmail.com",
    description="A CLI tool that writes your git commit messages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/007-shivam/commit-genie",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "gitpython",
        "google-generativeai",
    ],
    entry_points={
        "console_scripts": [
            "commit-genie=commit_genie.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)