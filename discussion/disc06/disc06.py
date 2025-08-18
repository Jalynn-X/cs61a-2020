# discussion 06


def memory(n):
    """
    Write a function that takes in a number n and returns a one-argument function.
    The returned function takes in a function that is used to update n. 
    It should return the updated n.
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x- 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

#  >>> s1 = [1, 2, 3]
#  >>> s2 = s1
# display nothing
#  >>> s1 is s2
#  True
#  >>> s2.extend([5, 6])
# display nothing
#  >>> s1[4]
# 6
#  >>> s1.append([-1, 0, 1])
# display nothing
#  >>> s2[5]
# [-1, 0, 1]
#  >>> s3 = s2[:]
#  >>> s3.insert(3, s2.pop(3))
# display nothing
#  >>> len(s1)
# 5
#  >>> s1[4] is s3[6] 
# True #注意这里的list是一样的object
#  >>> s3[s2[4][1]]
# 1
#  >>> s1[:3] is s2[:3]
# False #注意这里相当于复制了？所以不一样？
#  >>> s1[:3] == s2[:3]
# True

# Fill in the lines below so that the variables in the global frame are bound to the
# values below. Note that the image does not contain a full environment diagram.
# You may only use brackets, commas, colons, p , and q in your answer.
def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])


p = [2, 3]
q = [4, [p]]
mystery(q, p)
# 没想出来，以下是我自己写的
# def mystery(p, q):
#     p[1].extend([2, 3]) #这里不应该直接把p表示成[2, 3]
#     q[1].append(q[1:])


# p = [2, 3]
# q = [4, [p]]
# mystery(q, q)


def group_by(s, fn):
    """
    Write a function that takes in a sequence s and a function fn and returns a dictionary.
    The values of the dictionary are lists of elements from s. 
    Each element e in a list should be constructed such that fn(e) is the same for all elements in that list. 
    The key for each value should be fn(e). 
    For each element e in s, check the value that calling fn(e) returns, 
    and add e to the corresponding group.
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for e in s:
        key = fn(e)
        if key in grouped.keys():
            grouped[key].append(e)
        else:
            grouped[key] = [e]
    return grouped


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    Make sure to modify the original list using list mutation techniques.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    count = 0
    for item in s:
        if item == x:
            count = count + 1
    for i in range(count):
        s.append(el)
# 或者复制一个s出来进行判断（避免新增的数值影响for循环），例如网上的解法：
# s1 = s[:]
# for y in s1:
#   if y == x:
#       s.append(el)


# What would Python display?
# >>> s = [[1, 2]]
# >>> i = iter(s)
# >>> j = iter(next(i))
# >>> next(j)
# 1
# >>> s.append(3)
# >>> next(i)
# 3  #注意不是[1, 2]，因为[1, 2]已经被用过了？
# >>> next(j)
# 2
# >>> next(i)
# StopIteration  #注意不是3


def filter(iterable, fn):
    """
    only yields elements of iterable for which fn returns True.
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for x in iterable:
        if fn(x) is True:
            yield x


def merge(a, b):
    """
    Write a generator function merge that takes in two infinite generators a and b 
    that are in increasing order without duplicates and returns a generator that
    has all the elements of both generators, in increasing order, without duplicates.
    >>> def sequence(start, step):
    ...     while True:
    ...             yield start
    ...             start += step
    ... 
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    cur_a = next(a)
    cur_b = next(b)
    while True:
        if cur_a < cur_b:
            yield cur_a
            cur_a = next(a)
        elif cur_b < cur_a:
            yield cur_b
            cur_b = next(b)
        elif cur_a == cur_b:
            yield cur_a
            cur_a = next(a)
            cur_b = next(b)

    # list_a = list(a)
    # list_b = list(b)
    # if list_a[0] < list_b[0]:
    #     yield list_a[0]
    #     yield merge(list_a[1:], list_b)
    # else:
    #     yield list_b[0]
    #     yield merge(list_a, list_b[1:])

    # for i in range(len(a)):
    #     if a[i] < b[1]:
    #         yield a[i]
    #         yield merge(a[1:], b)
    #     else:
    #         yield b[i]
    #         yield merge(a, b[])