from itertools import combinations
# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()
S=S.split()


for i in range(int(S[1])):
    L=list(combinations(sorted(S[0]),i+1))
    for item in L:
        print("".join(item))
