import re

rule_pat = re.compile(r'(\d+) ([a-z ]+) bag')

with open('../in/input07.txt', 'r') as f:
    rules = {}
    # Read out the dependencies
    for l in f:
        data = l.split(' ', 4)
        target = ' '.join(data[0:2])
        for item in rule_pat.findall(data[-1]):
            if item[1] not in rules.keys():
                rules[item[1]] = []
            rules[item[1]].append(target)
    # Work out how many different bags contain can contain a shiny gold bag
    bags = set()
    buffer = rules['shiny gold'].copy()
    for container in buffer:
        if container not in bags:
            bags.add(container)
            if container in rules:
                buffer.extend(rules[container])
    print(f'Part 1: {len(bags)}')

with open('../in/input07.txt', 'r') as f:
    rules = {}
    # Read the rules
    for l in f:
        data = l.split(' ', 4)
        container = ' '.join(data[0:2])
        rules[container] = [(item[1], int(item[0])) for item in rule_pat.findall(data[-1])]
    # Work out how many bags inside
    buffer = rules['shiny gold'].copy()
    count = 0
    for bag in buffer:
        count += bag[1]
        buffer.extend(bag[1] * rules[bag[0]])
    print(f'Part 2: {count}')