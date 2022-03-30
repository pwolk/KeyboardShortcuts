# KeyboardShortcuts

## keyboardShortcuts.py

This program expands keyboard abbreviations into the full-length text intended.

## to try

1. Extract the files ``keyboardShortcuts.py`` and ``keyboardShortcuts.ini`` into a folder
2. Run the program
3. type ``@``-``@``-``<space>`` anywhere in your computer where you can type
4. See it expand into ``MyEmailName@my-email-domain.com``

The combinations of keyboard shortcuts and full-length text are defined in the *.ini file. Start by changing it into your e-mail address.

## How it works

The program emulates keystrokes; if you type ``@``-``@``-``<space>``, then the program quickly types ``<backspace>`` - ``<backspace>`` - ``<backspace>`` - to erase the three characters that just have been typed, and then types ``M`` - ``y`` -``E`` ..., etc.

## How to stop the program

``ctrl``+ ``alt``+``q`` quits the program
