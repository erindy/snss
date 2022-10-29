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



    def height(self, h=1):
        left_height = self.left.height(h+1) if self.left else h
        right_height = self.right.height(h+1) if self.right else h
        return max(left_height, right_height)

    def get_nodes_at_depth(self, depth, nodes=[]):
        if depth ==0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.get_nodes_at_depth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        if self.right:
            self.right.get_nodes_at_depth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        return nodes







    # my implementations
    def get_max_height(self, counter=0):
        counter += 1
        if self.left is None and self.right is None:
            return counter

        elif self.left is not None and self.right is not None:
            return max(self.left.get_max_height(counter), self.right.get_max_height(counter))
        elif self.right is None and self.left is not None:
            return self.left.get_max_height(counter)

        elif  self.right is not None and self.left is None:
            return self.right.get_max_height(counter)
        return counter

    def all_nodes_at_particular_depth(self, depth, value_list=[], depth_counter=1):
        if depth == depth_counter:
            value_list.append(self.data)
            return

        if self.left is not None:
            self.left.all_nodes_at_particular_depth(depth, value_list, depth_counter+1)
        else:
            value_list.extend([None]*2**(depth_counter-3))

        if self.right is not None:
            self.right.all_nodes_at_particular_depth(depth, value_list, depth_counter+1)
        else:
            value_list.extend([None]*2**(depth_counter-3))

        return value_list

    def print_tree(self):
        max_height = self.get_max_height()
        for i in range(max_height):
            print(self.get_nodes_at_depth(i, []))









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

    def get_max_height(self):
        return  self.root.get_max_height()

    def get_nodes_at_depth(self, depth):
        return self.root.get_nodes_at_depth(depth)

    def print_tree(self, label=""):
        print(self.name+ ' ' + label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) +1)
        # root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth>0:
                # print directional lines
                print(" "*(offset+1) + (" "*(spacing+2)).join(['/' + (' '*(spacing-2)) + "\\"]*(2**(depth-1))))
            row = self.root.get_nodes_at_depth(depth, [])
            print((" "*offset)+"".join([self._node_to_char(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset/2) - 1
        print("")

    def _node_to_char(self, n, spacing):
        if n is None:
            return "_"+(' '*spacing)
        spacing = spacing - len(str(n)) + 1
        return str(n)+(" "*spacing)


if __name__=="__main__":
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)
    node.left.left = Node(2)
    node.left.left.left = Node(1)
    node.left.right = Node(6)
    node.right.left = Node(13)
    node.right.right = Node(1000)

    my_tree = Tree(node, "My tree")
    # found = my_tree.search(1000)
    # print(found.data)

    print(my_tree.print_tree())