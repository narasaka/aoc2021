from collections import defaultdict

inpf = "in"
with open(inpf, "r") as f:
    Fish = list(map(int, f.read().strip().split(",")))

#there's only 9 types of fish bcos days to spawn are maxed at 8 (0-8)
sim = [0 for i in range(9)]
for fish in Fish:
    sim[fish] += 1

for i in range(256):
    temp = [0 for i in range(9)]
    for i in range(9):
        if i == 0:
            temp[6] += sim[i]
            temp[8] += sim[i]
        else:
            temp[i-1] += sim[i]
            
    sim = temp

print(sum(sim))


# idea
# 0 1 1 2 1 0 0 0 0 (sample init values)
# 1 1 2 1 0 0 0 0 0 (after 1 day)
# 1 2 1 0 0 0 1 0 1 (after 2 days)
# move everything down, add value at [0] to [6] and [8]
# print sum of array after 256 iterations
