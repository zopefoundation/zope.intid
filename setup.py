##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# https://zopetoolkit.readthedocs.io/
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.intid package
"""
import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


TESTS_REQUIRE = [
    'ZODB',
    'zope.testing',
    'zope.site',
    'zope.traversing',
    'zope.container',
]

setup(name='zope.intid',
      version=read('version.txt').strip(),
      author='Albertas Agejevas and Gintautas Miliauskas',
      author_email='zope-dev@zope.dev',
      maintainer='Zope developers',
      maintainer_email='zope-dev@zope.dev',
      description='Integer Id Utility',
      long_description=(
          read('README.rst')
          + '\n\n' +
          read('CHANGES.rst')
      ),
      keywords="zope3 integer id utility",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Programming Language :: Python :: 3.13',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='http://github.com/zopefoundation/zope.intid',
      license='ZPL-2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope'],
      python_requires='>=3.9',
      extras_require={
          'test': TESTS_REQUIRE,
          'docs': [
              'repoze.sphinx.autointerface',
              'sphinx_rtd_theme',
              'Sphinx',
          ],
      },
      install_requires=[
          'persistent',
          'BTrees',
          'setuptools',
          'zope.lifecycleevent>=3.5.2',
          'zope.component',
          'zope.event',
          'zope.interface',
          'zope.keyreference',
          'zope.location>=3.5.4',
          'zope.security',
      ],
      include_package_data=True,
      zip_safe=False,
      )
