from collections import defaultdict, deque

inpf = "in"
with open(inpf, 'r') as f:
    edges = f.read().strip().split()
    
adj = defaultdict(list)

for edge in edges:
    a, b = edge.split('-')
    adj[a].append(b)
    adj[b].append(a)

ends = {'start', 'end'}

def p1():
    paths = 0
    q = deque()
    q.append(('start', {'start'}, ""))
    while(q):
        curr, seen, smol = q.popleft()
        if curr == 'end':
            paths += 1
            continue
        for u in adj[curr]:
            if u not in seen:
                temp = set(seen)
                if u.islower():
                    temp.add(u)
                q.append((u, temp, smol))
    return paths

def p2():
    paths = 0
    q = deque()
    q.append(('start', {'start'}, ""))
    while(q):
        curr, seen, smol = q.popleft()
        if curr == 'end':
            paths += 1
            continue
        for u in adj[curr]:
            if u not in seen:
                temp = set(seen)
                if u.islower():
                    temp.add(u)
                q.append((u, temp, smol))
            if u in seen and u not in ends and smol == "":
                q.append((u, seen, u))
    return paths

print(p1())
print(p2())
