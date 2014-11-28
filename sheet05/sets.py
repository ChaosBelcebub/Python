'''File for sets
.. versionadded:: 2014-11-27
.. moduleauthor:: Michael Kotzjan <mich3ael@web.de>
'''


def subsets(s, k):
    '''Returns the subsets of s with length k

    Args:
      s (set):
        The set
      k (integer):
        the length of the wanted subset

    Returns:
      set: set of the subsets
    '''
    result = set()
    for e in s:
        if len(e) == k:
            result.add(e)
    return result


def permutations(s, k):
    '''Returns the permutations of s with length k

    Args:
      s (set):
        The set
      k (integer):
        the length of the wanted subset

    Returns:
      set: set of tuples
    '''
    out = set()
    if k == 1:
        out = set(s)
    elif k < 1:
        pass
    else:
        for e in s:
            if k > 1:
                t = s.copy()
                t.remove(e)
                for perm in permutations(t, k-1):
                    out.add((e,) + (perm,))
            else:
                out.add(e)
    return out

# Global variable for testing
test_lst = ["a", "b", "aa", "ab", "ba", "bb", "abc", "Test", "Welt"]
test = set(test_lst)
test2_lst = ["a", "b", "ca", "hey"]
test2 = set(test2_lst)


def test_subsets_one():
    assert subsets(test, -1) == set()


def test_subsets_two():
    assert subsets(test, 1) == {"a", "b"}


def test_subsets_three():
    assert subsets(test, 2) == {"aa", "ab", "ba", "bb"}


def test_subsets_four():
    assert subsets(test, 5) == set()


def test_permutations_one():
    assert permutations(test2, 0) == set()


def test_permutations_two():
    assert permutations(test2, 1) == {"a", "b", "ca", "hey"}


def test_permutations_three():
    assert permutations(test2, 2) == {("a", "b"), ("a", "ca"), ("a", "hey"),
                                      ("b", "a"), ("b", "ca"), ("b", "hey"),
                                      ("ca", "a"), ("ca", "b"), ("ca", "hey"),
                                      ("hey", "a"), ("hey", "b"),
                                      ("hey", "ca")}


def test_permutations_four():
    assert permutations(test2, 5) == set()
