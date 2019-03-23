from itertools import permutations
# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()
S=S.split()

L=sorted(list(permutations(S[0],int(S[1]))))
for item in L:
    print("".join(item))

