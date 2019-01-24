NodeList = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i']
edgeList = [(0,1), (0,4), (1,2),(1,3), (4,5), (5,6), (5,8), (6,7)]
graphs = (NodeList, edgeList)

def bfs(graph, start):
    graph = NodeList, edgeList
    visited = []
    queue = [start]
    adjancencyList = [[] for vertex in NodeList]

    for edge in edgeList:
        adjancencyList[edge[0]].append(edge[1])

    while queue:
        current = queue.pop()
        for neighbor in adjancencyList[current]:
            if not neighbor in visited:
                queue.insert(0,neighbor)
                """
                DFS - stack. LIFO => .append(neighbor) insert at the tail to come out first
                BFS - queue. FILO=> insert(0, neighbor) insert at the head to come out at last """
        visited.append(current)
    return visited

gp = bfs(graphs, 0)
print(gp)
N = []
for i in range(len(gp)):
    N.append(NodeList[gp[i]])
print(N)

