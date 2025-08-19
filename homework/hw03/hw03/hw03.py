HW_SOURCE_FILE=__file__


def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]


def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'


def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]


def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]


def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]


def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'


def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]


def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


def planet(size):
    """Construct a planet of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ['planet', size]


def size(w):
    """Select the size of a planet."""
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]


def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'


def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                              arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'total_weight', ['Index'])
    True
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"
    left_end = end(left(m))
    right_end = end(right(m))
    if is_mobile(left_end) and balanced(left_end) is False:
        return False
    elif is_mobile(right_end) and balanced(right_end) is False:
        return False
    else:
        left_torque = length(left(m)) * total_weight(left_end)
        right_torque = length(right(m)) * total_weight(right_end)
        if left_torque == right_torque:
            return True
        return False


def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'totals_tree', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return tree(total_weight(m))
    elif is_mobile(m):
        mobile_branches = []
        for mobile_end in (end(left(m)), end(right(m))):
            new_branch = totals_tree(mobile_end)
            mobile_branches.append(new_branch)
        return tree(total_weight(m), mobile_branches)
# 这里我用了for循环，但是其实只有两个数值，所以不用循环直接表示也可以
# 网上看到其他人的答案是：
# return tree(total_weight(b), [totals_tree(end(left(m))), totals_tree(end(right(m)))])

def replace_leaf(t, find_value, replace_value):
    """Returns a new tree where every leaf value equal to find_value has
    been replaced with replace_value.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t) is True:
        if label(t) == find_value:
            new_label = replace_value
        else:
            new_label = label(t)
        return tree(new_label)
    else:
        new_branches = []
        for b in branches(t):
            new_b = replace_leaf(b, find_value, replace_value)
            new_branches.append(new_b)
        return tree(label(t), new_branches)        
# 网上有人的写法很简洁
# if is_leaf(t):
#   return tree(replace_value) if label(t) == find_value else tree(label(t))
# return tree(label(t), [replace_leaf(b, find_value, replace_value) for b in branches(t))])

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    print_list = []
    if is_leaf(t):
        print_list.append(label(t))
        return print_list
    else:
        print_list.append(label(t))
        for branch in branches(t):
            branch_list = preorder(branch)  
            print_list = print_list + branch_list  # 这里可以表示为 print_list += preoder(branch)
        return print_list


def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    if len(word) == 1:
        return True if label(t) == word else False  # 这里可以直接写成 return label(t) == word
    else:
        if label(t) == word[0]:
            for b in branches(t):
                if has_path(b, word[1:]):
                    return True
        else:
            return False
# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False,则返回 False
# 如果有一个为 True,则返回 True。可迭代对象可以是列表、元组、集合、字典、字符串等。
# 网上有一种简洁的写法是：
# if len(word) == 1:
#     return label(t) == word
# return any([has_path(b, word[1:]) for b in branches(t)])
# any的用法使得代码很简洁，不过是不是漏掉了判断第一个字母的情况




# if label(t) == word:
#     if len(word) == 1:
#         return True
#     else:
#         next_word = word[1:]
#         for b in branches(t):
#             branch_path = has_path(b, next_word)
#             if branch_path is True:
#                 return True
# else:
#     return False


def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]


def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]


def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]


def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))


def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)


def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    min_num = min(p1, p2, p3, p4)
    max_num = max(p1, p2, p3, p4)
    return interval(min_num, max_num)

# p1 = x[0] * y[0]
# p2 = x[0] * y[1]
# p3 = x[1] * y[0]
# p4 = x[1] * y[1]
# return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]


def sub_interval(x, y):
    """Return the interval that contains 'the difference between any value in x
    and any value in y.'"""
    "*** YOUR CODE HERE ***"
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)
# 可以通过add_interval实现
# 网上的一种解法：
# return add_interval(x, interval(-upper_bound(y), -lower_bound(y)))


def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert lower_bound(y) * upper_bound(y) > 0, "interval should not span zero"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)


def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))


def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(-2, -1)  # Replace this line!
    r2 = interval(3, 4)  # Replace this line!
    return r1, r2


def multiple_references_explanation():
    return """par2 is better. par1 would enlarge the interval by using
    mul_interval function and therefore return an interval larger that
     that returned by par2"""
# She is right, because in par1, each interval is referenced twice, so that the interval will be looser
# since the it choose different values for each instance of the interval. 
# In par2, each interval is referenced only once, so the interval will be tighter.

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def f(t):
        return a*t*t + b*t + c
    upper = upper_bound(x)
    lower = lower_bound(x)
    supreme = -b/(2*a)
    if a < 0:
        if lower <= supreme <= upper:
            max_value = f(supreme)
            min_value = min(f(upper), f(lower))
            return interval(min_value, max_value)
    elif a > 0:
        if lower <= supreme <= upper:
            min_value = f(supreme)
            max_value = max(f(upper), f(lower))
            return interval(min_value, max_value)
    max_value = max(f(upper), f(lower))
    min_value = min(f(upper), f(lower))
    return interval(min_value, max_value)

# 实际上不需要区分a的正负号，直接通过min 、max判断即可
# if lower <= supreme <= upper:
#     return interval(min(f(upper), f(lower), f(supreme)), max(f(upper), f(lower), f(supreme)))
# else:
#     return interval(min(f(upper), f(lower)), max(f(upper), f(lower)))


# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

