# Python3 program for the above approach

# Stores the parent of each vertex
import math

parent = None


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
        r = root(parent[i])
        s.add(r)

    # Print count of connected components
    print(len(s))


# Function to print answer
def printAnswer(N, edges):
    # Setting parent to itself
    for i in range(N):
        parent[i] = i

    # Traverse all edges
    for i in range(len(edges)):
        connect(edges[i][0], edges[i][1])

    # Print answer
    connectedComponents(N)

def join(tmp,to):
    for k in range(N):
        if parent[k] == tmp:
            parent[k] = to

# Using readlines()
file1 = open('test2.txt', 'r')
Lines = file1.readlines()

verticies = set()
# Strips the newline character
for line in Lines:

    splitted = line.split(' ')
    verticies.add(splitted[0].strip())
    verticies.add(splitted[1].strip())

mapper = {}
mapper1 = {}
id = 0
for val in verticies:
    mapper[id] = val
    mapper1[id]=val.strip("[]").split(",")
    id+=1

inv_map = {v: k for k, v in mapper.items()}

# Given N
N = len(verticies)
parent = [0] * N
# Given edges
edges = []
new_verticies= []

for line in Lines:
    splitted = line.split(' ')
    v1 = inv_map[splitted[0].strip()]
    v2 = inv_map[splitted[1].strip()]
    edges.append([v1,v2])
print("Pocet grafov na zaciatku: ")
printAnswer(N, edges)

for k in range (N):
    group = -1
    from_e = -1
    to_e = -1
    min_d = 9999999999
    for n in range (N):
        for i in range (N):
            for j in range(i,N):
                if parent[i] != parent[j] :
                    dist =  math.hypot(int(mapper1[i][0]) - int(mapper1[j][0]), int(mapper1[i][1]) - int(mapper1[j][1]))
                    if dist < min_d :
                        min_d = dist
                        from_e = i
                        to_e = j
    if from_e > -1:
        edges.append([from_e,to_e])
        new_verticies.append([mapper[from_e], mapper[to_e]])
        tmp = parent[to_e]
        join(tmp,parent[from_e])

final_d=0
for vertex in new_verticies :
    a = vertex[0].strip("[]'").split(",")
    b = vertex[1].strip("[]'").split(",")
    d= math.hypot(int(a[0]) - int(b[0]), int(a[1]) - int(b[1]))
    final_d+= d

print("Distance : " + str(final_d))
# open file in write mode
with open('output1', 'w') as fp:
    for item in new_verticies:
        # write each item on a new line
        fp.write("%s\n" % item)

print("Pocet grafov na konci: ")
printAnswer(N, edges)