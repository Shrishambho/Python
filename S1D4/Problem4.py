from itertools import permutations

string = "abc"
res = list(permutations(string))

for p in res:
    print(''.join(p))
