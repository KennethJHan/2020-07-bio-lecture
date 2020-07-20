import sys

f = sys.argv[1]
d = {}

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip(): # ACGTACGTAAAA
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
print(d)

