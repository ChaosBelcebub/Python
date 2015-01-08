"""Template for exercise 6.3.

Start with this file to work on exercise 6.3.
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


def vigenere(text, secret, charset=ascii_letters):
    """Perfom a vigenere encoding on the input text and return the result.

    Args:
      text (str): the clear text to be encrypted.
      secret (str): the secret string to shift each single character
      charset (str, optional): the character set used to define which
        input characters should be shifted. All other characters remain
        unchanged. Defaults to string.ascii_letters.

    Examples:

    >>> vigenere("1. Advent", "Kerze")
    '1. ZhfiES'

    """
    # your code follows here
    for char in secret:
        if char not in charset:
            return None
    index = 0
    index_max = len(secret)
    encoded = []
    for char in text:
        new_char = char
        if char in charset:
            new_char = shift_char(char, charset.index(secret[index]), charset)
        index += 1
        if index == index_max:
            index = 0
        encoded.append(new_char)
    return ''.join(encoded)


def test_vigenere():
    assert vigenere("1. Advent", "Kerze") == "1. ZhfiES"
    assert vigenere("1. Advent", "Ker ze") == None
    assert vigenere("geheimnis", "akey") == "golCiwrGs"
    assert vigenere("Dies ist ein Test!", "Schokolade") == "vklG wDt iap hoGE!"


if __name__ == "__main__":
    encrypted = vigenere("1. Advent", "Kerze")
    print(encrypted)
    test_vigenere()
