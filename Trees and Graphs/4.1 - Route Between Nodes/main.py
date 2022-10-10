from collections import defaultdict

class Graph(object):

    def __init__(self, vertices):
        #Number of vertices in graph
        self.vertices = vertices
        #Using default dic to rep graph
        self.graph = defaultdict(list)

    def addEdge(self, node, nextNode):
        self.graph[node].append(nextNode)

    def isReachable(self, start, finish):
        visited = [False] * self.vertices
        queue = []

        #Start at 'start' node
        queue.append(start)
        visited[start] = True

        while queue:
            current = queue.pop(0)
            if current == finish:
                return True

            for i in self.graph[current]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return False

    def display(self):
        for k, v in self.graph.items():
            print(k)
            print(v)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.display()

u = 1; v = 3
 
if g.isReachable(u, v):
    print("There is a path from %d to %d" % (u,v))
else:
    print("There is no path from %d to %d" % (u,v))
 
u = 3; v = 1

if g.isReachable(u, v):
    print("There is a path from %d to %d" % (u,v))
else:
    print("There is no path from %d to %d" % (u,v))