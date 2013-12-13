from setuptools import setup, find_packages
import django_pixel

setup(
	name = "cmsplugin-pixel",
	version = django_pixel.__version__,
	packages = find_packages(),

	author = "Chris Modjeska",
	author_email = "kin@remuria.net",
	description = "",
	keywords = "django",
	url = "https://github.com/csmillions/cmsplugin-javascript/",
	include_package_data=True,
	long_description= """
	""",
	install_requires=[
		"django",
		"django-cms"
	],
)
