#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it_greedy(input_data):
    # Modify this code to run your optimization algorithm
    Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1]), float(parts[0])/float(parts[1])))
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    # Ordenar la lista de items por densidad de valor para despues meterla al primer greedy
    # empezamos ordenando por densidad.
    items = sorted(items, key=lambda x: -x.density)
    value_0 = 0
    weight_0 = 0
    taken_0 = [0]*len(items)
    for item in items:
        if weight_0 + item.weight <= capacity:
            taken_0[item.index] = 1
            value_0 += item.value
            weight_0 += item.weight
    # Ordenamos por valor de menor a mayor
    items = sorted(items, key=lambda x: x.value)
    value_1 = 0
    weight_1 = 0
    taken_1 = [0] * len(items)
    for item in items:
        if weight_1 + item.weight <= capacity:
            taken_1[item.index] = 1
            value_1 += item.value
            weight_1 += item.weight
    # Ordenamos por valor de mayor a menor
    items = sorted(items, key=lambda x: -x.value)
    value_2 = 0
    weight_2 = 0
    taken_2 = [0] * len(items)
    for item in items:
        if weight_2 + item.weight <= capacity:
            taken_2[item.index] = 1
            value_2 += item.value
            weight_2 += item.weight
    # Comparar los valores y elegimos el mejor
    if value_0 >= value_1:
        if value_0 >= value_2:
            taken = taken_0
            value = value_0
        else:
            taken = taken_2
            value = value_2
    elif value_0 < value_1:
        if value_1 >= value_2:
            taken = taken_1
            value = value_1
        else:
            taken = taken_1
            value = value_1
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def solve_it_DP(input_data):
    # parse the input

    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full

    def DP(k, j):
        if k == j:
            return 0
        elif items[j].weight <= k:
            return max(DP(k, j-1), items[j].value + DP(k-items[j].weight, j-1))
        else:
            return DP(k, j-1)
    # prepare the solution in the specified output format
    output_data = DP(capacity, item_count-1)
    # output_data = str(value) + ' ' + str(0) + '\n'
    # output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        # file_location = '.\data\ks_4_0'
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it_greedy(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

