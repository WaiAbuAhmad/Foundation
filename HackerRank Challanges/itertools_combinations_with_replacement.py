from itertools import combinations_with_replacement
# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()
S=S.split()
L=list(combinations_with_replacement(sorted(S[0]),int(S[1])))

for item in L:
    print("".join(item))
