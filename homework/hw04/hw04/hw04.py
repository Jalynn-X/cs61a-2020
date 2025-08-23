def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message == 'deposit':
            balance = balance + amount
            return balance
        elif message == 'withdraw':
            if balance < amount:
                return 'Insufficient funds'
            else:
                balance = balance - amount
                return balance
        else:
            return 'Invalid message'
    return bank


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    wrong_pass = []
    def withdraw_protect(amount, input_password):
        nonlocal balance  # 这里不加wrong_pass也可以，是不是因为list本身就是mutable的？
        if len(wrong_pass) < 3:
            if input_password != password:
                if input_password not in wrong_pass: 
                    wrong_pass.append(input_password)
                return 'Incorrect password'
                # 这里我本来是只要密码错误就append，没有考虑错误密码之前是否出现的，但是后面的make_joint测试中
                # make_joint(w, 'my', 'secret')、w(25, 'secret')都返回'Incorrect password'，说明有判断
                # 所以就返回来修改了这里的代码，增加了一处判断
            else:
                if balance >= amount:
                    balance = balance - amount
                    return balance
                else:
                    return 'Insufficient funds'
        else:
            return "Frozen account. Attempts: " + str(wrong_pass)
    return withdraw_protect


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    cur_num = next(t)
    next_num = next(t)
    count = 1
    while count < k:
        if cur_num == next_num:
            count += 1
            if count == k: # 我这里如果不增加这个if条件的话，就会导致如果列表最后一个满足，仍然执行next，导致stop
                return cur_num
        elif cur_num != next_num:
            count = 1
        cur_num = next_num
        next_num = next(t)
    return cur_num

# 网上有另一种方法可以避免next(t)超出范围导致stop报错，即避免两个next同时使用
# last_unm = None
# count = 1
# while True:
#     item = next(t)
#     if last_unm == item:
#         count = count + 1
#     else:
#         last_unm = item # 这里无需再重复item = next(t)，因为会回到循环开头执行next(t)
#         count = 1
#     if count == k:
#         return item

def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    num = len(seq)
    if num == 1:
        yield [seq[0]]
    else:
        for i in range(num):
            for item in permutations(seq[:i]+seq[i+1:]):
                yield [seq[i]] + item

# 这里我其实是构建了一个辅助的循环函数，但是其实可以直接用generator循环
# def helper(seq):
#     num = len(seq)
#     if num == 1:
#         return [seq]
#     else:
#         all_results = []
#         for i in range(num):
#             results = helper(seq[:i] + seq[i+1:])
#             for result in results:
#                 sub_result = [seq[i]] + result
#                 all_results.append(sub_result)
#         return all_results
# list_seq = list(seq)
# permutations_result = helper(list_seq)
# yield from permutations_result


def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    if type(withdraw(0, old_pass)) == str:
        return withdraw(0, old_pass)
    else:
        correct_password = [old_pass, new_pass]
        def withdraw_2pass(amount, password):
            if password in correct_password:
                return withdraw(amount, old_pass)
            return withdraw(amount, password)
        return withdraw_2pass


def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def sub_generators(m, remainder):
        n = naturals()
        next_n = next(n)
        while True:
            if next_n % m == remainder:
                yield next_n
            next_n = next(n)
    for remainder in range(m):
        yield sub_generators(m, remainder)
        
# while true也可以用for代替。网上的解法：
# def gen(i):
#   for e in naturals():
#       if e % m == i:
#           yield e
# for i in range(m):
#   yield gen(i)

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

