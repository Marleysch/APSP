import random
import sys
import time

import numpy as np

def create_adjacency_from_edge_m(edge_m):

    order = max([max(edge[0], edge[1]) for edge in edge_m])

    adjacency = [[float('inf') for _ in range(order)] for _ in range(order)]

    for edge in edge_m:
        adjacency[edge[0]-1][edge[1]-1] = edge[2]
        adjacency[edge[1] - 1][edge[0] - 1] = edge[2]

    for i in range(len(adjacency)):
        for j in range(len(adjacency[i])):
            if i == j:
                adjacency[i][j] = 0

    return adjacency

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

def create_APSP(adjacency):
    order = len(adjacency)

    shortest_path_m = adjacency
    for k in range(order-2):
        for j in range(order):
            for i in range(order):
                shortest_path_m[j][i] = min(shortest_path_m[j][i], shortest_path_m[j][k] + shortest_path_m[k][i])

        print(f'step {k} done')

    return shortest_path_m

def main():

    edge_list = create_matrix("graph.txt")
    # matrix = floyd_warshall(edge_list, 1000)
    matrix = create_APSP(create_adjacency_from_edge_m(edge_list))
    j = ''

    while j != 'quit':
        j = int(input('Enter the point you would like to start at: '))
        i = int(input('Enter the point you would like to end at: '))
        # print(f'The shortest distance from {j} to {i} is {shortest_path(j,i,matrix)}')
        print(f'The shortest distance from {j} to {i} is {matrix[j-1][i-1]}')


if __name__ == "__main__":
    main()