
import copy

def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm for finding all-pairs shortest paths.

    Args:
        graph (list): A 2D list representing the adjacency matrix of the graph.

    Returns:
        list: A 2D list representing the shortest path distances between all pairs of vertices.
    """

    n = len(graph)
    dist = [row[:] for row in graph]

    # Update the distance matrix considering all vertices as intermediate vertices.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        print(f'row {k} done')

    return dist

def create_matrix(file):
    with open(file, 'r') as file:
        content = file.read()
    content = content.replace(" ", "")
    content = content.replace("{", "")

    matrix = []
    row = []
    num = ''
    i = 0
    stop = len(content)
    while i != stop:
        if content[i] == '}':
            num = int(num)
            row.append(num)
            num = ''
            matrix.append(row)
            row = []
            i += 2
        elif content[i] == ',':
            num = int(num)
            row.append(num)
            num = ''
            i += 1
        else:
            num += content[i]
            i += 1

    return matrix

def create_adjacency_from_edge_m(edge_m, order):
    adjacency = [[-1 for _ in range(order)] for _ in range(order)]
    for edge in edge_m:
        adjacency[edge[0]-1][edge[1]-1] = edge[2]
    for i in range(len(adjacency)):
        for j in range(len(adjacency[i])):
            if i == j:
                adjacency[i][j] = 0
            if adjacency[i][j] == -1:
                adjacency[i][j] = float('inf')
    return adjacency


def create_APSP(adjacency):
    order = len(adjacency)

    adjacency_valid = [[-1 for _ in range(order)] for _ in range(order)]
    adjacency_p_valid = [[-1 for _ in range(order)] for _ in range(order)]
    for j in range(order):
        for i in range(order):
            if adjacency[j][i] != float('inf'):
                adjacency_valid[i][j] = j
                adjacency_p_valid[j][i] = i
    adjacency_valid = [[x for x in adjacency_valid[i] if x != -1] for i in range(len(adjacency_valid))]
    adjacency_p_valid = [[x for x in adjacency_p_valid[i] if x != -1] for i in range(len(adjacency_valid))]
    for i in range(order):
        adjacency_valid[i] = set(adjacency_valid[i])
        adjacency_p_valid[i] = set(adjacency_p_valid[i])
    curr_m_valid = adjacency_p_valid

    steps = [adjacency]
    curr_m = [[0 for _ in range(order)] for _ in range(order)]
    for k in range(order-2):
        prev_m = steps[-1]
        next_m_valid = []

        for j in range(order):
            next_m_row = set()

            for i in range(order):
                if i == j:
                    curr_m[j][i] = 0
                else:
                    tests = [(prev_m[j][v] + adjacency[v][i]) for v in curr_m_valid[j] & adjacency_valid[i]]
                    if len(tests) == 0:
                        curr_m[j][i] = float('inf')
                    else:
                        curr_m[j][i] = min(tests)

                if curr_m[j][i] != float('inf'):
                    next_m_row.add(i)

            next_m_valid.append(next_m_row)

        curr_m_valid = next_m_valid
        steps.append(curr_m)
        print(f'step {k} done')
    return steps

def shortest_path(start, finish, steps):
    return min([step[start-1][finish-1] for step in steps])

def main():
    order = 1000

    edge_list = create_matrix("graph.txt")

    adjacency_matrix = create_adjacency_from_edge_m(edge_list, order)
    matrix = floyd_warshall(adjacency_matrix)
    # APSP_matrix = create_APSP(adjacency_matrix)
    userinput = ''
    while userinput != 'quit':
        j = int(input('Enter the point you would like to start at: '))
        i = int(input('Enter the point you would like to end at: '))
        # print(f'The shortest distance from {j} to {i} is {shortest_path(j,i,matrix)}')
        print(f'The shortest distance from {j} to {i} is {matrix[j-1][i-1]}')
        userinput = input('Would you like to go again? Type quit if no: ')

if __name__ == "__main__":
    main()