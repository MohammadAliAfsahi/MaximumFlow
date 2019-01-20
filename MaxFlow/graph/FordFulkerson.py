class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack: # implementing Stack using linked list with push and pop attributes
    def __init__(self):
        self.head = None

    def push(self, data): # push data into head
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self): # pop last element that entered to stack
        if self.head is None:
            return
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

def dfs(Capacity_matrix, Flow_matrix, s, t): # DFS algorithm in order to find path from source(s) to sink(t)
                     # F is flow matrix and C is adjacency matrix
    stack = Stack()
    stack.push(s)
    paths = {s: []}
    if s == t:
        return paths[s]
    while(stack.head):
        u = stack.pop()
        for v in range(len(Capacity_matrix)):
            if (Capacity_matrix[u][v] - Flow_matrix[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                print("#--------------------------------------#")
                print("All the paths:")
                print(paths)
                print("Added path in this step:")
                print((u, v),"to node",v)
                print("This edge capacity")
                print(Capacity_matrix[u][v])
                print("#--------------------------------------#")
                if v == t:
                    return paths[v]
                stack.push(v)
    return None


def max_flow(Capacity_matrix, s, t): # find max flow in C adjacency matrix from s(source) to t(sink)
                       # Adjacency matrix represents weighted graph
    n = len(Capacity_matrix)
    Flow_matrix = [[0] * n for i in range(n)]
    path = dfs(Capacity_matrix, Flow_matrix, s, t)
    while path != None:
        flow = min(Capacity_matrix[u][v] - Flow_matrix[u][v] for u, v in path)
        for u, v in path:
            Flow_matrix[u][v] += flow
            Flow_matrix[v][u] -= flow
        path = dfs(Capacity_matrix, Flow_matrix, s, t)
    return sum(Flow_matrix[s][i] for i in range(n))
