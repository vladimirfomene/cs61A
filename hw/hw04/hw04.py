HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############
from operator import add, sub

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    a_avenue, a_street = avenue(a), street(a)
    b_avenue, b_street = avenue(b), street(b)

    return abs(a_avenue - b_avenue) + abs(a_street - b_street)


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [round((x) ** (1/2)) for x in s if x == round((x) ** (1/2)) * round((x) ** (1/2))]

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """

    curr = n
    prev_one, prev_two, prev_three = 3, 2, 1

    for i in range(3, n):
        curr = prev_one + 2 * prev_two + 3 * prev_three
        prev_one, prev_two, prev_three = curr, prev_one, prev_two
    return curr

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    def pingpong_element(k, i, operator):

        if k == 1:
            return i
        elif (((n + 1) - k) % 7) == 0 or "7" in str((n + 1) - k):
            if operator == add:
                return pingpong_element(k - 1, sub(i, 1), sub)
            else:
                return pingpong_element(k - 1, add(i, 1), add)
        else:
            return pingpong_element(k - 1, operator(i, 1), operator)
    return pingpong_element(n, 1, add)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_change_partitions(amount, coin):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif coin > amount:
            return 0
        else:
            return count_change_partitions(amount - coin, coin) + count_change_partitions(amount, 2 * coin)
    return count_change_partitions(amount, 1)

###################
# Extra Questions #
###################

from operator import sub, mul

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    #return lambda n: 1 if n == 1 else
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1)))) 
