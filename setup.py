### File: `setup.py`
from setuptools import setup, find_packages

setup(
    name="django-exception-logging-middleware",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["Django>=2.2", "pymongo>=3.11"],
    include_package_data=True,
    description="A Django middleware to log unhandled exceptions and request data to MongoDB.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/johnPractice/django_request_logging_middleware",
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
)
