import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ['pyramid',
            'pyramid_beaker',
            'WebError',
            'httplib2',
            ]

setup(name='sparql_shim',
      version='0.0',
      description='sparql_shim',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Nicholas Pilon',
      author_email='npilon@gmail.com',
      url='https://github.com/npilon/sparql-shim',
      keywords='web pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="sparql_shim",
      entry_points = """\
      [paste.app_factory]
      main = sparql_shim:main
      """,
      paster_plugins=['pyramid'],
      )

