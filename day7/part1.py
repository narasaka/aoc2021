inpf = "in"
with open(inpf, "r") as f:
    crabs = list(map(int, f.read().strip().split(',')))

crabs.sort()
target = crabs[len(crabs)//2]

fuel = 0
for crab in crabs:
    fuel += abs(target-crab)

print(fuel)
