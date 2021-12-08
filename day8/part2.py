"""

 0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""

import itertools

inpf = "in"
with open(inpf, "r") as f:
    segments = f.read().strip().split('\n')

patterns = {
        0 : 'abcefg',
        1 : 'cf',
        2 : 'acdeg',
        3 : 'acdfg',
        4 : 'bcdf',
        5 : 'abdfg',
        6 : 'abdefg',
        7 : 'acf',
        8 : 'abcdefg',
        9 : 'abcdfg'
        }

def perm(signals):
    letters = "abcdefg"
    for p in itertools.permutations(letters):
        matched = True
        temp = {}
        for i in range(len(letters)):
            temp[letters[i]] = p[i]
        for signal in signals:
            seq = ""
            for s in signal:
                seq += temp[s]
            seq = ''.join(sorted(seq))
            if seq not in patterns.values():
                matched = False
        if matched:
            return temp

ans = 0
for segment in segments:
    segment = segment.split('|')
    signals = segment[0].split()
    outputs = segment[1].split()

    mp = perm(signals)
    num = ''
    for output in outputs:
        seq = ''
        for c in output:
            seq += mp[c]
        seq = ''.join(sorted(seq))
        for k, v in patterns.items():
            if v == seq:
                num += str(k)
    ans += int(num)

print(ans)

        


