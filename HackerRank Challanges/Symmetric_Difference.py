# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
list1 = input().split()
M = int(input())
list2 = input().split()

list3=(set(list1).difference(set(list2))).union(set(list2).difference(set(list1)))
list3= list(map(int,list3))
for item in sorted(list3):
    print(item)

