lines = open("../in/input02.txt").read().splitlines()

count = 0
for line in lines:
    line = line.replace('-',' ').replace(':','').split(' ')
    # print(line)
    # print(line[3].count(line[2]))
    if int(line[0]) <= line[3].count(line[2]) <= int(line[1]):
        count = count + 1

print('part 1: ',count)

lines = open("../in/input02.txt").read().splitlines()

count = 0
for line in lines:
    line = line.replace('-',' ').replace(':','').split(' ')
    strarr = list(line[3])
    # print(strarr)
    v = 0
    if strarr[int(line[0])-1] == line[2]:
        v = v + 1
    if strarr[int(line[1])-1] == line[2]:
        v = v + 1
    if v == 1:
        count = count + 1
    # print(line)
    # print(line[3].count(line[2]))

print('part 2: ',count)
