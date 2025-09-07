def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    # # recursive
    # if link is Link.empty: #注意这里不能写成link.empty，会报错没有这个属性
    #     return []
    # else:
    #     result = [link.first]
    #     return result + convert_link(link.rest)
    
    # iterative
    result = []
    while link is not Link.empty:
        result.append(link.first)
        link = link.rest
    return result


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    count_index = 1
    new_s = Link(s.first)
    w = s.rest
    if w is Link.empty:
        s.first = new_s.first
        s.rest = new_s.rest
    else:
        while w is not Link.empty:
            if count_index % 2 != 0:
                w = w.rest
            if count_index % 2 == 0:
                new_s.rest = Link(w.first)
                p = Link(new_s)  # 如果直接写new_s.first = new_s会循环报错
                new_s = p
                w = w.rest
            count_index += 1
        s.first = new_s.first.first
        s.rest = new_s.first.rest

# 每count一次，多一个.rest
# s.rest = 
# s.rest.rest = 
# s.rest.rest.rest =
# 而且居然不能直接assign，例如直接用a = new_s.first无法改变s，s的first和rest要分开assign
            
# 我好像把问题复杂化了，问题的关键应该是通过s.rest = s.rest.rest进行迭代
def every_other(s):
    if s is Link.empty or s.rest is Link.empty:
        return
    else:
        s.rest = s.rest.rest  # 这一步是通过迭代删除
        every_other(s.rest)  # 循环，实际上是对原来s.rest.rest进行处理

def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    def helper(t):
        if t.is_leaf():
            return t.label
        else:
            result = t.label
            for b in t.branches:
                result = result * helper(b)
            return result
    t.label = helper(t)
    for b in t.branches:
        b = cumulative_mul(b)


def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    all_links = [link]
    sub_link = link.rest
    while sub_link is not Link.empty:
        if sub_link not in all_links:
            all_links.append(sub_link)
            sub_link = sub_link.rest
        else:
            return True
    return False

    # 注意link is not iterable
    # for sublink in link.rest:
    #     if sublink in all_links:
    #         return True
    #     all_links.append(sublink)
    # return False

def count_call(f):
    def call_helper(*args):
        count_call.call += 1
        return f(*args)
    count_call.call = 0
    return call_helper


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if link is Link.emtpy:
        return False
    else:
        fast, slow = link.rest, link
        while fast is not Link.empty:
            if fast.rest is Link.empty:
                return False
            elif fast is slow or fast.rest is slow:
                return True
            else:
                fast = fast.rest.rest
                slow = slow.rest
        return False
    # 这个没想出来
    # """ use a slow pointer and a fast pointer. 
    # The slow pointer moves one step for each round,
    # while the fast pointer moves two steps a round,
    # if the fast pointer catch the slow pointer, the cycle exists. """



# def reverse_other(t):
#     """Mutates the tree such that nodes on every other (odd-depth) level
#     have the labels of their branches all reversed.

#     >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
#     >>> reverse_other(t)
#     >>> t
#     Tree(1, [Tree(4), Tree(3), Tree(2)])
#     >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
#     >>> reverse_other(t)
#     >>> t
#     Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
#     >>> t = Tree(1, [Tree(8, [Tree(3), Tree(6, [Tree(7), Tree(8)])]), Tree(2)])
#     >>> reverse_other(t)
#     >>> t
#     Tree(1, [Tree(8, [Tree(3), Tree(6, [Tree(8), Tree(7)])]), Tree(2)])
#     """
#     "*** YOUR CODE HERE ***"
#     # def helper(t, need_reverse):
#     #     if t.is_leaf():
#     #         t = t
#     #     else:
#     #         if need_reverse:
#     #             old_label = [b.label for b in t.branches]
#     #             new_label = old_label[::-1]
#     #             for i in range(len(old_label)):
#     #                 t.branches[i].label = new_label[i]
#     #         for b in t.branches:
#     #             helper(b, not need_reverse)
#     # helper(t, True)

def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7), Tree(8)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(8), Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def helper(t, need_reverse):
        if t.is_leaf():
            t = t
        else:
            if need_reverse:
                old_label = [b.label for b in t.branches]
                new_label = old_label[::-1]
                for i in range(len(old_label)):
                    t.branches[i].label = new_label[i]
            for b in t.branches:
                helper(b, not need_reverse)
    helper(t, True)
# 参考网上的思路，一个是设置True/False标志，这样就能保证同一个层级的是同一个标志
# 还有一种解决方法也类似使用depth奇偶数判断，但是要确保使用同一个depth
    # def helper(t, cur_level):
    #     if t.is_leaf():
    #         return
    #     if cur_level % 2 == 0:
    #         label_list = []
    #         for b in t.branches:
    #             label_list.append(b.label)
    #         label_list.reverse()
    #         for i in range(len(t.branches)):
    #             t.branches[i].label = label_list[i]
    #     for b in t.branches:  # 这里确保使用同一个cur_level
    #         helper(b, cur_level + 1)

    # return helper(t, 0)




# 下面是我自己写的，试图通过nonlocal追踪depth是否为奇数。
# 虽然对于课程提供的测试案例都可以通过，但是测试案例并不完善，没有测出来这个代码的不足
# 对于depth，每调用一次helper，增加一次。那么对于平级的node，因为都要调用，会导致本来应该一致的depth，还是会逐渐增加
# 例如下面的，本来5、4和7、8都是平级的，depth = 3，但是由于调用次数的增加，导致他们的depth不同，因此5、4调换了，但是7、8没有调换
# def reverse_other(t):
    # >>> t = Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7), Tree(8)])]), Tree(2)])
    # >>> reverse_other(t)
    # >>> t
    # Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(8), Tree(7)])]), Tree(2)])
    # depth = 0
    # def helper(t):
    #     nonlocal depth
    #     if depth % 2 != 0:
    #         new_list = [b.label for b in t.branches][::-1]
    #         for i in range(len(t.branches)):
    #             t.branches[i].label = new_list[i]
    #             for b in t.branches[i].branches:
    #                 b = helper(b)
    #         depth += 1
    #     else:
    #         depth += 1
    #         return helper(t)
    # t = helper(t)


# 注意这里的破题关键不是找偶数或者奇数index，然后互换。而是把整个level都逆序, [::-1]表示翻转
# Write a function reverse_other that mutates the tree such that labels on every other (odd-depth) level are reversed. 
# For example, Tree(1,[Tree(2, [Tree(4)]), Tree(3)]) becomes Tree(1,[Tree(3, [Tree(4)]), Tree(2)]). 
# Notice that the nodes themselves are not reversed; only the labels are.

def change(list):
    if len(list) < 3:
        return list
    else:
        copy = list[:]
        length = len(copy)
        m, n = length // 4, length % 4
        if length >= 3:
            if m == 0:
                list[0] = copy[2]
                list[2] = copy[0]
            elif m > 0:
                for i in range(m):
                    list[i] = copy[i + 2]
                    list[i + 2] = copy[i]
                if n == 3:
                    list[m * 4] = copy[m * 4 + 2]
                    list[m * 4 + 2] = copy[m * 4]
            return list
    
             
# def change(list):
#     if len(list) < 2:
#         return list
#     else:
#         copy = list[:]
#         length = len(copy)
#         m = length // 2
#         if length >= 2:
#             if m == 0:
#                 list[0] = copy[1]
#                 list[1] = copy[0]
#             elif m > 0:
#                 for i in range(m):
#                     list[i*2] = copy[i*2 + 1]
#                     list[i*2 + 1] = copy[i*2]
#             return list
    


            




class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

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

