# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
total=0
s=[]
number_of_shoes = input()
all_shoes_size = Counter(list(input().split()))
num_customers  = input()

for n in range(int(num_customers)):
    s.append((input().split()))
    if   all_shoes_size[s[n][0]]>0:
        total +=int(s[n][1])
        all_shoes_size[s[n][0]] = all_shoes_size[s[n][0]]-1
print(total)
        
