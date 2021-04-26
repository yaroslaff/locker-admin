from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='locker-admin',
      version='0.1',
      description='locker-admin',
      url='https://github.com/yaroslaff/locker-admin',
      author='Yaroslav Polyakov',
      author_email='yaroslaff@gmail.com',
      license='MIT',
      packages=['locker-client'],
      scripts=['bin/locker-admin'],
      # include_package_data=True,

      long_description = read('README.md'),
      long_description_content_type='text/markdown',

      install_requires=[],
      zip_safe=False
      )

