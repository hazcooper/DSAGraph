from DSAListNode import DSAListNode
from DSALinkedListIterator import DSALinkedListIterator


class DSALinkedList:

    def __init__(self):

        self.head = None

    def insert_first(self, new_value):

        new_node = DSAListNode(new_value)

        if self.is_empty():

            self.head = new_node

        else:

            new_node.set_next(self.head)
            self.head = new_node

    def insert_last(self, new_value):

        new_node = DSAListNode(new_value)

        if self.is_empty():

            self.head = new_node

        else:

            current_node = self.head

            while current_node.get_next() != None:
                current_node = current_node.get_next()

            current_node.set_next(new_node)

    def is_empty(self):

        return self.head is None

    def peek_first(self):

        if self.is_empty():

            raise ValueError("The Linked list is empty!")

        else:

            node_value = self.head.get_value()
            return node_value

    def peek_last(self):

        if self.is_empty():

            raise ValueError("The Linked list is empty!")

        else:

            current_node = self.head

            while current_node.get_next() != None:
                current_node = current_node.get_next()

            node_value = current_node.get_value()

            return node_value

    def remove_first(self):

        if self.is_empty():

            raise ValueError("The Linked list is empty!")

        else:

            node_value = self.head.get_value()

            self.head = self.head.get_next()

            return node_value

    def remove_last(self):

        if self.is_empty():

            raise ValueError("The Linked list is empty!")

        elif self.head.get_next() == None:

            node_value = self.head.get_value()

            self.head = None

            return node_value

        else:

            previous_node = None

            current_node = self.head

            while current_node.get_next() != None:
                previous_node = current_node

                current_node = current_node.get_next()

            previous_node.set_next(None)

            node_value = current_node.get_value()

            return node_value

    def remove_node(self, value):

        if self.is_empty():
            raise ValueError("The linked list is empty!")

        elif self.head.get_next() == None:
            node_value = self.head.get_value()
            self.head = None
            return node_value

        else:

            previous_node = None
            current_node = self.head

            while current_node.get_next() != None:
                previous_node = current_node
                current_node = current_node.get_next()
                if current_node.get_value() == value:
                    found_node = current_node.get_value()
                    previous_node.set_next(current_node.get_next())

                    return found_node

            # if reaches this point, node was not found
            raise ValueError(f"No node with value {value} found in the list")

    def display_list(self):

        current = self.head

        while current:
            print(current.get_value(), end=" -> ")
            current = current.get_next()

        print("None")

    def contains(self, label):
        current = self.head
        is_true = False

        while current:
            if current.get_value() == label:
                is_true = True
            current = current.get_next()
        return is_true

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()

        return count

    # def iterate(self):
    #     for element in self.head:
    #         element = self.head.getValue
    #         self.head = self.head.getNext
    #
    #     return element

    def __iter__(self):
        return DSALinkedListIterator(self.head)

    def __str__(self):

        curNode = self.head
        result = []
        while curNode:
            result.append(str(curNode.value))
            curNode = curNode.next_node

        return " -> ".join(result)
