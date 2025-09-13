class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, product_name, price):
        self.produce_name = product_name
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        if self.stock == 0:
            return 'Inventory empty. Restocking required.'
        else:
            diff = self.balance - self.price
            if diff < 0:
                return f'You must add ${abs(diff)} more funds.'
            else:
                self.balance = 0
                self.stock -= 1
                if diff == 0:
                    return f'Here is your {self.produce_name}.'
                else:
                    return f'Here is your {self.produce_name} and ${diff} change.'
    
    def restock(self, number):
        self.stock += number
        return f'Current {self.produce_name} stock: {self.stock}'

    def add_funds(self, money):
        if self.stock == 0:
            return f'Inventory empty. Restocking required. Here is your ${money}.'
        else:
            self.balance += money
            return f'Current balance: ${self.balance}'

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2020
    >>> dime = mint.create(Dime)
    >>> dime.year
    2020
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2020
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        return kind(self.year)
    
    # 以下是我刚开始写的。注意如果没有return，就没有办法表示create出来的coin
    # 并且在创造instance的时候，无需写self
    # kind.__init__(self, self.year)
    # return kind.__init__(self, self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Mint.current_year

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        year_diff = Mint.current_year - self.year
        if year_diff > 50:
            return self.cents + year_diff - 50
        return self.cents
    # 也可以通过max进行比较，省去if
    # max(Mint.current_year - self.year -50, 0)


class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return Link(n)
    else:
        before = n // 10
        last = n % 10
        result = Link(last)
        while before >= 10:
            middle = before % 10
            before = before // 10
            result = Link(middle, result)
        return Link(before, result)
    
        # else:
        #     middle = before % 10
        #     before = store_digits(before//10)
        #     return Link(before, Link(middle, Link(last)))


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False

    """
    "*** YOUR CODE HERE ***"

        
    if t.is_leaf():
        return True
    else:
        if len(t.branches) > 2:
            return False
        elif len(t.branches) == 1:
            return is_bst(t.branches[0])
        elif len(t.branches) == 2:
            if max_helper(t.branches[0]) <= t.label  and t.label < min_helper(t.branches[1]):
                if all([is_bst(b) for b in t.branches]):
                    return True
            return False

def max_helper(branch):
    if branch.is_leaf():
        # return [branch.label]， 如果返回的是列表，会报错'>' not supported between instances of 'list' and 'int'
        return branch.label
    else:
        return max([branch.label] + [max_helper(b) for b in branch.branches])
    
def min_helper(branch):
    if branch.is_leaf():
        # return [branch.label]
        return branch.label
    else:
        return min([branch.label] + [min_helper(b) for b in branch.branches])    
    
    # def bst_min(t):
    #     if t.is_leaf():
    #         return t.label
    #     return min([t.label] + list(map(bst_min, t.branches)))

    # def bst_max(t):
    #     if t.is_leaf():
    #         return t.label
    #     return max([t.label] + list(map(bst_max, t.branches)))
# if t.is_leaf():
#     return True
# elif len(t.branches) > 2:
#     return False
# elif len(t.branches) == 1:
#     branch = t.branches[0]
#     if branch.label <= t.label:
#         for b in branch.branches:
#             if not is_bst(b):
#                 return False
#             if    len(b.branches) == 1 and b.label > t.label:
#                 return False
#     else:
#         for b in branch.branches:
#             if not is_bst(b):
#                 return False
#             if len(b.branches) == 1 and b.label <= t.label:
#                 return False
# elif len(t.branches) == 2:
#     left_b, right_b = t.branches[0], t.branches[1]
#     if left_b.label > t.label or right_b.label <= t.label:
#         return False
#     elif len(left_b.branches) == 1 and left_b.branches[0].label > t.label:
#         return False
#     elif len(right_b.branches) == 1 and right_b.branches[0].label <= t.label:
#         return False
#     elif is_bst(left_b) is False or is_bst(right_b) is False:
#         return False
# return True
# 疯了吧，写的超长超繁琐, 而且我觉得写的有点问题，Tree再长一点，就出问题了
# 例如
# >>> t8 = Tree(2, [Tree(1, [Tree(0, [Tree(6)])]), Tree(4)])
# >>> is_bst(t8)
# False
# 执行出来却是True




#         elif len(t.branches) == 1:
#             return left_bst(t.branches, t.label) if t.branches.label <= t.label else right_bst(t.branches, t.label)
#         else:
#             return all([is_bst()])
#         elif len(t.branches) == 1:
#             if t.branches.label <= t.label:
#                 for b in t.branches.branches:
#                     if not left_bst(b, t.label):
#                         return False
#             else:
#                 for b in t.branches.branches:
#                     if not right_bst(b, t.label):
#                         return False
#         elif len(t.branches) == 2:
#             left_b, right_b = t.branches[0], t.branches[1]
#             if left_b.label <= t.label or right_b.label <= t.label:
#                 return False
#             for subleft in left_b.branches:
#                 if subleft.label > t.label:
#                     return False
#                 return is_bst(subleft.branch)

# def left_bst(b, label): #
#     if b.is_leaf():
#         return True if b.label <= label else False
#     else:
#         if b.label <= label:
#             for sub in b.branches:
#                 if not left_bst(sub, label):
#                     return False
#             return True
#         return False
    
# def right_bst(b, label):
#     if b.is_leaf():
#         return True if b.label > label else False
#     else:
#         if b.label <= label:
#             for sub in b.branches:
#                 if not left_bst(sub, label):
#                     return False
#             return True
#         return False


            
        #     else:
        #         for subleft in left_b.branches:
        #             if is_bst(subleft) is False:
        #                 return False
        #         for subright in right_b.branches:
        #             if is_bst(subright) is False:
        #                 return False
        # elif len(t.branches) == 1:
        #     return 






    # if t.is_leaf() is True:
    #     return True
    # else:
    #     if len(t.branches) > 2:
    #         return False
    #     elif len(t.branches) == 1:
    #         return True
    #     elif len(t.branches) == 2:
    #         left_b, right_b = t.branches[0], t.branches[1]
    #         if left_b.label > right_b.label:
    #             return False
    #         else:
    #             return is_bst(left_b) and is_bst(right_b)
                # for lb in left_b.branches:
                #     if is_bst(lb) is False:
                #         return False
                # for rb in right_b.branches:
                #     if is_bst(rb) is False:
                #         return False

    

# 本来想import tree的，但是报错。难道因为这里的案例都是Tree，不能直接用？
# if is_leaf(t):
#     return True
# else:
#     if len(branches(t)) > 2:
#         return False
#     elif len(branches(t)) == 1:
#         return is_bst(branches(t))
#     elif len(branches(t)) == 2:
#         left_b = branches(t)[0]
#         right_b = branches(t)[1]
#         if label(left_b) > label(right_b):
#             return False
#         else:
#             return all(is_bst(left_b), is_bst(right_b))


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return [t.label]
    else:
        result = [t.label]
        for b in t.branches:
            result = result + preorder(b)
        return result
    # https://inst.eecs.berkeley.edu/~cs61a/fa20/hw/hw03/
    # hw03已经出现过了，是不是因为前面是用的funtion，现在要用class？


def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(path_yielder(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = path_yielder(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = path_yielder(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """

    "*** YOUR CODE HERE ***"
    if t.label == value:
        yield [t.label]
    for b in t.branches:
        for x in path_yielder(b, value):
            yield [t.label] + x
    "*** YOUR CODE HERE ***"
    # No ELSE clause because finding a desired value does not eliminate the
    # possibility of other desired values' existence down the current path (t2).
    
    # if t.label == value:
    #     yield [t.label]
    # for b in t.branches:
    #     if b.label == value:
    #         yield [t.label, b.label]
    #     else:
    #         for sub in b.branches:
    #             if value in sub:
    #                 yield [t.label, b.label].extend(path_yielder(sub, value))




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

