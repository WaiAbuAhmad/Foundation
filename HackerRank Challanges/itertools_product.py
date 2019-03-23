# Enter your code here. Read input from STDIN. Print output to STDOUT

a = input()
b = input()
l=tuple()
A=a.split()
B  = b.split()
for i in range(len(A)):
    for j in range(len(B)):
        l=tuple((int(A[i]),int(B[j])))
        print(l,"",end="")

