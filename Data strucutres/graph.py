

class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ": ", self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, ver1, ver2):
        if self.adj_list.get(ver1) is None or self.adj_list.get(ver2) is None: 
            return False
        
        self.adj_list[ver1].append(ver2)
        self.adj_list[ver2].append(ver1)
        
        return True
        
    def remove_edge(self, ver1, ver2):
        if self.adj_list.get(ver1) is None or self.adj_list.get(ver2) is None: 
            return False
        try:
            self.adj_list[ver1].remove(ver2)
            self.adj_list[ver2].remove(ver1)
        except ValueError:
            pass
        
        return True
        
    def remove_vertex(self, vertex):
        if vertex in self.adj_list is not None:
            for i in self.adj_list[vertex]:
                self.adj_list[i].remove(vertex)
            self.adj_list.pop(vertex)       
            return True
        return False        
    
graph = Graph()

graph.add_vertex("Eslam")
graph.add_vertex("Ahmed")
graph.add_vertex("Osama")
graph.add_vertex("Sami")

graph.add_edge("Eslam", "Ahmed")
graph.add_edge("Ahmed", "Osama")
graph.add_edge("Eslam", "Osama")


graph.print_graph()

print()

graph.remove_vertex("Eslam")

graph.print_graph()