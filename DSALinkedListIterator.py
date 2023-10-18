class DSALinkedListIterator:

    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        node = self.current
        self.current = self.current.get_next()
        return node.get_value()
