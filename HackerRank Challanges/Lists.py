if __name__ == '__main__':
    N = int(input())
game_list =[]

for i in range (N):
    command = input()
    command = command.split()
    if command[0]=="insert" :
        game_list.insert(int(command[1]),int(command[2]))
    if command[0]=="print" :
        print(game_list)
    if command[0]=="remove" :
        game_list.remove(int(command[1]))
    if command[0]=="append" :
        game_list.append(int(command[1]))
    if command[0]=="sort" :
        game_list.sort()
    if command[0]=="pop" :
        game_list.pop()
    if command[0]=="reverse" :
        game_list.reverse()
        