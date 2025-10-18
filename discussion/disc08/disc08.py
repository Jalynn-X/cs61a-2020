class A():
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2

class B():
    def __init__(self):
        print("boo!")
        self.a = []
    
    def add_a(self, a):
        self.a.append(a)
    
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret
    

# 01
# >>> A("one")
# one 
# >>> print(A("one"))
# oneone
# >>> repr(A("two"))
# 'two'
# >>> b = B()
# boo!
# >>> b.add_a(A("a"))  
# >>> b.add_a(A("b"))  
# >>> b
# 2
# aabb  # 注意这里括号里是A class的instance，所以调用A的str


# 02 Linked Lists

# 2.2
def multiply_lnks(lst_of_lnks):
    """
    a function that takes in a Python list of linked lists and multiplies them element-wise. 
    It should return a new linked list. If not all of the Link objects are of equal length, 
    return a linked list whose length is that of the shortest linked list given.
    You may assume the Link objects are shallow linked lists, 
    and that lst of lnks contains at least one linked list.
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    label = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty  # 只要有一个为空，所有的都为空
        label = label * link.first
    return Link(label, multiply_lnks([b.rest for b in lst_of_lnks]))


    # 上面是网上别人的解法
    # 下面是我自己写的，没有完全参考要求的格式
    # label = 1
    # for link in lst_of_lnks:
    #     label = label * link.first
    # if any(link.rest is Link.empty for link in lst_of_lnks):
    #     return Link(label)
    # else:
    #     new_lst = [l.rest for l in lst_of_lnks]
    #     return Link(label, multiply_lnks(new_lst))
#


# 2.4
# using a while loop
def filter_link(link, f):
    """
    Implement filter link, which takes in a linked list link and a function f
    and returns a generator which yields the values of link for which f returns True.
    Try to implement this both using a while loop and without using any form of iteration.
    # >>> next(g)
    # StopIteration
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest


# without using any form of iteration
def filter_link_without(link, f):
    """implement filter_link  without using any form of iteration."""
    if link is not Link.empty:
        if f(link.first) is True:
            yield link.first
        link = link.rest
        yield from filter_link(link, f)


# 03 Questions
# 3.1
def make_even(t):
    """
    Define a function make_even which takes in a tree t whose values are integers, 
    and mutates the tree such that all the odd integers are increased by 1
    and all the even integers remain the same.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 != 0:
        t.label += 1
    if t.is_leaf() is False:
        for b in t.branches:
            make_even(b)


# 3.2
# Define a function square tree(t) that squares every value in the non-empty tree t.
# You can assume that every value is a number.
def square_tree(t):
    """
    Mutates a Tree t by squaring all its elements.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t)
    >>> t
    Tree(1, [Tree(4, [Tree(9)]), Tree(16), Tree(25)])
    """
    t.label = pow(t.label, 2)
    if t.is_leaf() is False:
        for b in t.branches:
            square_tree(b)


# 3.5
def alt_tree_map(t, map_fn):
    """
    Implement the alt_tree_map function that, given a function and a Tree, applies the
    function to all of the data at every other level of the tree, starting at the root.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x:-x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    def helper(t, map_fn, apply):
        if apply is True:
            t.label = map_fn(t.label)
            for b in t.branches:
                helper(b, map_fn, False)
        else:
            for b in t.branches:
                helper(b, map_fn, True)
        return t
    return helper(t, map_fn, True)



# --------------------------
class Link:
    """ Alinked list is either an empty linked list, 
    or a Link object containing a first value and the rest of the linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()