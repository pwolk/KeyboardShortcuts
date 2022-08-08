#! /usr/bin/python
# -*- coding: utf-8 -*-
"""

This module expands keyboard abbreviations into the full-length text intended.
The combinations of keyboard shortcuts and full-length text are defined in the *.ini file.
'ctrl+shift+q' quits the program

"""
__version__ = "0.1.7"
__author__ = "Pieter van der Wolk"

__copyright__ = "Copyright 2022, Pieter van der Wolk"

__status__ = "beta"  # "pre-alpha" / "alpha" / "beta" / "RC" / "RTM" / "GA" / "Gold"   # https://en.wikipedia.org/wiki/Software_release_life_cycle

# __Python-version-used__ = "3.9.5"

"""
Bugs

2. configparser sets every key to lowercase. - solved: setting configparser
3. prevent the program from running more than one instance - done 08-08-2022; using tendo
4. remove extra functionality: extended HTML function, etc.

"""

"""
Feature requests

6. standalone executable: "pyinstaller --onefile KeyboardShortcuts.py"

"""

"""
installation of dependencies

pip install keyboard
pip install configparser
pip install tendo

"""

fVerbose = False

import keyboard
import configparser
from tendo import singleton  # takes care of running only one instance. It does double the size of the executable. Tendo can also untangle UTF-woes https://pythonhosted.org/tendo/

me = singleton.SingleInstance() # will sys.exit(-1) if other instance is running

config = configparser.ConfigParser()
config.optionxform = str  # otherwise, all keys are converted to lowercase - bug 2
config.sections()
config.read('KeyboardShortcuts.ini')

for key in config['Abbreviations']:
    if fVerbose: print(key, config['Abbreviations'][key])
    keyboard.add_abbreviation(key, config['Abbreviations'][key])

keyboard.wait('ctrl+shift+q')   # 'ctrl+shift+q' quits the program
