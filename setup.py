# -*- coding: utf-8 -*-
#   Copyright (c) 2019 D. de Vries
#
#   This file is part of XFoil.
#
#   XFoil is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   XFoil is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with XFoil.  If not, see <https://www.gnu.org/licenses/>.
import re
from setuptools import setup

__version__ = re.findall(
    r"""__version__ = ["']+([0-9\.]*)["']+""",
    open('xfoil/__init__.py').read(),
)[0]

def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='xfoil',
    version=__version__,
    description='Stripped down version of XFOIL as compiled python module ',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Fortran',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
    ],
    keywords='xfoil airfoil aerodynamic analysis',
    url='https://github.com/daniel-de-vries/xfoil-python',
    download_url='https://github.com/daniel-de-vries/xfoil-python/tarball/' + __version__,
    author='Daniël de Vries',
    author_email='contact@daniel-de-vries.com',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=['xfoil'],
    # package_dir={'': 'src'},
    install_requires=['numpy'],
)
