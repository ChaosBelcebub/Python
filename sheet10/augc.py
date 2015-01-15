import re


# RegEx sind Sinnvoll da der Code so um einiges kürzer ist
def check_for_startcodon(AUGCstring):
    """Checks for startcodon

    Args:
      AUGCstring (string): the AUGC string
    """
    if re.findall(r"AUG", AUGCstring):
        return True
    else:
        return False

# b) r"AUG(?:[AUGC]{3})+UAG"


def extract_codon_string(AUGCstring):
    return re.findall(r"(?<=AUG)(?:[AUGC]{3})+?(?=UAG)", AUGCstring)
