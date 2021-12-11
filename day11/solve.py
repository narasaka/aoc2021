import numpy as np
infp = "in"
with open(infp, "r") as f:
    octopi = f.read().strip().split('\n')


octopi = [list(map(int, list(i))) for i in octopi]
flashes = 0
day = 0
p1 = 0
p2 = 0

while True:
    day += 1
    # add 1
    for i in range(10):
        for j in range(10):
            octopi[i][j] += 1
    # flash
    found = False
    while True:
        ok = True
        flashing = 0
        for i in range(10):
            for j in range(10):
                if octopi[i][j] == 0:
                    flashing += 1
                if octopi[i][j] > 9:
                    flashes += 1
                    ok = False
                    top = i-1>=0
                    bot = i+1<10
                    left = j-1>=0
                    right = j+1<10
                    octopi[i][j] = 0

                    if top and left and octopi[i-1][j-1] != 0:
                        octopi[i-1][j-1] += 1
                    if top and octopi[i-1][j] != 0:
                        octopi[i-1][j] += 1
                    if top and right and octopi[i-1][j+1] != 0:
                        octopi[i-1][j+1] += 1
                    if right and octopi[i][j+1] != 0:
                        octopi[i][j+1] += 1
                    if bot and right and octopi[i+1][j+1] != 0:
                        octopi[i+1][j+1] += 1
                    if bot and octopi[i+1][j] != 0:
                        octopi[i+1][j] += 1
                    if bot and left and octopi[i+1][j-1] != 0:
                        octopi[i+1][j-1] += 1
                    if left and octopi[i][j-1] != 0:
                        octopi[i][j-1] += 1

        if flashing == 100:
            p2 = day
            found = True
        if ok:
            break

    if day == 100:
        p1 = flashes
    if found:
        break


    print(day)
    print(np.matrix(octopi))
    print()

print('Part 1:', p1)
print('Part 2:', p2)

# 11111
# 19991
# 19191
# 19991
# 11111

# 2  2  2  2  2
# 2 10 10 10  2
# 2 10  2 10  2
# 2 10 10 10  2
# 2  2  2  2  2

# 3  4  5  4  3
# 4  0  0  0  4
# 5  0  0  0  5
# 3  0  0  0  4
# 3  4  5  4  3
