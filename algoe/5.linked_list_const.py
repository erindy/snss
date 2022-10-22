class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insert_before(self.head, node)

    def set_tail(self, node):
        if self.tail is None:
            self.set_head(node)
            return
        self.insert_after(self.tail, node)

    def insert_before(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev =  node.prev
        node_to_insert.next = node
        if node.prev is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert

        node.prev = node_to_insert

    def insert_after(self, node, node_to_insert):
        # node.prev remains the same
        # node.next needs to be updated to node_insert
        # node_to_insert.prev should be updated to node
        # node_to_insert.next should be updated to node.next

        if node_to_insert == self.head and node_to_insert ==self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node
        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert

        node.next = node_to_insert





    def insert_at_position(self, position, node_to_insert):
        if position == 1:
            self.set_head(node_to_insert)
            return
        node = self.head
        current_position = 1
        while node is not None and current_position != position:
            node = node.next
            current_position += 1

        if node is not None:
            self.insert_before(node, node_to_insert)

        else:
            self.set_tail(node_to_insert)

    def remove_node_with_value(self, value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    def remove(self, node):

        # none <----- node ----> none
        # in this case head and tail are two different variables pointing to the same node
        # so we have to update two variables? self.head & self.tail
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
            
            
        self.__remove_node_bindings(node)


    def contains_node_with_value(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next

        return node is not None

    def __remove_node_bindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None



def run():
    pass

if __name__ == "__main__":
    run()