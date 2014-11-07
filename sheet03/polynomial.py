def first_derif(t):
    result = []
    length = len(t)
    count = 1
    for f in t:
        if (f * (length - count)) != 0:
            result.insert(count - 1, f * (length - count))
        count += 1
    return tuple(result)

def derif(t, k):
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
