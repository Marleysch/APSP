from venv import create


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
    steps = [adjacency]
    empty_matrix = [[0 for _ in range(order)] for _ in range(order)]
    for k in range(order-2):
        curr_m = empty_matrix
        prev_m = steps[-1]
        for j in range(order):
            for i in range(order):
                curr_m[j][i] = min([(prev_m[j][v] + adjacency[v][i]) for v in range(order)])
            print(f'row {j} done')
        steps.append(curr_m)
        print(f'step {k} done')
    return steps

def shortest_path(start, finish, steps):
    return min([step[start-1][finish-1] for step in steps])

def main():
    order = 5
    edge_list = create_matrix("test.txt")
    print(edge_list)
    adjacency_matrix = create_adjacency_from_edge_m(edge_list, order)
    print(adjacency_matrix)
    APSP_matrix = create_APSP(adjacency_matrix)
    userinput = ''
    while userinput != 'quit':
        j = int(input('Enter the point you would like to start at: '))
        i = int(input('Enter the point you would like to end at: '))
        print(f'The shortest distance from {j} to {i} is {shortest_path(j,i,APSP_matrix)}')
        userinput = input('Would you like to go again? Type quit if no: ')

if __name__ == "__main__":
    main()