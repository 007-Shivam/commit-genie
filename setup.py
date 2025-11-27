from setuptools import setup, find_packages

# Read your README for the long description on PyPI
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-commit",  # ⚠️ Check pypi.org to make sure "ai-commit" isn't taken!
    version="1.0.0",
    author="Shivam Bhosle",
    author_email="shivambhosle270903@gmail.com",
    description="A CLI tool that writes your git commit messages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/007-shivam/ai-commit",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "gitpython",
        "google-generativeai",
    ],
    entry_points={
        "console_scripts": [
            "ai-commit=ai_commit.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)