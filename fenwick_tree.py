__author__ = 'ratnesh.mishra'


class BinaryIndexedTree:

    def __init__(self):
        self.tree = []

    def update_tree(self, incr, idx, size):
        idx += 1
        while idx <= size:
            self.tree[idx] += incr
            idx += idx & - idx

    def construct_tree(self, arr: list=[]):
        self.tree = [0]*(len(arr)+1)
        for idx, val in enumerate(arr):
            self.update_tree(val, idx, len(arr))
        return

    def get_cum_sum(self, idx, size):

        if idx > size: return self.tree[size-1]
        it, cumsum = idx + 1, 0
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
    bit = BinaryIndexedTree()
    bit.construct_tree(numbers)
    k = int(input())
    print(bit.get_cum_sum(k, len(numbers)))
