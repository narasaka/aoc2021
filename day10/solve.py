infp = "in"
with open(infp, "r") as f:
    lines = f.read().strip().split('\n')



closer = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'}

opener = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
        '>' : '<'}

c_points = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137}

i_points = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4}

# corrupted
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

# incomplete
# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.

cc = 0
iis = []
for line in lines:
    st = []
    ii = 0
    corrupted = False
    for c in line:
        if c in closer.keys():
            st.append(c)
        else:
            if st[-1] != opener[c]:
                corrupted = True
                cc += c_points[c]
                break
            else:
                st.pop()

    if not corrupted:
        while len(st):
            ii *= 5
            ii += i_points[closer[st[-1]]]
            st.pop()
        iis.append(ii)

iis.sort()
print("Part 1:", cc)
print("Part 2:", iis[len(iis)//2])





