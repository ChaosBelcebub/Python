'''File with corrected version of next_word and the word_tree
.. versionadded:: 2014-11-20
.. moduleauthor:: Michael Kotzjan <mich3ael@web.de>
'''

LETTERS = "abcdefghijklmnopqrstuvwxyz"+\
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+\
"ÄÖÜäöüß"

def _next_word_helper(s):
    '''Helper function for next_word

    Args:
      s (string): a string
        Holds the sentence

    Returns:
      tupel: 2 elements, first the next word, second the other string
        first element is None if s[0] not in LETTERS

    Examples:

      >>> _next_word_helper("Test test")
      ('Test', ' test')
      >>> _next_word_helper("HelloWorld")
      ('HelloWorld', '')
    '''
    
    if not s:
        return None, s
    """if s[0] not in LETTERS"""
    """Syntaxfehler, nach einer If Anweisung muss ein Doppelpunkt stehen"""
    if s[0] not in LETTERS:
        return None, s
    word = s[0]
    word_rest, s_rest = _next_word_helper(s[1:])
    if word_rest:
        """word = word_rest"""
        """Semantischer Fehler. Es wird immer nur ein Buchstabe zurückgegeben"""
        """Nicht ein ganzes Wort"""
        word = word + word_rest
    return word, s_rest

def next_word(s):
    '''Return the first word of an given string. Eats leading punctation marcs,
    white spaces, etc.

    Args:
      s (string): a string
        Holds the sentence

    Returns:
      tupel: a tupel, returned by _next_word_helper()

    Examples:

      >>> next_word("")
      (None, '')
      >>> next_word("")
      (None, '')
    '''
    
    """while s[0] not in LETTERS:"""
    """Wenn s = "" dann tritt hier ein laufzeitfehler auf"""
    if len(s) == 0:
        return (None, "")
    while s[0] not in LETTERS:
        s=s[1:]
    return _next_word_helper(s)

def lexi_sort(word, w):
    '''Test two words for lexikographic sorting

    Args:
      word (string): a string
        Holds the word of the tree
      w (string): a string
        Holds the word which should be tested

    Returns:
      integer: if w should be sorted left, else 2

    Examples:

      >>> lexi_sort("a", "b")
      2
      >>> lexi_sort("Hallo", "Welt")
      2
      >>> lexi_sort("Welt", "Hallo")
      1
      >>> lexi_sort("aaab", "aaaa")
      1
    '''
    
    if w < word:
        return 1
    else:
        return 2

def to_tuple(l):
    '''Change a list and all its sub lists into tuples

    Args:
      l (list): a nested list

    Returns:
      tuple: returns the changed list

    Examples:
      >>> to_tuple(['a', ['a', 'b'], ['a', 'b']])
      ('a', ('a', 'b'), ('a', 'b'))
      >>> to_tuple(['a', 'b'])
      ('a', 'b')
      >>> to_tuple([])
      ()
      >>> to_tuple([[['a', 'b'],],])
      ((('a', 'b'),),)
    '''
    for i in range(len(l)):
        if isinstance(l[i], list):
            l[i] = to_tuple(l[i])
    return tuple(l)

def word_tree(s):
    '''Generate a sorted tree of an string

    Args:
      s (string): a string
        Holds the sequence of words

    Returns:
      tuple: return the tree

    Examples:

      >>> word_tree('a')
      ('a', None, None, 1)
      >>> word_tree('')
      (None, None, None, 1)
      >>> word_tree('b a c')
      ('b', ('a', None, None, 1), ('c', None, None, 1), 1)
      >>> word_tree("g h j a b g g i i b")
      ('g', ('a', None, ('b', None, None, 2), 1), ('h', None, ('j', ('i', None, None, 2), None, 1), 1), 3)
    '''
    
    word, rest = next_word(s)
    wordtree = [word, None, None, 1]
    while rest != "":
        tree = wordtree
        word, rest = next_word(rest)
        while True:
            if tree[0] == word:
                tree[3] += 1
                break
            elif lexi_sort(word, tree[0]) == 2:
                if tree[1] is None:
                    tree[1] = [word, None, None, 1]
                    break
                else:
                    tree = tree[1]
            else:
                if tree[2] is None:
                    tree[2] = [word, None, None, 1]
                    break
                else:
                    tree = tree[2]
    return to_tuple(wordtree)

def freq_word_tree(tree, word):
    '''Returns the frequency of an given word in a tree

    Args:
      tree (tupel): a tupel
        The tree
      word (string): a string
        The given word

    Returns:
      integer: the frequency of word

    Examples:

      >>> freq_word_tree(('a', None, ('b', None, ('c', None, None, 3), 2), 1), 'a')
      1
      >>> freq_word_tree(('a', None, ('b', None, ('c', None, None, 3), 2), 1), 'b')
      2
      >>> freq_word_tree(('a', None, ('b', None, ('c', None, None, 3), 2), 1), 'c')
      3
      >>> freq_word_tree(('a', None, ('b', None, ('c', None, None, 3), 2), 1), 'd')
      0
    '''
    if tree is None:
        return 0
    elif tree[0] == word:
        return tree[3]
    elif tree[0] > word:
        return freq_word_tree(tree[1], word)
    else:
        return freq_word_tree(tree[2], word)

