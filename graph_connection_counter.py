# 1 means connected, 0 means not connected
graph = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

for row in range(len(graph)):
    connections = 0
    for col in range(len(graph[row])):
        if graph[row][col] == 1:
            connections += 1

    print("Node", row, "has", connections, "connections")