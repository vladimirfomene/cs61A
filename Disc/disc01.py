def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """

    return (temp < 60) || raining

wears_jacket(90, False)
wears_jacket(40, False)
wears_jacket(100, True)


def handle_overflow(s1, s2):

    if s1 > 30 and s2 > 30 :
        print("No space left in either section")
    elif s1 > 30 :
        print("Move to Section 2:", s2 - 30)
    elif s2 > 30 :
        print("Move to section 1", s1 - 30)

def keep_ints(cond, n):
    if cond(n) :
        for i in range(1, n + 1):
            print(i)

def keep_ints(n):

    def print_all(cond):
        if cond(n) :
            for i in range(1, n + 1):
                print(i)
    return print_all
