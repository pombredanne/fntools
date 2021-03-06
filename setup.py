from setuptools import setup
import fntools


setup(name='fntools',
      version=fntools.__version__,
      description='Functional programming tools for data processing',
      long_description=open('README.rst').read(),
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
          ],
      author=u'Taurus Olson',
      author_email=u'taurusolson@gmail.com',
      url='https://github.com/TaurusOlson/fntools',
      packages=['fntools'],
      keywords='functional programming tools data processing',
      license=fntools.__license__,
      include_package_data=True,
      zip_safe=False
      )
