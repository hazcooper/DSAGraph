from DSALinkedList import DSALinkedList

class DSAGraphNode:
    def __init__(self, shopNumber, shopName, category, location, rating):
        self.shopNumber = shopNumber
        self.shopName = shopName
        self.category = category
        self.location = location
        self.rating = rating
        self.links = DSALinkedList()   # Adjacency list
        self.visited = False

    # Getter methods
    def get_shopNumber(self):
        return self.shopNumber
    
    def get_shopName(self):
        return self.shopName
    
    def get_category(self):
        return self.category
    
    def get_location(self):
        return self.location
    
    def get_rating(self):
        return self.rating

    def get_adjacent(self):
        return self.links.__iter__()

    def is_adjacent(self, vertex):
        for existing_vertex in self.links:
            if existing_vertex.get_shopNumber() == vertex.get_shopNumber():
                return True
        return False

    def get_visited(self):
        return self.visited

    def add_edge(self, vertex):
        if not self.is_adjacent(vertex):
            self.links.insert_last(vertex)
        else:
            print(f"Edge already exists between shop {self.shopNumber} and shop {vertex.get_shopNumber()}")

    def set_visited(self):
        self.visited = True

    def clear_visited(self):
        self.visited = False

    # Utility methods to update shop details
    def update_shopName(self, newName):
        self.shopName = newName

    def update_category(self, newCategory):
        self.category = newCategory

    def update_location(self, newLocation):
        self.location = newLocation

    def update_rating(self, newRating):
        if 1 <= newRating <= 5:
            self.rating = newRating
        else:
            print("Invalid rating. Please provide a rating between 1 and 5.")

    def to_string(self):
        return f"Shop Number: {self.shopNumber}, Shop Name: {self.shopName}, Category: {self.category}, Location: {self.location}, Rating: {self.rating}"


