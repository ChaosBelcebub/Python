"""This is a template file for using the timeit module.

   The timeit module can process strings as well as callables. The second
   testing routine uses that. If you get into any namespace troubles try the
   first version and consult the online documentation.

"""
dictionary = {}
keys_all = list(range(1000))
keys_half = list(range(500)) + list(range(1000, 1500))
keys_none = list(range(1000, 2000))
def init():
    for i in range(1000):
        dictionary[i] = "test"


def func_if_all():
    for k in keys_all:
        if k in dictionary:
            test = dictionary[k]


def func_if_half():
    for k in keys_half:
        if k in dictionary:
            test = dictionary[k]


def func_if_none():
    for k in keys_none:
        if k in dictionary:
            test = dictionary[k]


def func_try_all():
    for k in keys_all:
        try:
            test = dictionary[k]
        except:
            pass


def func_try_half():
    for k in keys_half:
        try:
            test = dictionary[k]
        except:
            pass


def func_try_none():
    for k in keys_none:
        try:
            test = dictionary[k]
        except:
            pass


if __name__ == '__main__':
    init()
    import timeit

    repeat = 5
    number = 1000
    unit = "usec"
    unittosec = {"usec": 1e6, "msec": 1000, "sec": 1}

    for fct_name in ["func_if_all", "func_if_half", "func_if_none",
                     "func_try_all", "func_try_half", "func_try_none"]:
        res = timeit.repeat(
            "%s()" % fct_name,
            setup="from __main__ import %s" % fct_name,
            repeat=repeat, number=number)
        print("%s: %d loops, best of %d: %.3g %s per loop" %
              (fct_name,
               number, repeat,
               min(res) / number * unittosec[unit],
               unit))

##    # Second (alternative) version:
##    for fct in [func_a, func_b, func_c]:
##        res = timeit.repeat(
##            fct,
##            repeat=repeat, number=number)
##        print("%s: %d loops, best of %d: %.3g %s per loop" %
##              (fct.__name__,
##               number, repeat,
##               min(res) / number * unittosec[unit],
##               unit))
