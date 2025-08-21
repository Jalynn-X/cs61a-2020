this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    c = 0
    def adder(b):
        nonlocal c
        result = a + b + c
        c += 1
        return result
    return adder
# 这里我另设了一个nonlocal变量c
# 网上看到别人的解法是直接nonlocal a
# 然后 a = a + 1

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    first = 0
    second = 1
    third = 0
    def next_fib():
        nonlocal first, second, third
        result = first  # 0 --> 1 --> 1 --> 2
        third = first + second  # 1 --> 2 --> 3 -->5
        first = second  # 1 --> 1 --> 2 --> 3
        second = third  # 1 --> 2 --> 3 --> 5
        return result
    return next_fib

# 以上是我写的。我刚开始也只想设置两个变量，但是没想到两个变量怎么迭代，于是用了三个
# 参考别人的解法，其实两个变量就够了,别人的解法如下

def make_fib_other():
    """other's solution for make fibonacci numbers"""
    cur, next = 0, 1
    def fib():
        nonlocal cur, next
        result = cur
        cur, next = next, cur + next
        # 我写的third其实就是把cur和next用另一个名称代替了，然后再传递给second
        return result
    return fib


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while i < len(lst):
        if lst[i] == entry:
            lst.insert(i+1, elem)
            i += 2
        else:
            i += 1
    return lst

# 以上是我的思路，我认为在找到一个一样的数字之后，无论插入的数值与寻找的数值是否一致
# 都可以跳过插入的数值，进行下一个数的判断，所以 i += 2
# 别人的解法是再加一个判断，则无需像我一样用else了

def insert_items_other(lst, entry, elem):
    """other's solutino for insert items"""
    i = 0
    while i < len(lst):
        if lst[i] == entry:
            lst.insert(i+1, elem)
            if entry == elem:
                i += 1
        i += 1
    return lst

