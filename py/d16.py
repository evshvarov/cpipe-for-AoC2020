#!/usr/bin/python
# Floris Douw
# 2020
#
# AoC 2020 Day 16: Ticket Translation

import re


def clear_index_from_column(columns, name, index):
    if len(columns[name]) > 1:
        columns[name].remove(index)
        if len(columns[name]) == 1:
            j = columns[name][0]
            for cn in columns:
                if cn != name and j in columns[cn]:
                    clear_index_from_column(columns, cn, j)


rule_pattern = re.compile(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)')

with open('../in/input16.txt', 'r') as f:
    # Part 0: Read rules and ticket data
    rawinput = f.read().split('\n\n')

    rules = {}
    for match in rule_pattern.finditer(rawinput[0]):
        name, a, b, c, d = match.groups()
        rules[name] = set.union(set(range(int(a), int(b)+1)), range(int(c), int(d)+1))
    all_fields = set.union(*rules.values())

    myticket = [int(n) for n in rawinput[1].splitlines()[1].split(',')]

    nearbytickets = [
        [int(n) for n in line.split(',')] for line in rawinput[2].splitlines()[1:]
    ]

    # Part 1: compute checksum
    checksum = sum(num for ticket in nearbytickets for num in ticket if num not in all_fields)
    print(f'Part 1: {checksum}')

    # Part 2
    # Filter out invalid tickets
    # Create a copy: if you remove items from the list you're iterating over, you will skip some items
    # Some consecutive tickets are invalid and you would miss the second one
    valid_tickets = [ticket for ticket in nearbytickets if all(num in all_fields for num in ticket)]

    # Match colums
    ncols = len(myticket)
    columns = {name: [*range(ncols)] for name in rules}
    for ticket in valid_tickets:  # inc. myticket?
        for col_index, num in enumerate(ticket):
            for name in columns:
                if num not in rules[name] and col_index in columns[name]:
                    clear_index_from_column(columns, name, col_index)

    # Collect data from myticket
    total = 1
    for name in columns:
        if name.startswith('departure'):
            total *= myticket[columns[name][0]]

    print(f'Part 2: {total}')