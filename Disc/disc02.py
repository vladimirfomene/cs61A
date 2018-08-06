# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

def tree_max(t):
    """Return the max of a tree."""
    def collect_labels(t, labels = []):
        labels.append(label(t))
        for b in branches(t):
            collect_labels(b, labels)
        return labels
    return max(collect_labels(t))

def tree_max(t):
    """Return the max of a tree."""
    return max([label(t)] + [tree_max(b) for b in branches(t)])

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    else:
        return max([1 +  height(b) for b in branches(t)])

def square_tree(t):
    """Return a tree with the square of every element in t"""
    return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])

def find_path(tree, x):
    """Can implement a much faster algorithm if I assume that the tree is binary
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    return [find_path(b) for b in branches(tree) if contains(b, x)]

def contains(tree, x):
    """Returns true if a tree contains a particular value
    >>>contains(t, 5)
    True
    >>>contains(t, 8)
    False
    """
    found = None
    if label(tree) == x:
        found = True
    else:
        for b in branches(tree):
            contains(b, x)
    return found


def prune(t, k):
    return tree(leaf(t), [prune(b, k - 1) for b in branches(t) if k > 0])
