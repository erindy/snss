class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        current_node = self
        while current_node is not None:
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                current_node = current_node.left



    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
            else:
                return True

        return False


    def __retrieve_node(self, value):
        current_node = self
        parent = None
        while current_node is not None:
            if value > current_node.value:
                parent = current_node
                current_node = current_node.right
            elif value < current_node.value:
                parent = current_node
                current_node = current_node.left
            else:
                return current_node, parent

        return None, None

    def clear_left_most(self, parent_node):
        current_node = self
        parent_node = parent_node
        while current_node is not None:
            if current_node.left is not None:
                parent_node = current_node
                current_node = current_node.left
            # elif current_node.right is not None:
            #     parent_node = current_node
            #     current_node = current_node.right
            else:
                # if current_node.right has a value then we need to attach the value

                left_most_value = current_node.value
                if parent_node.value >= current_node.value:
                    parent_node.left = None
                else:
                    parent_node.left = current_node.right

                return left_most_value



    def remove(self, value, parentNone = None):
        if not self.contains(value):
            return

        # find the item you are looking for
        target_node, parent_node = self.__retrieve_node(value)

        # case when the value to be removed is a leaf node
        if (target_node.left is None) and (target_node.right is None):
            if parent_node.value >= target_node.value:
                parent_node.left = None
            else:
                parent_node.right = None

        # case when the node has only one child
        if (target_node.left is None) and (target_node.right is not None):
            if parent_node.value >= target_node.value:
                parent_node.left = target_node.right
            else:
                parent_node.right = target_node.right


        if (target_node.left is not None) and (target_node.right is None):
            if parent_node.value >= target_node.value:
                parent_node.left = target_node.left
            else:
                parent_node.right = target_node.left

        # case when the node has two children
        if (target_node.left is not None) and (target_node.right is not None):
            left_most_value = target_node.right.clear_left_most(target_node)
            target_node.value = left_most_value




""""
            4
           / \
          3   7
         /    /\
        1    5  8
              \
               6
"""


if __name__=="__main__":
    bst_ = BST(4)
    bst_.insert(7)
    bst_.insert(3)
    bst_.insert(1)
    bst_.insert(5)
    bst_.insert(6)
    bst_.insert(8)

    print(bst_.contains(8))
    print(bst_.contains(0))
    bst_.remove(8)
    print("test")


