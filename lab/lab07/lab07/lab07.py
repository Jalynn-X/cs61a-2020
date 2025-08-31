def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    yield from map(lambda x: x*multiplier, it)

# 没想到怎么写，参考网上用了map
# 注意不能直接写map(x*multiplier, it)，不知道x是什么
# 也不能直接写map(it*multiplier, it)。所以要结合lambda
# for i in (yield from it):
#     yield from i * multiplier


    
# def scale_helper(it):
#     result = []
#     iter_it = iter(it)
#     cur_it = None
# while True:
#     if type(cur_it) != str:
#         cur_it = next(iter_it)
#         if type(cur_it) == str:
#             break
#         result.append(cur_it)
#     else:
#         break
# yield from result

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    if n != 1:
        yield int(n)
        if n % 2 == 0:
            yield from hailstone(n/2)
        elif n % 2 != 0:
            yield from hailstone(n * 3 + 1)
    else:
        yield int(n)

# 上面是参考了网上解法写的。下面是自己写的，没有使用yield from
# while n != 1: 
#     yield int(n)
#     if  n > 0 and n % 2 == 0:
#         n = n / 2
#     elif n > 0 and n % 2 != 0:
#         n = n * 3 + 1
# yield int(n)