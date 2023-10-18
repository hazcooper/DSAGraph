from DSALinkedList import DSALinkedList
from DSAGraphNode import DSAGraphNode
from DSAQueue import DSAQueue
from DSAStack import DSAStack


class DSAGraph:

    def __init__(self):
        self.vertices = DSALinkedList()

    def add_vertex(self, label, value=None, category=None, location=None, rating=None):
        new_vertex = DSAGraphNode(label, value, category, location, rating)
        # insert last into linked list
        self.vertices.insert_last(new_vertex)


    def delete_vertex(self, label):
        vertex_to_delete = self.get_vertex(label)
        # find value and remove from linked list
        # exception handling
        if vertex_to_delete is None:
            raise ValueError(f"Vertex with label {label} not found!")

        # if vertex_to_delete.get_adjacent() is not None:
            # iterate through the nodes and see if they have this node adjacent if they do remove it
            # from there edge list, how would i do this?
        for vertex in self.vertices:
            for adjacent_vertex in vertex.get_adjacent():
                if adjacent_vertex.get_label() == vertex_to_delete.get_label():
                    vertex.delete_edge(vertex_to_delete)

        self.vertices.remove_node(vertex_to_delete)

    def delete_edge(self, label_one, label_two):
        # getting the vertex associated with the label
        vertex_one = self.get_vertex(label_one)
        vertex_two = self.get_vertex(label_two)
        vertex_one.delete_edge(vertex_two)
        vertex_two.delete_edge(vertex_one)

    def add_edge(self, label_one, label_two):
        vertex_one = self.get_vertex(label_one)
        vertex_two = self.get_vertex(label_two)
        vertex_one.add_edge(vertex_two)
        vertex_two.add_edge(vertex_one)

    def has_vertex(self, label):
        return self.vertices.contains(label)

    def get_vertex_count(self):
        return self.vertices.size()

    def get_edge_count(self):
        count = 0
        for vertex in self.vertices:
            count += len(vertex.get_adjacent())
        return count // 2

    def get_vertex(self, label):
        x = None
        for node in self.vertices:
            vertex = node
            if vertex.get_label() == label:
                x = vertex

        return x

    def get_adjacent(self, label):
        vertex = self.get_vertex(label)
        if vertex:
            connected_nodes = vertex.get_adjacent()
        else:
            raise ValueError("The vertex doesn't exist")

        return connected_nodes

    def is_adjacent(self, label_one, label_two):
        is_true = False
        vertex_one = self.get_vertex(label_one)
        vertex_two = self.get_vertex(label_two)
        if vertex_one and vertex_two:
            is_true = vertex_two in vertex_one.get_adjacent()

        return is_true

    # def display_as_list(self):
    #     for vertex in self.vertices:
    #         adjacent_nodes = [v.value for v in vertex.get_adjacent()]
    #         adjacent_labels = [adjacent_nodes.value.get_label() for adjacent_nodes in vertex.get_adjacent()]
    #         print(vertex.get_label(), "->", adjacent_labels)

    def display_as_list(self):
        for vertex in self.vertices:
            adjacent_labels = [node.get_label() for node in vertex.get_adjacent()]
            print(vertex.get_label(), "->", adjacent_labels)

    def display_as_matrix(self):
        # creates a list of vertex labels in graph, determines row and column size for matrix
        labels = [vertex.get_label() for vertex in self.vertices]
        # initializes the matrix filled with 0s
        matrix = [[0 for _ in labels] for _ in labels]

        for i, vertex_one in enumerate(self.vertices):
            for j, vertex_two in enumerate(self.vertices):
                matrix[i][j] = 1 if vertex_two in vertex_one.get_adjacent() else 0

    def breadth_first_search(self):
        t = DSAQueue()
        q = DSAQueue()

        # setting visited to false on all vertices
        for vertex in self.vertices:
            vertex.clear_visited()

        start_vertex = self.vertices.peek_first()
        start_vertex.set_visited()
        q.enqueue(start_vertex)

        while not q.is_empty():
            start_vertex = q.dequeue()
            print(start_vertex, end=" ")
            for w in start_vertex.get_adjacent():
                if not w.get_visited():
                    t.enqueue(start_vertex)
                    t.enqueue(w)
                    w.set_visited()
                    q.enqueue(w)

    def depth_first_search(self):
        # init stack and queue
        t = DSAQueue()
        s = DSAStack()


        # string to store output order in depth first search
        output_str = ""
        # setting visited to false on all vertices
        for vertex in self.vertices:
            vertex.clear_visited()

        # getting first vertex and storing in start vertex variable
        start_vertex = self.vertices.peek_first()
        # setting start vertex as visited
        start_vertex.set_visited()
        # pushing start vertex onto stack
        s.push(start_vertex)
        output_str += start_vertex.get_label() + " "

        while not s.is_empty():
            for w in start_vertex.get_adjacent():
                if not w.get_visited():
                    t.enqueue(start_vertex)
                    # print(start_vertex, end=" ")
                    t.enqueue(w)
                    w.set_visited()
                    output_str += w.get_label() + " "
                    # print(start_vertex, w, end=" ")
                    # print(w.get_label())
                    s.push(w)
                    start_vertex = w
            # print(t)
            start_vertex = s.pop()

        print(output_str.strip())