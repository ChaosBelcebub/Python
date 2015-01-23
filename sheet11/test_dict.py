"""This is a template file for using the timeit module.

   The timeit module can process strings as well as callables. The second
   testing routine uses that. If you get into any namespace troubles try the
   first version and consult the online documentation.

"""
dictionary = {}

def init():
    for i in range(1000):
        dictionary[i] = "test"


def func_a():
    pass


def func_b():
    pass


def func_c():
    pass


if __name__ == '__main__':
    init()
    print(dictionary)
    import timeit

    repeat = 5
    number = 1000
    unit = "usec"
    unittosec = {"usec": 1e6, "msec": 1000, "sec": 1}

    for fct_name in ["func_a", "func_b", "func_c"]:
        res = timeit.repeat(
            "%s()" % fct_name,
            setup="from __main__ import %s" % fct_name,
            repeat=repeat, number=number)
        print("%s: %d loops, best of %d: %.3g %s per loop" %
              (fct_name,
               number, repeat,
               min(res) / number * unittosec[unit],
               unit))

    # Second (alternative) version:
    for fct in [func_a, func_b, func_c]:
        res = timeit.repeat(
            fct,
            repeat=repeat, number=number)
        print("%s: %d loops, best of %d: %.3g %s per loop" %
              (fct.__name__,
               number, repeat,
               min(res) / number * unittosec[unit],
               unit))
