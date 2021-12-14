import sys
from collections import defaultdict
inpf = sys.argv[1] if len(sys.argv)>1 else "in"
with open(inpf, 'r') as f:
    lines = f.read().strip().split('\n')

mp = {}
for i in range(2, len(lines)):
    a, b = lines[i].split(' -> ')
    mp[a] = b


def solve(steps):
    start = lines[0]
    pairs = defaultdict(int) #pair : number of times it appeared
    for i in range(len(start)-1):
        pairs[start[i]+start[i+1]] += 1

    for t in range(steps):
        temp = defaultdict(int)
        for pair in pairs:
            temp[pair[0]+mp[pair]] += pairs[pair]
            temp[mp[pair]+pair[1]] += pairs[pair]
        pairs = temp

    elements = defaultdict(int) #element : number of times it appeared
    for pair in pairs:
        # just count the first character
        # bcos the second character will appear
        # in some other pair as its first character
        # except for the last character (which we didn't touch)
        # aka -> last character of start == last character of modified start
        elements[pair[0]] += pairs[pair]
    elements[start[-1]] += 1

    mx = max(elements.values())
    mn = min(elements.values())
    return mx-mn

print("Part 1:", solve(10))
print("Part 2:", solve(40))
