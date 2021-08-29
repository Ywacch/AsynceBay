import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="AsynceBay",
    version="0.0.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Ywacch/AsynceBay",
    author="Emmanuel Adebayo",
    author_email="toluwalashe.adebayo@gmail.com",
    license="MIT",
    # packages=find_packages(),
    # install_requires=[],
    include_package_data=True
)
