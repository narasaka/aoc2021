import matplotlib.pyplot as plt
inpf = "in"
with open(inpf, 'r') as f:
    lines = f.read().strip().split('\n')

mark = lines.index('')
dots = set([tuple(map(int, lines[i].split(','))) for i in range(mark)])
folds = [lines[i].split()[2].split('=') for i in range(mark+1, len(lines))]

def Y(n):
    a, b = n
    return b

first = True
for fold in folds:
    temp = set(dots)
    axis, n = fold
    n = int(n)
    for dot in dots:
        x, y = dot
        diff_x = x-n
        diff_y = y-n
        if x > n and axis == 'x':
            temp.remove(dot)
            temp.add((n-diff_x, y))
        if y > n and axis == 'y':
            temp.remove(dot)
            temp.add((x, n-diff_y))
    if first:
        print(len(temp))
        first = False
    dots = set(temp)

x = [x for x, y in dots]
y = [-y for x, y in dots]
plt.plot(x, y, 'o')
plt.show()
