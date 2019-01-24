NodeList = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i']
edgeList = [(0,1), (0,4), (1,2),(1,3), (4,5), (5,6), (5,8), (6,7)]
graphs = (NodeList, edgeList)

def DFS(graph, start):
    graph = NodeList, edgeList
    stack = [start]
    visited = []
    ancyList = [[] for _ in NodeList]

    for edge in edgeList:
        ancyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in ancyList[current]:
            if neighbor not in visited:
                stack.append(neighbor)
        visited.append(current)
    return visited

print(DFS(graphs, 0))
