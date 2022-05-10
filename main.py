# Python3 program for the above approach

# Stores the parent of each vertex
parent = [0] * (1000000)


# Function to find the topmost
# parent of vertex a
def root(a):
    # If current vertex is
    # the topmost vertex
    if (a == parent[a]):
        return a

    # Otherwise, set topmost vertex of
    # its parent as its topmost vertex
    parent[a] = root(parent[a])
    return parent[a]


# Function to connect the component
# having vertex a with the component
# having vertex b
def connect(a, b):
    # Connect edges
    a = root(a)
    b = root(b)

    if (a != b):
        parent[b] = a


# Function to find unique top most parents
def connectedComponents(n):
    s = set()

    # Traverse all vertices
    for i in range(n):
        # Insert all topmost
        # vertices obtained
        s.add(root(parent[i]))

    # Print count of connected components
    print(len(s))


# Function to print answer
def printAnswer(N, edges):
    # Setting parent to itself
    for i in range(N + 1):
        parent[i] = i

    # Traverse all edges
    for i in range(len(edges)):
        connect(edges[i][0], edges[i][1])

    # Print answer
    connectedComponents(N)


# Using readlines()
file1 = open('graf.txt', 'r')
Lines = file1.readlines()

verticies = set()
# Strips the newline character
for line in Lines:

    splitted = line.split(' ')
    verticies.add(splitted[0].strip())
    verticies.add(splitted[1].strip())

mapper = {}
id = 0
for val in verticies:
    mapper[id]=val
    id+=1

inv_map = {v: k for k, v in mapper.items()}

# Given N
N = len(verticies)

# Given edges
edges = []

for line in Lines:

    splitted = line.split(' ')

    v1 = inv_map[splitted[0].strip()]
    v2 = inv_map[splitted[1].strip()]

    edges.append([v1,v2])

printAnswer(N, edges)
# This code is contributed by divyesh072019