
class node:
    def __init__(self, name, x = None, y = None):
        self.name = name
        self.edges = []
        self.x = x
        self.y = y

    def connect(self, node):
        key = (self.name, node.name)
        self.edges.append(key)

class edge:
    def __init__(self, left, right, weight = 1):
        self.left = left
        self.right = right
        self.weight = weight

class graph:
    time = 0
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.bfs_time = 0
        self.dfs_time = 0
        self.dijkstra_time = 0
        self.a_star_time = 0
        self.bfs_length = 0
        self.dfs_length = 0
        self.dijkstra_length = 0
        self.a_star_length = 0
        self.count = 0
        self.number_of_edges = 0

    def addEdge(self, left, right, weight = 1):
        self.number_of_edges += 1
        self.nodes[left.name] = left
        self.nodes[right.name] = right
        new_edge = edge(left, right, weight)
        key = (left.name, right.name)
        self.edges[key] = new_edge
        key = (right.name, left.name)
        self.edges[key] = new_edge
        left.connect(right)
        right.connect(left)
    
   
        
    def load_graph(self, file_name):
        f = open("graph.txt", "r")
        graph_dict = {}
        coordinates = {}
        for x in f:
            name = ""
            neighbour_name = ""
            neighbour_weight = ""
            neighbour_dict = {}
            reading_name = True
            reading_neighbour = False
            reading_neighbour_name = True
            reading_neighbour_weight = False
            reading_coordinate = False
            reading_first_coordinate = False
            reading_second_coordintate = False
            first_coordinate = ""
            second_coordinate = ""
            for char in x:
                if not reading_coordinate:
                    if ord(char) == 40:
                        reading_name = False
                    elif ord(char) == 93:
                        if ord(neighbour_name[0]) == 32:
                                neighbour_name = neighbour_name[1:]
                        neighbour_dict[neighbour_name] = int(neighbour_weight)
                        neighbour_name = ""
                        neighbour_weight = ""
                        reading_neighbour = False
                        reading_neighbour_weight = False
                        reading_neighbour_name = True
                        reading_coordinate = True
                        continue
                    elif ord(char) == 91:
                        reading_neighbour = True
                        reading_name = False
                        continue
                    if reading_name:
                        name += char
                    if reading_neighbour:
                        if ord(char) == 58:
                            reading_neighbour_weight = True
                            reading_neighbour_name = False
                            continue
                        elif ord(char) == 44 or ord(char) == 93:
                            if ord(neighbour_name[0]) == 32:
                                neighbour_name = neighbour_name[1:]
                            neighbour_dict[neighbour_name] = int(neighbour_weight)
                            neighbour_name = ""
                            neighbour_weight = ""
                            reading_neighbour_weight = False
                            reading_neighbour_name = True
                            continue
                        if reading_neighbour_name:
                            neighbour_name += char
                        if reading_neighbour_weight:
                            neighbour_weight += char
                else:
                    if ord(char) == 40:
                        reading_first_coordinate = True
                        reading_second_coordintate = False
                        continue
                    elif ord(char) == 41:
                        reading_neighbour = False
                        reading_neighbour_weight = False
                        reading_neighbour_name = True
                        reading_coordinate = False
                        reading_first_coordinate = False
                        reading_second_coordintate = False
                        break
                    elif ord(char) == 44:
                        reading_first_coordinate = False
                        reading_second_coordintate = True
                        continue
                    if reading_first_coordinate:
                        first_coordinate += char
                    if reading_second_coordintate:
                        second_coordinate += char
            if name == "\n":
                break
            graph_dict[name] = neighbour_dict
            coordinates[name] = (float(first_coordinate), float(second_coordinate))
        added = {}
        added_edge = set()
        for current_node in graph_dict.keys():
            x_node, y_node = coordinates[current_node]
            if current_node not in added.keys():
                added[current_node] = node(current_node, x_node, y_node)
            for neighbour in graph_dict[current_node].keys():
                x_neighbour, y_neighbour = coordinates[neighbour]
                if neighbour not in added.keys():
                    added[neighbour] = node(neighbour, x_neighbour, y_neighbour)
                if (current_node, neighbour) not in added_edge:
                    self.addEdge(added[current_node], added[neighbour], graph_dict[current_node][neighbour])
                    added_edge.add((current_node, neighbour))
                    added_edge.add((neighbour, current_node))
        