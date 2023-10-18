from DSAGraphNode import DSAGraphNode
from DSAGraph import DSAGraph


def main():
    graph = DSAGraph()
    is_running = True

    while is_running:
        print("Welcome to the graph program!")
        print("Your options to choose from are as follows:")
        print("1. Add Shop")
        print("2. Delete Shop")
        print("3. Add edge")
        print("4. Delete edge")
        print("5. Display as list")
        print("6. Display as matrix")
        print("7. Breadth first search")
        print("8. Depth first search")
        print("9. Exit")

        chosen_option = input("Please choose an option: ")

        if chosen_option == "1":
            added_vertex = input("Please enter the Shop name you want to add: ")
            vertex_value = input("Please enter the Shop number : ")
            vertex_category = input("Please enter the Shop category: ")
            vertex_location = input("Please enter the Shop location: ")
            vertex_rating = input("Please enter the Shop rating: ")

            graph.add_vertex(added_vertex, vertex_value, vertex_category, vertex_location, vertex_rating)


        elif chosen_option == "2":

            vertex_to_delete = input("Please enter the Vertex you want to delete: ")
            graph.delete_vertex(vertex_to_delete)

        elif chosen_option == "3":
            edge_one = input("Please enter the first vertex you want to add the edge to: ")
            edge_two = input("Please enter the second vertex you want to add the edge to: ")

            graph.add_edge(edge_one, edge_two)

        elif chosen_option == "4":
            edge_one = input("Please enter the first vertex you want to delete the edge from: ")
            edge_two = input("Please enter the second vertex you want to delete the edge from: ")

            graph.delete_edge(edge_one, edge_two)

        elif chosen_option == "5":
            graph.display_as_list()

        elif chosen_option == "6":
            graph.display_as_matrix()

        elif chosen_option == "7":
            print("Following is the Breadth-First Search")
            graph.breadth_first_search()

        elif chosen_option == "8":
            print("Following is the Depth-First Search")
            graph.depth_first_search()

        elif chosen_option == "9":
            is_running = False
            print("Exiting the program. Goodbye!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
