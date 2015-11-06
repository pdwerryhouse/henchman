from setuptools import setup, find_packages
import sys, os

version = '0.0.2'

setup(name='henchman',
      version=version,
      description="Orchestration engine without a DSL",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Paul Dwerryhouse',
      author_email='paul@dwerryhouse.com.au',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
