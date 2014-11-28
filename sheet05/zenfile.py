'''File with fileprogressing
.. versionadded:: 2014-11-27
.. moduleauthor:: Michael Kotzjan <mich3ael@web.de>
'''

import os


def add_zen(fname):
    '''Function for adding the pythonzen to file

    Args:
      fname (string):
        The filename

    Returns:
      Nothing
    '''

    file = open("./testing/" + fname, mode='a')
    try:
        a = os.popen('python3.2 -m this')
        file.write(a.read())
    finally:
        file.close()


def readchar(fname, lower, upper):
    '''Function for reading a string from file of given length

    Args:
      fname (string):
        The Filename
      lower (integer):
        Read from here
      upper (integer):
        to here

    Returns:
      string: the string of the file from lower to upper
    '''

    file = open("./testing/" + fname, mode='r')
    try:
        text = file.read()
        if len(text) < upper:
            raise ValueError("Die Datei enthält weniger Zeichen als\
                              die obere Grenze!")
        else:
            # Ich gebe hier den Index aus
            return text[lower:upper+1]
    finally:
        file.close()


def test_readchar():
    file = open("./testing/test", mode='w')
    a = "Hallo Welt! Wie geht es dir?"
    file.write(a)
    file.close()

    assert readchar("test", 0, 5) == 'Hallo '
    assert readchar("test", 5, 6) == ' W'
    assert readchar("test", 0, 27) == 'Hallo Welt! Wie geht es dir?'
    # Teste auf ValueError
    try:
        readchar("test", 25, 29)
    except ValueError:
        pass
    else:
        print("ERROR")
