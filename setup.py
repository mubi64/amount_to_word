from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in amount_to_word/__init__.py
from amount_to_word import __version__ as version

setup(
	name="amount_to_word",
	version=version,
	description="this app to change amount to words with currency",
	author="Saad",
	author_email="m.saad@sowaan.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
