import re


# RegEx sind Sinnvoll da der Code so um einiges kürzer ist
def check_for_startcodon(AUGCstring):
    """Checks for startcodon

    Args:
      AUGCstring (string): the AUGC string

    Returns:
      Bool: True or False
    """
    if re.findall(r"AUG", AUGCstring):
        return True
    else:
        return False

# b) r"AUG(?:[AUGC]{3})+UAG"


def extract_codon_string(AUGCstring):
    """Extract codon

    Args:
      AUGCstring (string): the AUGC string

    Returns:
      String: The extracted codon
    """
    return re.findall(r"(?<=AUG)(?:[AUGC]{3})+?(?=UAG)", AUGCstring)


def test_check_for_startcodon():
    assert check_for_startcodon("AUG") is True
    assert check_for_startcodon("UAGAGUGAUGUGA") is True
    assert check_for_startcodon("UAGUAG") is False
    assert check_for_startcodon("") is False


def test_extract_codon_string():
    assert extract_codon_string("AUGCCCUAGAUGCCCUAG") == ['CCC', 'CCC']
    assert extract_codon_string("AUGAUGCCCUAG") == ['AUGCCC']
    assert extract_codon_string("AUGUAG") == []
    assert extract_codon_string("UGAAAUGCCCCCCUAG") == ['CCCCCC']


if __name__ == "__main__":
    test_check_for_startcodon()
    test_extract_codon_string()
