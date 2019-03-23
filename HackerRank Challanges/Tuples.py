if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

my_list= list(integer_list)
print(hash(tuple(my_list)))