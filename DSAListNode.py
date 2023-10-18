class DSAListNode:
    
    def __init__(self, value):
        
        self.value = value
        self.next_node = None
        self.prev_node = None

    def get_value(self):
        
        return self.value

    def get_next(self):

        return self.next_node
    
    def get_prev(self):

        return self.prev_node

    def set_value(self, in_value):

        self.value = in_value

    def set_next(self, new_next):

        self.next_node = new_next

    def set_prev(self, new_prev):

        self.prev_node = new_prev
