def subsets(s, k):
    result = set()
    for e in s:
        if len(e) == k:
            result.add(e)
    return result


def permutations(s, k):
    return set(perm_helper(s, k))


def perm_helper(s, k):
    out = []
    if len(s) == 1:
        out = set(s)
    else:
        for e in s:
            if k > 1:
                t = s.copy()
                t.remove(e)
                for perm in perm_helper(t, k-1):
                    if isinstance(perm, str):
                        out.append(tuple([e]) + tuple([perm]))
                    else:
                        out.append(tuple([e]) + tuple(perm))
            else:
                out.append(e)
    return out
