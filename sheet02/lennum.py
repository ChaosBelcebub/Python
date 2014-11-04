def binlen(n):
    """Return the length of the binary representation of a natural nummber.

    """
    result = 0
    if type(n) != int:
        return None
    if n < 0:
        return None
    if n == 0:
        result = 1

    while n > 0:
        n = int(n / 2)
        result += 1

    return result
