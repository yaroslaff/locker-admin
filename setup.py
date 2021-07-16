from setuptools import setup
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from locker_client import version

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='locker-admin',
      version=version,
      description='locker-admin',
      url='https://github.com/yaroslaff/locker-admin',
      author='Yaroslav Polyakov',
      author_email='yaroslaff@gmail.com',
      license='MIT',
      packages=['locker_client'],
      scripts=['bin/locker-admin'],
      # include_package_data=True,

      long_description = read('README.md'),
      long_description_content_type='text/markdown',

      install_requires=['requests', 'python-dotenv'],
      zip_safe=False
      )

