from setuptools import setup, find_packages

setup(
    name="fastapi-admin-cli",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fastapi-admin = fastapi_admin.cli:main",
        ],
    },
    install_requires=[
        "fastapi",
        "uvicorn",
    ],
    author="Ritesh Mahale",
    description="A CLI tool to create and manage FastAPI projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/everest1508/fastapi-admin-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
