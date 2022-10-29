class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def search(self, target):
        cursor = self
        while cursor is not None:
            if target > cursor.data:
                cursor = cursor.right
            elif target < cursor.data:
                cursor = cursor.left
            else:
                return cursor
        return None

    def search_rec(self, target):
        if target is None:
            return None

        if target > self.data:
            return self.right.search_rec(target)
        elif target < self.data:
            return self.left.search_rec(target)
        else:
            return self

    def traverse_preorder(self):
        print(self.data)
        # base case
        if self.left is None and self.right is None:
            return

        if self.left:
            self.left.traverse_preorder()

        if self.right:
            self.right.traverse_preorder()

    def traverse_in_order(self):
        if self.left is None and self.right is None:
            print(self.data)
            return

        if self.left:
            self.left.traverse_in_order()

        print(self.data)

        if self.right:
            self.right.traverse_in_order()


    def traverse_post_order(self):
        if self.left is None and self.right is None:
            print(self.data)
            return

        if self.left:
            self.left.traverse_post_order()


        if self.right:
            self.right.traverse_post_order()

        print(self.data)




class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, data):
        return self.root.search_rec(data)

    def traverse_preorder(self):
        self.root.traverse_preorder()

    def traverse_in_order(self):
        self.root.traverse_in_order()

    def traverse_post_order(self):
        self.root.traverse_post_order()


