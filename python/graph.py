class Node:
    '''
    
    The Node class holds two attributes:
        - the 'value' attribute represents the value currently stored at the Node object
        - the 'next' attribute represents the next node to which the Node object points

    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class Graph:
    '''
    
    The Graph class will create an undirected graph data structure filled with nodes (vertices). 
    Here we will adopt the adjacency representation of the graph
    Two attributes:
        - 'num_nodes' - holds the number of nodes in the graph whose values range from (0 - num_nodes - 1)
        - 'graph' - holds the adjacency list where each index holds the Node object whose value is that of the index number. 
                    Each Node object will turn into an linked list which shows which nodes are connected to that Node object  

    '''
    def __init__(self, num_nodes):
        
        self.num_nodes = num_nodes
        self.graph = [None] * num_nodes # all linked lists end with None

    def add_edge(self, u_idx, v_idx):
        # let u == from_node
        # let v == to_node
        # direction doesn't matter so order of operation for connecting u -> v and v -> u doesn't matter
        u = Node(u_idx)
        v = Node(v_idx)

        # we need to connect u -> v
        u.next = self.graph[v_idx]  # since linked_list store at idx v in the graph attribute
        self.graph[v_idx] = u # update graph attribute at idx v to object 

        v.next = self.graph[u_idx]
        self.graph[u_idx] = v
    
    def print_agraph(self):
        for i in range(self.num_nodes):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.value), end="")
                temp = temp.next
            print(" \n")



if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()
