# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup, find_packages

long_desc = Path("README.rst").read_text()

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-mscgenjs',
    version='0.1',
    url='https://github.com/LoveIsGrief/sphinxcontrib-mscgenjs',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-mscgenjs',
    license='BOLA',
    author='LoveIsGrief',
    author_email='loveisgrief@tuta.io',
    description='mscgenjs Sphinx extension',
    long_description=long_desc,
    zip_safe=False,
    project_urls={
        "Bugs": "https://github.com/LoveIsGrief/sphinxcontrib-mscgenjs/issues"
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
