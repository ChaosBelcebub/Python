def jos(men, k, count, out):
    if len(men) < 1:
        return
    if count < k:
        jos(men[1:]+[men[0]], k, count + 1, out)
    else:
        out.append(men[0])
        jos(men[1:], k, 1, out)
def josephus(n, k):
    out = []
    jos(list(range(1, n+1)), k, 1, out)
    return out

def test_josephus():
    assert josephus(10, 2) == [2, 4, 6, 8, 10, 3, 7, 1, 9, 5], "Test failed"
    assert josephus(2, 3) == [1, 2], "Test failed"
    assert josephus(1, 5) == [1,], "Test failed"
    assert josephus(0, 2) == [], "Test failed"
