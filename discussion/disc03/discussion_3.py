# discussion 3


def multiply(m, n):
    """
    Write a function that takes two numbers m and n and returns their product.
    Assume m and n are positive integers.
    >>> multiply(5, 3)
    15
    """
    if m == 0 or n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)
# 题目里建议思考(m, n-1)和(n, m-1)的区别。我刚开始没看出来。
# 在网上看到有如下解法，相比之下如果n比m大很多这个方法可以节省一定的计算时长
#   if n > m:
#       m, n = n, m
#   if n == 0:
#       return 0


# 注意这里如果需要统计步长，在网上看到的解法是需要引入另一个变量
#  def hailstone(n):
#     if n == 1:
#         print(n)
#     else:
#         if n % 2 == 0:
#             print(n)
#             return hailstone(n / 2)
#         else:
#             print(n)
#             return hailstone(3 * n + 1)
# 没想出来怎么用recursion统计步长)))


def hailstone(n, count=0):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>>a
    7
    """
    if n == 1:
        print(n)
        count += 1
        return count
    else:
        if n % 2 == 0:
            print(n)
            count += 1
            return hailstone(n / 2, count)
        else:
            print(n)
            count += 1
            return hailstone(3 * n + 1, count)


def split(n):
    return n // 10, n % 10


def merge(n1, n2):
    """ Merges two numbers with digits in decreasing order and returns 
    a single number with all of the digits of the two, in decreasing order. 
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        all_but_last_1, last_1 = split(n1)
        all_but_last_2, last_2 = split(n2)
        if last_1 >= last_2:
            return int(str(merge(n1, all_but_last_2)) + str(last_2))
        else:
            return int(str(merge(all_but_last_1, n2)) + str(last_1))



def make_func_repeater(f, x):
    """
    Define a function that takes in a one-argument function f and an integer x.
    The function returns another function that takes another integer argument.
    Returns the result of applying f to x this number of times.
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(a):
        if a == 1:
            return f(x)
        else:
            return f(repeat(a - 1))
    return repeat
# 妙啊！！！我没想到把repeat放在f里面
# 还以为要return make_func_repeater(f, f(x))， 然后返回repeat(a - 1)，结果报错显示 a 没有定义


def is_prime(n):
    """
    returns True if positive integer n is a prime number and False otherwise
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(k):
        if n == k:
            return True
        elif n == 1 or n % k == 0:
            return False
        else:
            return prime_helper(k + 1)
    return prime_helper(2)
# 虽然想到了要从2开始讨论，以及要设置上限为n，但是没有想到可以通过n == k来设置循环跳出
# 这段逻辑的意义在于：当从2 直到 n - 1，若有碰到一个数值使得 n 被它整除，那么就不是质数，直接return False跳出。
# 相反，如果之间没有任何一个数满足条件，则 n 一直到碰到它自身才可以实现整除，所以说明只有1和本身两个因数，即是质数，然后跳出循环