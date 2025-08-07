HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        if x == 8:
            return 1
        else:
            return 0
    else:
        if x % 10 == 8:
            return num_eights(x // 10) + 1
        else:
            return num_eights(x // 10)
# else条件可以简化为return num_eights(x // 10) + num_eights(x % 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        def direction(n):
            """
            if n is a multiple of 8 or contains the digit 8,
            the direction switches
            """
            if n == 1:
                return 1
            else:
                if n % 8 == 0 or num_eights(n) != 0:
                    return -1 * direction(n - 1)
                else:
                    return direction(n - 1)
        return pingpong(n - 1) + direction(n - 1)


# 刚开始想通过if实现，发现可以简化
#        if direction(n - 1) == 1:
#            return pingpong(n - 1) + 1
#        elif direction(n -) == -1:
#            return pingpong(n - 1) - 1
# 刚开始把direction单独定义成为一个函数，后尝试合并，以下为原始代码：
# def direction(n):
#     """
#     if n is a multiple of 8 or contains the digit 8,
#     the direction switches
#     """
#     if n == 1:
#         return 1
#     else:
#         if n % 8 == 0 or num_eights(n) != 0:
#             return -1 * direction(n - 1)
#         else:
#             return direction(n - 1)


# 还看到一种解决方法：
# def pingpong(n):
#   def helper(index, pp_value, direc):
#       if index == n:
#           return pp_value --这里就是break跳出条件了，index从1开始累加，然后算到n，跳出
#       else:
#           if index % 8 == 0 and num_eights(index) != 0:
#               return helper(index + 1, pp_value - direc, -direc)
#           else:
#               return helper(index + 1, pp_value + direc, direc)
#   return helper(1, 1, 1) -- 通过return传入helper的初始值    


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        if ((n // 10) % 10) == (n % 10):
            return missing_digits(n // 10) + 0
        else:
            return missing_digits(n // 10) + abs(((n // 10) % 10) - (n % 10) + 1)


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    def count(total, coin=1):
        if total == coin:
            return 1
        elif total < 0 or coin is None:
            return 0
        else:
            #注意这里相减代表着如果结果是0，则说明满足第一个if条件，增加 1种方法
            with_cur_coin = count(total - coin, coin)
            without_cur_coin = count(total, next_largest_coin(coin))
            return with_cur_coin + without_cur_coin
    return count(total)
# count(100, 25) --> count(75, 25) + count(100, None) --> count(50, 25) + count(75, None) --> count(25, 25) + count(50, None)
# count(25, 25) --> return 1 --说明100全部使用25仅有1种方法

# 下面这些是我自己尝试写的
# 注意这个题目和课堂上提到的count_partition不太一样，完全模仿课堂是写不出来的
# 课堂上是逐次递减，这里是逐次递增（如果不用目前的硬币，需要使用下一个更大的硬币）
    #     if next_largest_coin(coin) is None:
    #         return count(total - coin, 1) + count(coin, 1)
    #     else:
    #         if total < 1:
    #             return 0
    #         elif total <= next_largest_coin(coin):
    #             return 1
    #         else:
    #             count_bigger = count(total - next_largest_coin(coin), next_largest_coin(coin))
    #             # sing at least one next_largest_coin
    #             count_smaller = count(total, coin)
    #             # using no next_largest_coin
    #             return count_bigger + count_smaller
    # return count(total)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda n: f(f, n))(lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1))))
# https://stackoverflow.com/questions/34198346/what-is-the-explanation-of-the-python-code-which-uses-anonymous-lambda-to-implem
# https://blog.csdn.net/wnw231423/article/details/131556836
# https://blog.csdn.net/qq_42103298/article/details/123773235?spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-123773235-blog-131556836.235%5Ev43%5Epc_blog_bottom_relevance_base2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-123773235-blog-131556836.235%5Ev43%5Epc_blog_bottom_relevance_base2&utm_relevant_index=12

# f = lambda x: x * f(x-1)
# lambda f: lambda x: 1 if x ==1 else x * f(x, x - 1)
# f(x)相当于x*f(x, f(x-1))，f(x, f(x-1))就相当于(x-1)*f(x-1, f(x-2)), 即f(x-n+1, f(x-n+1,f(x-n))，当 x-n = 1 时，值为1，再重新往回递归
# 由于题目要求调用的时候只传入x，所以在(lambda f: lambda x: 1 if x ==1 else x * f(x, f(x-1)))之后要传入f，f也就是f(x, f(x-1))

# https://www.bilibili.com/video/BV1s3411G7yM?p=31&spm_id_from=pageDriver&vd_source=97f34f56a505e26f93241ece11301b8b
# 视频Q&A解释如下：
# 1、要替代fact = lambda n: 1 if n == 1 else n * fact(n-1)，将fact当作一个argument传入lambda
#   因此可以得到lambda n, fact = 1 if n == 1 else n * fact((n - 1)， fact)
# 2、由于只能传入n一个参数，那么要把lambda构造成关于n的功能，即 lambda n: (lambda fact: fact(n, fact))
#   此时n 传入lambda之后，返回的是fact(n, fact)，而fact是之后传入的lambda n, fact = 1 if n == 1 else n * fact((n - 1)， fact)
