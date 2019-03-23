from itertools import groupby

s=input()
t=set()
L=[]
for k, g in groupby(s, key=None):
    L.append(((len(list(g))),int(k)))
    t=L
for item in t:
    print(item,"" ,end="")
    
