LAB_SOURCE_FILE = __file__



this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 2:
        return n
    else:
        return n + skip_add(n - 2)


def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n-1, term)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def choices(a, b):
        if a == m - 1:
            return 1
        elif b == n - 1:
            return 1
        else:
            return choices(a + 1, b) + choices(a, b + 1)
    return choices(0, 0)


def digits_list(n):
    """
    change a number in to a list with digits of the number as iterms in the list
    """
    digits = []
    for digit in str(n):
        digits.append(int(digit))
    return digits


def max_subseq_my(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    def max_one_digit(n, t):
        if t == 0:
            return 0
        elif len(str(n)) <= t:
            return n
        elif (n // pow(10, len(str(n)) - 1)) >= max(digits_list(n)[:t+1]):
            return (n // pow(10, len(str(n)) - 1)) * pow(10, t - 1) + max_subseq(n % pow(10, len(str(n)) - 1), t - 1)
        else:
            return max_subseq_my(n % pow(10, len(str(n))-1), t)
    return max_one_digit(n, t)
# 以上代码是我自己写的，所以加了一个my做区分
# 相较于网上看到的其他方法，我的代码过于复杂。原因在于没有考虑使用tree recursion而仅仅是使用了recursion
# 我的思路与tree recursion的区别在于：我想通过找最大的digit，组合成为最大的sub sequence
# 在找最大的digit时，牵扯到要转化为list才可比较，然后要限定list的比较范围
# 而tree recursion则是考虑所有sub sequence组合成的集合，在全集里找最大的那个sequence
# tree recursion分为使用最后一个数字和不使用最后一个数字。看完他人解答后，自己尝试默写一次，熟悉思路


def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    if t == 0:
        return 0
    elif n < 10: # 我刚开始写的条件是len(str(n)) <= t:，但是使用 n<10 这个条件更好，因为 n//10 递归最终会达到0，也就是满足小于10的跳出条件
        return n
    else:
        seq_with_last = max_subseq(n//10, t-1) * 10 + n % 10
        seq_without_last = max_subseq(n//10, t)
        return max(seq_with_last, seq_without_last)


def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"
    if len(w1) == 0:
        return w2
    else:
        if w1[0] == w2[0]:
            return add_chars(w1[1:], w2[1:])
        else:
            return w2[0] + add_chars(w1, w2[1:])
# 我原来使用了list，但其实文本不用list也可以
# if len(list(w1)) == 0:
#     return w2
# else:
#     if list(w1)[0] == list(w2)[0]:
#         return add_chars(w1[1:], w2[1:])
#     else:
#         return w2[0] + add_chars(w1, w2[1:])