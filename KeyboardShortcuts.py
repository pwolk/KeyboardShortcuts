#! /usr/bin/python
# -*- coding: utf-8 -*-
"""

This module expands keyboard abbreviations into the full-length text intended.
The combinations of keyboard shortcuts and full-length text are defined in the *.ini file.
'ctrl+alt+q' quits the program

"""
__version__ = "0.1.6"
__author__ = "Pieter van der Wolk"

__copyright__ = "Copyright 2022, Pieter van der Wolk"

__status__ = "beta"  # "pre-alpha" / "alpha" / "beta" / "RC" / "RTM" / "GA" / "Gold"   # https://en.wikipedia.org/wiki/Software_release_life_cycle

# __Python-version-used__ = "3.9.5"

"""
Bugs

2. configparser sets every key to lowercase. - solved: setting configparser
3. prevent the program from running more than one instance - todo 17-09-2021

"""

"""
Feature requests


"""

"""
installation of dependencies

pip install keyboard
pip install configparser

"""

fHTML = False
fVerbose = False

import keyboard
import configparser

config = configparser.ConfigParser()
config.optionxform = str  # otherwise, all keys are converted to lowercase - bug 2
config.sections()
config.read('KeyboardShortcuts.ini')

def KeyboardShortcuts():
    """
    This subroutine connects an action to the F12 key, which is the key connected ot the Herga pedal
    Currently in translates F12 to F8, which in turn links to make screenshot
    Note: chances are you don't have a Herga pedal. You can trigger this action with F12.

    The option is defined in the KeyboardShortcuts.ini file

    screenshot = F8 = screenshot.py
    pagedown = PgDn keypress

    Returns
    -------
    None.

    """
    if fVerbose: print("Got F12!")
    # run a program
    # command = subprocess.run(['ls', '-l'], )
    # subprocess.run(r'C:\Python3\python.exe C:\Users\me\Desktop\screenshots\Screenshots.py')
    # os.startfile(r'C:\Windows\notepad.exe')
    # os.system(r'C:\Users\me\Desktop\screenshots\Screenshots.py')
    if config['F12 function']["F12"] == "screenshot": keyboard.send('F8')
    if config['F12 function']["F12"] == "PageDown": keyboard.send('pagedown')


keyboard.add_hotkey('F12', KeyboardShortcuts)

fHTML = config['HTML']['HTML mode']


for key in config['Abbreviations']:
    if fVerbose: print(key, config['Abbreviations'][key])
    keyboard.add_abbreviation(key, config['Abbreviations'][key])

# keyboard.add_abbreviation('@@', 'MyEmailName@my-email-domain.com')


if fHTML:               # this is an extra library that can be switched on or off, with HTML codes
    # keyboard.add_abbreviation('CO2', r'CO<sub>2</sub>')
    for key in config['HTML Abbreviations']:
        if fVerbose: print(key, config['HTML Abbreviations'][key])
        keyboard.add_abbreviation(key, config['HTML Abbreviations'][key])


keyboard.wait('ctrl+shift+q')   # 'ctrl+alt+q' quits the program
