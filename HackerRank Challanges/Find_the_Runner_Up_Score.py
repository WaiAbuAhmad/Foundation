if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


list1=list(arr)


z = max(list1)
while max(list1) == z:
    list1.remove(max(list1))

print (max(list1))
