from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-mopac',
    version=version,
    description="Mopac client extension",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Toby Dacre',
    author_email='toby.dacre@whythawk.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.mopac'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        mopac=ckanext.mopac.plugin:Mopac
    ''',
)
