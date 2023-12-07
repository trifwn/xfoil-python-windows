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
import os 
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

def get_package_version() -> str:
    """Get the package version from the __init__ file"""
    __version__ = re.findall(
        r"""__version__ = ["']+([0-9\.]*)["']+""",
        open('xfoil/__init__.py').read(),
    )[0]
    return __version__

def main():
    package = 'xfoil'
    __version__ = get_package_version()

    if len(sys.argv) >= 2:
        command: str = sys.argv[1]
    else:
        command = ""

    if command == "uninstall":
        uninstall(package)
    else:
        install(package, __version__)
        print(f"Command {command} not recognized")

def install(package: str, version: str) -> None:
    """INSTALL THE PACKAGE

    Args:
        package (str): Package Name
        version (str): Version Number
    """
    setup(
        name=package,
        version=version,
        packages=['xfoil'],
        package_data= {'xfoil': ['libxfoil.dll',"libxfoil.dll.a"]},
        include_package_data=True,
    )

def uninstall(package: str) -> None:
    """Uninstall the package

    Args:
        package (str): Package Name
    """
    try:
        import pip
    except ImportError:
        print("Error importing pip")
        return

    import sys, shutil
    # clean up local egg-info
    try:
        shutil.rmtree(package + '.egg-info')
    except:
        pass     

        # setup up uninstall arguments
    args = sys.argv
    del args[0:1+1]
    args = ['uninstall', package] + args
    
    # uninstall
    try:
        pip.main(args)
    except:
        pass

if __name__ == "__main__":
    main()