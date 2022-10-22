# old implementation
# recursive
from time import time
array_bist =  [0 , 1, 21, 33, 45, 45, 61, 71, 72, 73]


def binary_search_rec(array, search_item):
    array_len = len(array)
    if array_len == 1 and array[0]==search_item:
        return True
    if array_len == 1 and array[0]!=search_item:
        return False
    elif array_len==0:
        return False


    n_2 = array_len // 2

    if array[n_2] > search_item:
        res = binary_search_rec(array[:n_2], search_item)
    elif array[n_2] < search_item:
        res = binary_search_rec(array[n_2:], search_item)

    else:
        return True

    return res


def binary_search_sec(array, element):
    left = 0
    right = len(array)-1
    middle = (left + right) // 2

    while right >= left:

        if array[middle] == element:
            return True
        elif array[middle] > element:
            right = middle - 1
        else:
            left = middle + 1

        middle = (left + right) // 2


    return False


def contains(collection, target):
    return target in collection


def performance(func):
    n = 1024
    while n < 500000000:
        sorted = list(range(n))
        now = time()
        # code whose performance is to be evaluated
        contains(sorted, -1)

        done = time()
        print(n, (done-now)*1000)
        n *=2


class BinaryNode():
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryNode(value)

        else: # value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryNode(value)


    def contains(self, value):

        if self.value == value:
            return True
        elif self.value > value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def find(self, value):

        if self.value > value:
            if self.left is None:
                return None
            self.left.find(value)
        elif self.value < value:
            if self.right is None:
                return None
            self.right.find(value)
        else:
            return self

    def delete(self):
        if self.right is None and self.left is None:
            return None
        elif self.right is None and self.left is not None:
            return self.left
        elif self.right is not None and self.left is None:
            return self.right

        else:

            parent = self
            left_most_child = self.left
            while left_most_child.right is not None:
                parent = left_most_child
                left_most_child = left_most_child.right

            parent.right = None

            self.value = left_most_child.value

            return self



class BinaryTree():
    def __init__(self):
        """create an empty tree"""
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self, target):
        if self.root is None:
            return False
        # if self.root.value == target:
        #     return True
        else:
            return self.root.contains(target)


    def find(self, target):
        if self.root is None:
            return False
        # if self.root.value == target:
        #     return True
        else:
            return self.root.find(target)

    # def remove(self, value):
    #     if not self.contains(value):
    #         # do nothing because the value is not there
    #         pass
    #     else:
    #         node = self.find(value)
    #         # we decide whether it is a single leaved node, no leaved node or double leaved node
    #         if node.right is None and node.left is None:
    #             # delete the node
    #         if

    def remove(self, value):
        if self.root:
            self.root = self.remove_from_parent(self.root, value)


    def alternate_contains(self, target):
        node = self.root
        while node is not None:
            if node.value > target:
                node = node.left
            elif node.value < target:
                node = node.right

            else:
                return True
        return False

    def remove_from_parent(self, parent, value):
        # base case
        if parent is None:
            return None
        if parent.value > value:
            parent.left = self.remove_from_parent(parent.left, value)
        elif parent.value < value:
            parent.right = self.remove_from_parent(parent.right, value)
        else:
            return parent.delete()

        return parent


import random
def performance_bin():
    n = 1024
    while n <= 655366:
        bt = BinaryTree()
        for i in range(n):
            bt.add(random.randint(1,n))
        now = time()
        bt.alternate_contains(random.randint(1,n))
        print(n, (time() - now)*1000)

        n *= 2


if __name__=='__main__':
    # bt = BinaryTree()
    # bt.add(5)
    # print(bt.contains(10))

    # performance_bin()

    bt = BinaryTree()
    bt.add(5)
    bt.add(1)
    bt.add(10)
    bt.contains(5)
