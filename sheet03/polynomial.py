''' File for derif functions '''

def first_derif(t):
    '''Calculate the first derif of a given polynomial expression

    Args:
      t (tupel): a tupel of integer
        Holds the polynomial expression

    Returns:
      tupel: empty tupel if result contains only a 0, otherwise the derif

    Examples:
    
      >>> first_derif((3, 2, 1))
      (6, 2)
      >>> first_derif((4, 3, 2))
      (8, 3)
      >>> first_derif((4, 2))
      (4,)
      >>> first_derif((-2, 5, 2))
      (-4, 5)
    '''

    result = []
    length = len(t)
    count = 1
    if len(t) == 1:
        return (0,)
    for f in t:
        if (f * (length - count)) != 0:
            result.insert(count - 1, f * (length - count))
        count += 1
    return tuple(result)

def derif(t, k):
    '''Calculate the k derif of a given polynomial expression

    Args:
      t (tupel): a tupel of integer
        Holds the polynomial expression
      k (int): a integer
        Holds the number of derifs

    Returns:
      tupel: tuple or None: Tuple if k >= 0, None otherwise

    Examples:
    
      >>> derif((3, 2, 1), -1)
      
      >>> derif((3, 2, 1), 2)
      (6,)
      >>> derif((6, 8, 3, 2), 3)
      (36,)
      >>> derif((12, 7, 4), 0)
      (12, 7, 4)
    '''
    count = 1
    for i in range(0, k):
        result = []
        length = len(t)
        for f in t:
            if (f * (length - count)) != 0:
                result.insert(count - 1, f * (length - count))
            count += 1
        count = 1
        t = result
    if k == 0:
        return t
    elif k < 0:
        return None
    else:
        return tuple(result)
