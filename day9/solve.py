infp = "in"
with open(infp, "r") as f:
    heightmap = f.read().strip().split('\n')


seen = [[False for x in heightmap[0]] for y in heightmap]
areas = []
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def dfs(x, y, prev):
    area = 0
    if y<0 or y>=len(heightmap) or x<0 or x>=len(heightmap[0]): return 0
    if seen[y][x]: return 0

    curr = int(heightmap[y][x])
    if curr == 9: return 0
    if curr > prev:
        area += 1
        seen[y][x] = True
    else:
        return 0

    for move in moves:
        area += dfs(x+move[0], y+move[1], curr)

    return area

def find_lows():
    lows = []
    risk = 0
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            curr = int(heightmap[y][x])
            top = 10 if y-1<0 else int(heightmap[y-1][x])
            bot = 10 if y+1>=len(heightmap) else int(heightmap[y+1][x])
            left = 10 if x-1<0 else int(heightmap[y][x-1])
            right = 10 if x+1>=len(heightmap[0]) else int(heightmap[y][x+1])

            if curr < top and curr < bot and curr < left and curr < right:
                lows.append((x, y))
                risk += curr+1

    return (lows, risk)

lows, p1 = find_lows()
for low in lows:
    areas.append(dfs(low[0], low[1], -1))

p2 = 1
areas.sort(reverse=True)
for i in range(3):
    p2 *= areas[i]

print("Part 1:", p1)
print("Part 2:", p2)
