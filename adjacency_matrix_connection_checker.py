# Building directly on the Adjacency Matrix task,
# you now need to check if two specific nodes share a connection.
# Write a program that asks the user to input two node numbers.
# Check the matrix at those exact coordinates and print whether they are connected or not.

graph = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

node1 = int(input("enter first node (0-2): "))
node2 = int(input("enter second node (0-2): "))

if graph[node1][node2] == 1:
    print("nodes", node1, "and", node2, "are connected")
else:
    print("nodes", node1, "and", node2, "are not connected")