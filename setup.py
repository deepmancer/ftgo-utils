from setuptools import setup, find_packages

setup(
    name="ftgo_utils",
    version="1.11.7",
    description="Shared utilities for FTGO platform",
    author="Alireza Heidari",
    author_email="alirezaheidari.cs@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/alirezaheidari-cs/ftgo-utils",
    install_requires=[
        "argon2-cffi",
        "bcrypt",
        "colorama",
        "dataclasses",
        "geojson",
        "h3",
        "httpx",
        "loguru",
        "passlib",
        "pyotp",
        "pydantic[email]",
        "PyJWT",
        "python-jose[cryptography]",
        "python-slugify",
        "pytz",
        "pwdlib",
        "validators",
    ],
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    python_requires=">=3.6",
    project_urls={
        "Source": "https://github.com/alirezaheidari-cs/ftgo-utils",
        "Tracker": "https://github.com/alirezaheidari-cs/ftgo-utils/issues",
    },
)
