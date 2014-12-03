"""Template for exercise 6.2.

Start with this file to work on exercise 6.2.
Don't modify the predefined function "shift_char".

References:
    * http://de.wikipedia.org/wiki/Polyalphabetische_Substitution

"""

from string import ascii_letters


def shift_char(char, shift, charset):
    """Perform casear shift on a single char.

    Args:
      char (str): the character to be shifted.
      shift (int): the shift performed on each single character
      charset (str): the character set used to define, which input
      characters should be shifted. All other characters remain
        unchanged.

    """
    index = (charset.index(char) + shift) % len(charset)
    return charset[index]


def caesar(fname, shift=0, charset=ascii_letters):
    """Perfom a caesar shift on the input text and return the result.

    Args:
      text (str): the clear text to be encrypted.
      shift (int): the shift performed on each single character
      charset(list of str, optional): the character set used to define which
        input characters should be shifted. All other characters remain
        unchanged. Defaults to string.ascii_letters.

    Examples:

    >>> caesar("abc", -2)
    'YZa'
    >>> caesar("YZa", 2)
    'abc'

    """
    try:
        file = open(fname, mode='r')
        text = file.read()
        file.close()
    except IOError:
        print("No file '%s' found. Using Demo text." % fname)
        text = "abcdefghijklmnopqrstuvwxyz"
    # prepare an empty list to be filled with the encrypted text
    encoded = []
    for char in text:
        new_char = char
        # only shift character, if it is member of the character set
        if char in charset:
            new_char = shift_char(char, shift, charset)
        encoded.append(new_char)
    file = open(fname + ".enc", mode='w')
    file.write(''.join(encoded))
    file.close()
    # return a string representation of the resulting list
    return ''.join(encoded)
    

if __name__ == "__main__":
    encrypted = caesar("caesar.txt", 3)
    decrypted = caesar("caesar.txt.enc", 3)
    print(encrypted, decrypted, sep='\n')
