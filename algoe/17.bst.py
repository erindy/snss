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


    def remove(self, value, parentNone = None):
        if not self.contains(value):
            return

        # case when the value to be removed is a leaf node






if __name__=="__main__":
    # bst_ = BST(4)
    # bst_.insert(6)
    # bst_.insert(3)
    # bst_.insert(8)
    #
    # print(bst_.contains(8))
    # print(bst_.contains(0))
    print(sort_csv_columns_test("Beth,Charles,Danielle,Adam,Eric\n17945,10091,10088,3907,10132\n2,12,13,48,11"))


