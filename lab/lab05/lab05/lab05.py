def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    element_lists = []
    for i in range(len(s)):
        element_lists.append(sum([[x for x in s if s.index(x) == i], [y for y in t if t.index(y) == i]], []))
    return element_lists
# 如果用list comprehension，得到的结果也是list，所以为了把list都结合在一起，用了sum函数

# 写的好复杂，网上简洁的写法是
# return [[s[i], t[i]] for i in range(0, len(s)))]
# 这里要学习的是，list comprehension的语法可以使用 for i in range()
# list comprehension还可以同时复合两个list，而不是只能for x in list a 一个列表



from math import sqrt


def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    "*** YOUR CODE HERE ***"
    lat_diff_square = pow(get_lat(city_a) - get_lat(city_b), 2)
    lon_diff_square = pow(get_lon(city_a) - get_lon(city_b), 2)
    city_distance = sqrt(lat_diff_square + lon_diff_square)
    return city_distance


def closer_city(lat, lon, city_a, city_b):
    """
    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon). If the two cities are the same distance away
    from the coordinate, consider city_b to be the closer city.

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    compare_city = make_city('comparision', lat, lon)
    if distance(city_a, compare_city) < distance(city_b, compare_city):
        return get_name(city_a)
    else:
        return get_name(city_b)


def check_city_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    >>> change_abstraction(False)
    """


# Treat all the following code as being behind an abstraction layer, you shouldn't need to look at it!

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return {"name" : name, "lat" : lat, "lon" : lon}
    else:
        return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    def find_helper(t):
        if label(t) == 'berry':
            return 1
        else:
            if is_leaf(t) is True:
                return 0
            else:
                exist_berry = 0
                for index in range(0, len(branches(t))):
                    exist_berry += find_helper(branches(t)[index])
                return exist_berry
    exist = find_helper(t)
    if exist:
        return True
    else:
        return False

# 我写的代码很复杂，因为我把label和branch分开考虑了
# 对于branch的情况，还要考虑sub branch是leaf和branch如何循环 
# 网上的解答就很简洁，只用了for b in branch，用in判断是否存在，存在则return True
def berry_finder(t):
    if label(t) == 'berry':
        return True
    else:
        for b in branches(t):
            # return berry_finder(b) 注意这里不能直接return berry_finder(b)，否则导致循环不完整
            if berry_finder(b) is True:
                return True #只要有一个true，就不会执行return false了，确保进行所有循环
        return False #注意缩进，不能和if平级，否则对于所有的b，都会返回false


# 刚开始没想通过数值来标志是否存在berry。认为只要判断如果是leaf且不是berry就可以返回false
# 但是没有考虑到如果一个branch有两个leaves，其中第一个不是berry
# 那么在判断完第一个的情况后，就直接返回false了，根本不会继续判断第二个

# 以下为之前尝试的代码
# exist_berry = 0
# if label(t) == 'berry':
#     return True
# else:
#     if is_leaf(t):
#         exist_berry = 1 if label(t) == 'berry' else 0
#     else:
#         for index in range(len(branches(t))):
#             return berry_finder(branches(t)[index])
# return True if exist_berry == 1 else False


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        leaves_to_tree = [tree(x) for x in leaves]
        return tree(label(t), leaves_to_tree)
    else:
        sprouted = [sprout_leaves(x, leaves) for x in branches(t)]
        return tree(label(t), sprouted)


# Abstraction tests for sprout_leaves and berry_finder
def check_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    >>> change_abstraction(False)
    """


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    return [[x, fn(x)] for x in seq if fn(x) >= lower and fn(x) <= upper]
# 其实是可以表示为 lower <= fn(x) <= upper


def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"
    return sum([[x, deck[deck.index(x) + round(len(deck)/2)]] for x in deck 
                if deck.index(x) < len(deck)/2], [])


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t1) is True and is_leaf(t2) is True:
        new_label = label(t1) + label(t2)
        return tree(new_label)
    elif len(branches(t1)) == len(branches(t2)):
        new_label = label(t1) + label(t2)
        new_branch = []
        for node_t1, node_t2 in zip(branches(t1), branches(t2)):
            new_branch.append(add_trees(node_t1, node_t2))
        return tree(new_label, new_branch)
    elif len(branches(t1)) != len(branches(t2)):
        small_tree = t1 if len(branches(t1)) < len(branches(t2)) else t2
        big_tree = t1 if len(branches(t1)) > len(branches(t2)) else t2
        if len(branches(small_tree)) == 0:
            return tree(label(small_tree) + label(big_tree), branches(big_tree))
        else:
            add_part = add_trees(small_tree, tree(label(big_tree), branches(big_tree)[:len(branches(small_tree))]))
            new_branch = branches(add_part) + branches(big_tree)[len(branches(small_tree)):]
            new_tree = tree(label(add_part), new_branch)
            return new_tree

# 看了网上的解法，很简洁。不进行过多的分类讨论，只针对两个tree的长度是否相等
# # 网上解法：
#     if not t1:
#         return t2
#     if not t2:
#         return t1
#     new_label = label(t1) + label(t2)
#     t1_children, t2_children = branches(t1), branches(t2)
#     length_t1, length_t2 = len(t1_children), len(t2_children)
#     if length_t1 < length_t2:
#         t1_children += [None for _ in range(length_t1, length_t2)]
#     elif len(t1_children) > len(t2_children):
#         t2_children += [None for _ in range(length_t2, length_t1)]
#     return tree(new_label, [add_trees(child1, child2) for child1, child2 in zip(t1_children, t2_children)])

# 尝试自己写一下，但是还是有点理解不了
# 如果相等，则相加；不相等，把较小的那一个tree长度补齐，全用空值补齐，然后相加
# new_label = label(t1) + label(t2)
# if len(branches(t1)) > len(branches(t2)):
#     t1_branches= branches(t1) + [None for _ in range(branches(t1), branches(t2))]
#     t1 = tree(label(t1), t1_branches)
#     # return add_trees(new_label, add_trees(branches(t1), branches(t2))) #这行其实不需要写，统一放在后面
# elif len(branches(t1)) < len(branches(t2)):
#     t2_branches= branches(t2) + [None for _ in range(branches(t2), branches(t1))]
#     t2 = tree(label(t2), t2_branches)
# return tree(new_label, [add_trees(t1_child, t2_child) for t1_child, t2_child in zip(branches(t1), branches(t2))])


# 绞尽脑汁终于做出来了。花了好长时间，而且代码真的很丑....以下全都是过程
# new_label = label(t1) + label(t2)
# bigger_branch = branches(t1) if len(branches(t1)) > len(branches(t2)) else branches(t2)
# smaller_branch = branches(t1) if len(branches(t1)) < len(branches(t2)) else branches(t2)
# if len(smaller_branch) == 0:
#     return tree(new_label, bigger_branch)
# else:
    
#     new_branch = add_trees(smaller_branch, bigger_branch[:len(smaller_branch)]) + bigger_branch[len(smaller_branch):]
#     return tree(new_label, tree(new_branch))


# new_branch.append(tree(label(node_t1)+ label(node_t2), 
#                               [add_trees(branches(node_t1), branches(node_t2))])
# elif is_leaf(t1) or is_leaf(t2):
#     new_branch = branches(t1) if len(branches(t2)) == 0 else branches(t2)
#     return tree(label(t1) + label(t2), )
    # if len(t1) == 0 and len(t2) == 0:
    #     return t1 + t2


# zip function takes in a serie of arguments that can be iterated.
# The items in these arguments are paked as tupes(元组)
# the function then return a list consisted of these tupes
# if the lengths of the arguments are not identical, the shortest length would be returned
# >>> name = ['jack', 'pic', 'how' ]
# >>> age = ['20', '30', '40']
# >>> for n, a in zip(name, age):
# ...     print(n, a)
# >>> 
# jack 20
# pic 30
# how 40


def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            "*** YOUR CODE HERE ***"
            table[prev] = [word]
            "*** YOUR CODE HERE ***"
        else:
            table[prev] = table[prev] + [word]
        prev = word
    return table
# 不确定这里的your code here是不是只能填一行代码

# 看了网上的解法，的确是只能填一行代码
# if prev not in table:
#     table[prev] = [] #这一步有点像在模拟之前的结果，如果之前没有prev，那么table中这个键的值也就是空
# table[prev] += [word] #相当于把word存在列表里
# prev = word


def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
        result = result + ' ' + word
        word = random.choice(table[word])
    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open(path, encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
# tokens = shakespeare_tokens()
# table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)



# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
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

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


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

