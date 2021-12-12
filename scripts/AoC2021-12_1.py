def rec(graph, path):
    total = 0
    for adj in graph[path[-1]]:
        if adj == 'end':
            total += 1
        elif not adj.islower() or adj not in path:
            total += rec(graph, path + [adj])
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

print(rec(graph, ['start']))
