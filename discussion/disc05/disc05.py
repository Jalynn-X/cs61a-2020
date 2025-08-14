from tree import *

# trees


# 01. height of tree
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t) is True:
        return 0
    else:
        t_branches = branches(t)
        max_branch = max(t_branches, key=len)
        return height(max_branch) + 1
# 我是先考虑哪个branch的元素最多，就说明height最大
# 网上看到有一种解法是，直接return max(height(branch) for branch in branches(t)) + 1



# 02. maximum sum of the values along any path in the tree
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    node = label(t)
    if is_leaf(t) is True:
        return node
    else:
        return node + max(max_path_sum(branch) for branch in branches(t))


# 03. takes in a tree and squares every value
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers =tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7)]), tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    if is_leaf(t) is True: 
        return tree(pow(label(t), 2))
    else:
        return tree(pow(label(t), 2), 
                    [square_tree(branch) for branch in branches(t)])
    

# 04. return lists of paths of a tree including x
# def find_path(t, x):
#     """
#     takes in a tree and a value x and returns a list containing the nodes 
#     along the path required to get from the root of the tree to a node containing x.
#     >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
#     >>> find_path(t, 5)
#     [2, 7, 6, 5]
#     >>> find_path(t, 10) # returns None
#     """
#     if label(t) == x:
#         return [label(t)]
#     else:
#         if len(branches(t)) == 0:
#             return None
#         else:
#             for branch in branches(t):
#                 if find_path(branch, x) is not None:
#                     return [label(t)] + find_path(branch, x)
# 以上是我自己写的版本。实在是无法一步到位填出空格部分，所以打算自己写了，再改写

def find_path(t, x):
    """
    takes in a tree and a value x and returns a list containing the nodes 
    along the path required to get from the root of the tree to a node containing x.
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(t) == x:
        return [label(t)]
    for branch in branches(t):
        path = find_path(branch, x)
        if path is not None:
            return [label(t)] + path

# if is_leaf(t) is True and label(t) == x:
#     return [label(t)]
# elif len(branches(t)) > 0:
#     path = [find_path(branch, x) for branch in branches(t)]
#     if label(t) == x or x in [y for y in path]:
#         return label(t) + [y for y in path if x in y]
        
# elif len(branches(t)) == 0:
#     return []

#     for branch in branches(t):
#         path = 
#         if x in path:
#             return [label(t)] + find_path(branch, x)

# if label(t) == x:
#     return [label(t)]
# else: # label(t) != x
#     if len(branches(t)) !=0 :
#         for branch in branches(t):
#             if find_path(branch, x) :
#                 path = [label(t)] + find_path(branch, x)
#                 return path
#     elif len(branches(t)) == 0:
#         return []

# 05. binary numbers
# 5 = 4 + 1 = 2^2 + 2^0 = 101
# 10 = 8 + 2 = 2^3 + 2^1 = 1010
# 14 = 8 + 4 + 2 = 2^3 + 2^2 + 2^1 = 1110
# 37= 32 + 2 = 2^5 + 2^1 = 100010
# 10 = 2^1 = 2
# 101010 = 2^5 + 2^3 + 2^1 = 32 + 8 + 2 = 42
# 1100101 = 2^6 + 2^5 + 2^2 + 2^0 = 64 + 32 + 4 + 1 = 101

# 06.
def prune_binary(t, nums):
    """
    Write a function that takes in a tree t that is consisted of 0s and 1s
    and a list of binary numbers nums. 
    Returns a new tree that contains only the numbers in nums that exist in t. 
    >>> t = tree('1', [tree('0', [tree('0'), tree('1')]), tree('1', [tree('0')])])
    >>> num = ['01', '110', '100']
    >>> prune_binary(t, num)
    ['1', ['0', ['0']], ['1', ['0']]]
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums if num[0] == label(t)]
        new_branches = []
        for branch in branches(t):
            pruned_branch = prune_binary(branch, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)
# 要是我自己写的话估计我还会考虑位数？
# 但其实不考虑位数也无所谓了，循环到最后就是leaf，如果t走到了leaf那一步，还不存在于nums里
# 就可以说明不符合了
# 其实我做的时候，还有一个很纠结的点在于，如果不是leaf，那么如何比较开头第一个数字？
# 看到网上有一种解法是在next_valid_nums后面加限定，即：
# next_valid_nums = [num[1:] for num in nums if num[0] == label(t)]





# if 
#     if :
#         return 
#     return None
# else:
#     next_valid_nums = [x[1:] for x in nums]
#     new_branches = []
#     for branch in branches(t):
#         pruned_branch = prune_binary(branch, next_valid_nums)
#         if pruned_branch is not None:
#             new_branches = new_branches + tree[pruned_branch]
#     if not new_branches:
#         return None
#     return tree(label(t), new_branches)

