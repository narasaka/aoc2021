inpf = "in"
with open(inpf, "r") as f:
    crabs = list(map(int, f.read().strip().split(',')))

crabs.sort()
fuels = []

#idk lets just brute force
for i in range(crabs[len(crabs)-1]):
    fuel = 0
    target = i
    for crab in crabs:
        distance = abs(target-crab)
        fuel += distance*((1+distance)/2)
    fuels.append(fuel)

print(min(fuels))

#oh it worked lmao
