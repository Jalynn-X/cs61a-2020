def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    if k > 0:
        while k >= 1: 
            result = result * n
            n = n - 1
            k = k - 1
        return result
    elif k == 0:
        return 1
# 以上我写的代码中有三处可以优化的地方
# 1）在最开始定义了result=1，则无需考虑elif条件，默认K=0的时候，直接返回最开始定义的result
# 2）无需考虑elif的情况下，无需使用if语句，直接使用while即可
# 3）对于多个值，可以使用逗号分隔，例如：result, n = result * n, n - 1

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    t = 1
    k = y // 10
    smd = y % 10
    while k >= 1:
        smd = smd + (y % pow(10, t+1)) // pow(10, t)
        t = t + 1
        k = y // pow(10, t)
    return smd
# 以上我写的代码中有三处可以优化的地方
# 1）参数过多，可以简化：首先对于 y，不需要一直使用%取余再取整商，而是可以使用 y = y // 10 替代
# 2）当 y 可以随着条件更新数值时，不需要用 t 进行指数计算，也不需要用 k 进行替代，直接使用 y 即可
# 3）while y > 0 :
#       sum, y = sum + y % 10 （这里就可以直接计算出余数）, y // 10
#   return sum

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n > 10:
        if n % 10 == 8 and (n // 10) % 10 == 8:
            count = count + 1
        n = n // 10
    if count >= 1:
        return True
    else:
        return False


# 以下是我刚开始写的代码，存在的问题主要在于in a row的理解
# 我理解成了一行里面有两个8，按照doctest中880088可以用过的案例来说，这样理解是错的
# in a row表示连续的，所以只要考虑两个8相邻的情况即可
#    num = n % 10
#    count = 0
#    while n > 10:
#        if num == 8:
#            count = count + 1
#            n = n // 10
#        num = n % 10
#    if count == 2:
#        return True
#    else:
#        return False
    
# 学习如下代码得到的体会：
#    while n > 0:
#        if n%10 == 8 and (n//10)%10 == 8:
#            return True
#        n = n//10
#    return Fals
# 1）当 if 碰到 return 之后，就终止运行了，所以之后的都不会执行
# 2）没有执行return时，才会继续执行下一步，当 n 的值得到更新，while就会继续循环，直至 n 不满足大于0的条件
# 3）当执行完循环后仍然不满足条件时，循环终止，执行 return False（所以缩进和while平级）
# 4）我以为return false仍然需要通过if和else进行，但是中间插入n = n // 10后，if结构被打乱，就卡住不知道如何下手了
# 5）我以为return false仍然需要通过条件判断，但是又写不出不满足以上所有的if条件，没有想到直接在最后return false就表示不满足while中所有条件了