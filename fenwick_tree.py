__author__ = 'ratnesh.mishra'


class BinaryIndexedTree:

    def __init__(self, tree):
        self.tree = tree

    def update_tree(self, incr, size):
        idx = 0
        while idx <= size:
            self.tree[idx] += incr
            idx += idx - idx

    def get_value(self, idx, size):

        if idx > size: return self.tree[size-1]
        it, cumsum = 0, 0
        while it:
            cumsum += self.tree[it]
            it -= it & -it

        return cumsum


if __name__ == '__main__':
    """
    List of numbers can be provided
    upon which sample (below) operations can be performed in O(lgn) where n = size of list
    1. Cumulative updates
    2. Retrieve value of a particular index
    """
    s = input()
    numbers = list(map(int, s.split()))
    bit = BinaryIndexedTree(numbers)









