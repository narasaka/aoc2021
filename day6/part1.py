inpf = "sample"
with open(inpf, "r") as f:
    Fish = list(map(int, f.read().strip().split(",")))

for i in range(80):
    temp = []
    for fish in Fish:
        if fish == 0:
            temp.append(6)
            temp.append(8)
        else:
            temp.append(fish-1)

    Fish = temp

print(len(Fish))
