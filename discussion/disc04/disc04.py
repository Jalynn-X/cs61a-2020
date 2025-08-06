# discussion 04

#  01  count_stair_ways

def count_stair_ways(n):
    """
    calculate how many different ways to go up a fight of stairs that has n steps.
    You can either take 1 or 2 steps each time. Assume n is positive.
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        with_one_step = count_stair_ways(n - 1)
        with_two_step = count_stair_ways(n - 2)
        return with_one_step + with_two_step

# 下面这个是我最开始写的，错误在于不能每次都加1
# 想象一下，如果每次都只走1步，也只是1种方法，但按我原来的代码，却加出来3次
# def count_stair_ways_my(n):
#     """
#     calculate how many different ways to go up a fight of stairs that has n steps.
#     You can either take 1 or 2 steps each time. Assume n is positive.
#     """
#     if n <= 0:
#         return 0
#     else:
#         with_one_step = count_stair_ways_my(n - 1) + 1
#         with_two_step = count_stair_ways_my(n - 2) + 1
#         return with_one_step + with_two_step
# 网上有一个方法把base situation写成如下，我觉得也蛮合理的
# if n <= 2:
#   return n (此时有1、2两种步长选择)

# def count_k(n, k):
#     """
#     a special version of the count_stairways problem.
#     we are able to take up to and including k steps at a time.
#     Write a function count_k that figures out the number of paths. 
#     Assume n and k are positive.
#     >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
#     4
#     >>> count_k(4, 4)
#     8
#     >>> count_k(10, 3)
#     274
#     >>> count_k(300, 1) # Only one step at a time
#     1
#     """
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     else:
#         ways = 0
#         for i in range(1, k + 1):
#             ways = ways + count_k(n - i, k)
#         return ways
# 对于n==0而言，意味着n-i=0，当i=k的时候，也就是count_k(n-k,k)

# m = k
# if n - 1 < 1:
#     return count_k(n, 1) + count_k(n-1, k)

# #     return count_k(n, k, k)

#     # if n < 0:
#     #     return 0
#     # if n == 0:
#     #     return 1
#     # elif k == 0:
#     #     return 0
#     # elif k != 1:
#     #     return count_k(n - k, k) + count_k(n, k - 1)
#     # else:

def count_k(n, k):
    """
    a special version of the count_stairways problem.
    we are able to take up to and including k steps at a time.
    Write a function count_k that figures out the number of paths. 
    Assume n and k are positive.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total, i = 0, 1
        while i <= k:
            total = total + count_k(n - i, k)
            i += 1
        return total
# hint video https://www.bilibili.com/video/BV138411F7vT?p=85&vd_source=97f34f56a505e26f93241ece11301b8b
# after taking one step in allowed range, which is from 1 up to k, the next choice will be the same
# so, (n - i) represent the remaining steps needed to be taken, and the recursive function ensure that
# the next step will still be in this range, until n is 0 or below 0


# lists
def even_weighted(s):
    """
    takes a list s and returns a new list
    that keeps only the even-indexed elements of s 
    and multiplies them by their corresponding index.
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [item * s.index(item) for item in s if s.index(item) % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))


# else:
#     for x in s:
#         b = x * max_product(s[s.index(x)+1:])
#     a.append(b)
#     return max(a)
# 然后我就卡了，被for和return绕晕了
# 参考了网上别人的解法，不得不说真的很优雅！ 其实无需用for，也就不需要用index(x)+1来作为新的index
# 对于当前index=0的数据来说，需要乘以至少index-2以后最大的max_product，才有可能组合为最大的数据
# 和他形成对比的就是它的下一位数字可能形成的max_product，通过s[0]的不断变化并与recursion相结合，找到所有解的集合
# def max_product(s):
#     if len(s) == 0:
#         return 1
#     return max(s[0] * max_product(s[2:]), max_product(s[1:]))
