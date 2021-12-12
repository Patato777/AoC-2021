def rec(graph, path, small):
    total = 0
    for adj in graph[path[-1]]:
        if adj == 'end':
            path.append('end')
            total += 1
        elif adj != 'start':
            if not adj.islower() or (small == 2 and adj not in path):
                total += rec(graph, path + [adj], small)
            elif small < 2:
                total += rec(graph, path + [adj], (path + [adj]).count(adj)) 
    return total

graph = dict()
with open('../inputs/AoC2021-12.txt', 'r') as f:
    for line in f:
        vertices = line.strip().split('-')
        if vertices[0] in graph.keys():
            graph[vertices[0]].append(vertices[1])
        else:
            graph[vertices[0]] = [vertices[1]]
        if vertices[1] in graph.keys():
            graph[vertices[1]].append(vertices[0])
        else:
            graph[vertices[1]] = [vertices[0]]

print(rec(graph, ['start'], 0))
