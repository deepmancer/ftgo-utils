from setuptools import setup, find_packages

setup(
    name="ftgo_utils",
    version="0.1.2",
    description="Shared utilities for FTGO platform",
    author="Alireza Heidari",
    author_email="alirezaheidari.cs@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "aiocache",
        "argon2_cffi",
        "asyncpg",
        "bcrypt",
        "colorama",
        "email-validator==2.1.0",
        "greenlet",
        "httpx",
        "loguru",
        "passlib",
        "pyotp",
        "psycopg2-binary",
        "pydantic",
        "PyJWT",
        "python-jose[cryptography]",
        "python-slugify",
        "pytz",
        "redis",
        "pwdlib",
        "sqlalchemy",
        "validators"
    ],
)
