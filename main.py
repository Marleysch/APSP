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
    adjacency_valid = [[-1 for _ in range(order)] for _ in range(order)]
    for i in range(order):
        for j in range(order):
            if adjacency[i][j] != float('inf'):
                adjacency_valid[j][i] = i
    adjacency_valid = [[x for x in adjacency_valid[i] if x != -1] for i in range(len(adjacency_valid))]

    print(adjacency_valid)

    steps = [adjacency]
    empty_matrix = [[0 for _ in range(order)] for _ in range(order)]
    for k in range(order-2):
        curr_m = empty_matrix
        prev_m = steps[-1]
        for j in range(order):
            if j < 1:
                valid_vs = []
                for v in range(order):
                    if prev_m[j][v] != float('inf'):
                        valid_vs.append(v)

            for i in range(order):

                if i == j:
                    curr_m[j][i] = 0
                else:
                    tests = [(prev_m[j][v] + adjacency[v][i]) for v in adjacency_valid[i]]
                    if len(tests) == 0:
                        curr_m[j][i] = float('inf')
                    else:
                        curr_m[j][i] = min(tests)

            print(f'row {j} done')
        print(curr_m)
        steps.append(curr_m)
        print(f'step {k} done')
    return steps

def shortest_path(start, finish, steps):
    return min([step[start-1][finish-1] for step in steps])

def main():
    order = 1000

    edge_list = create_matrix("graph.txt")
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